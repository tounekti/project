# -*- coding: utf-8 -*-

"""
Template pages.
"""

import os
from time import sleep
import web

from . import auth
from . import AuthError
from . import check_token, make_token


__all__ = ["login_form", "Login", "Logout", "Captcha", "ResetToken", "ResetChange"]


# Will mapping to local templates path
curdir = os.path.abspath(os.path.dirname(__file__))
local_template_path = os.path.join(curdir, 'templates/')
render = web.template.render(local_template_path)


def login_form():
    auth_error = auth.session.get('auth_error', '')
    if auth_error:
        del auth.session['auth_error']
    form = web.template.Template('''
    <form action="%s" method="post" accept-charset="utf-8">
      <p>
        <label for="login">Username:</label>
        <input type="text" name="login" id="login"
               maxlength="254" tabindex="1" />
      </p>
      <p>
        <label for="password">Password:</label>
        <input type="password" name="password" id="password"
               maxlength="254" tabindex="2" />
      </p>
      <p class="submit">
        <button type="submit">Log in</button>
      </p>
    </form>
    ''' % (auth.config.url_login,))
    form.auth_error = auth_error
    return form


class Login(object):
    def GET(self, template=None):
        if 'user' in auth.session.keys():
            web.found(auth.config.url_after_login)
            return

        template = template or auth.config.template_login or render.login

        auth_error = auth.session.get('auth_error', '')
        if auth_error:
            del auth.session['auth_error']

        return template(error=auth_error,
                        captcha_on=auth.session.get('captcha_on', False),
                        url_reset=auth.config.url_reset_token)

    def POST(self):
        # artificial delay (to slow down brute force attacks)
        sleep(auth.config.forced_delay)

        i = web.input()
        login = i.get('login', '').strip()
        password = i.get('password', '').strip()

        captcha_on = auth.session.get('captcha_on', False)

        if captcha_on:
            try:
                checkcode_input = i.get('captcha').strip().lower()
                checkcode_session = auth.session.captcha_checkcode.lower()

                if not checkcode_input == checkcode_session:
                    raise AuthError('Captcha validation failed: Wrong checkcode!')
            except (AttributeError, AuthError):
                auth.session.auth_error = 'captcha_wrong'
                web.found(auth.config.url_login)
                return

        user = auth.authenticate(login, password)
        if not user:
            auth.session.auth_error = 'fail'
            if auth.config.captcha_enabled == True:
                auth.session.captcha_on = True
            web.found(auth.config.url_login)
            return
        elif user.user_status == 'suspended':
            auth.session.auth_error = 'suspended'
            if auth.config.captcha_enabled == True:
                auth.session.captcha_on = True
            web.found(auth.config.url_login)
            return
        else:
            auth.login(user)
        url_next = auth.session.get('url_next', auth.config.url_after_login)
        try:
            del auth.session['url_next']
        except KeyError:
            pass
        try:
            # auth.session.captcha_on = False
            del auth.session['captcha_on']
            del auth.session['captcha_checkcode']
        except KeyError:
            pass
        web.found(url_next)
        return


class Captcha(object):
    def GET(self):
        if ((not auth.config.captcha_enabled) or
                (not auth.session.get('captcha_on', False))):
            return

        try:
            captcha, checkcode = auth.config.captcha_func()
        except (AttributeError, TypeError):
            return

        try:
            if not isinstance(checkcode, basestring):
                raise TypeError("Captcha checkcode should be a string.")

            captcha_img = captcha.getvalue()
            if not isinstance(captcha_img, str):
                raise TypeError("Captcha image should be a str instance, "
                                "the value or content of a cStringIO.StringO or "
                                "StringIO.StringO object.")
        except TypeError:
            return

        auth.session.captcha_checkcode = checkcode
        return captcha_img


class Logout(object):
    def GET(self):
        auth.logout()
        web.found('/')
        return


class ResetToken(object):
    def GET(self, template=None):
        template = (template or
                    auth.config.template_reset_token or
                    render.reset_token)
        token_sent = auth.session.get('auth_token_sent', False)
        if token_sent:
            del auth.session['auth_token_sent']
        return template(done=token_sent)

    def POST(self, email_template=None):
        template = (email_template or
                    auth.config.template_reset_email or
                    render.reset_email)
        i = web.input()
        login = i.get('login', '').strip()
        try:
            if not login:
                raise AuthError

            query_where = web.db.sqlwhere({'user_login': login,
                                           auth.config.db_email_field: login},
                                          ' OR ')
            user = auth.db.select('user', where=query_where).list()
            if not user:
                raise AuthError

            user = user[0]

            from_address = auth.config.email_from
            to_address = user[auth.config.db_email_field]
            token = make_token(user)
            token_url = '%s%s/%s$%s' % (web.ctx.home,
                                        auth.config.url_reset_change,
                                        user.user_id,
                                        token)
            message = template(token_url)
            subject = message.get('Subject', 'Password reset').strip()
            headers = dict(message)
            del headers['__body__']
            if 'ContentType' in headers:
                headers['Content-Type'] = headers['ContentType'].strip()
                del headers['ContentType']
            web.utils.sendmail(from_address,
                               to_address,
                               subject,
                               str(message),
                               headers)
        except (AuthError, IOError):
            pass

        auth.session.auth_token_sent = True
        web.found(web.ctx.path)


class ResetChange(object):
    def GET(self, uid, token, template=None):
        # artificial delay (to slow down brute force attacks)
        sleep(auth.config.forced_delay)

        template = (template or
                    auth.config.template_reset_change or
                    render.reset_change)
        try:
            user = auth.db.select('user',
                                  where='user_id = $uid',
                                  vars={'uid': uid}).list()
            if ((not user) or
                    (not check_token(user[0],
                                     token,
                                     auth.config.reset_expire_after))):
                raise AuthError
        except AuthError:
            auth_error = 'expired'
        else:
            auth_error = auth.session.get('auth_error', '')
            if auth_error:
                del auth.session['auth_error']
        return template(error=auth_error, url_reset=auth.config.url_reset_token)

    def POST(self, uid, token):
        # artificial delay (to slow down brute force attacks)
        sleep(auth.config.forced_delay)

        i = web.input()
        password = i.get('password', '').strip()
        password2 = i.get('password2', '').strip()
        try:
            user = auth.db.select('user',
                                  where='user_id = $uid',
                                  vars={'uid': uid}).list()
            if not user:
                raise AuthError('expired')
            user = user[0]
            if not check_token(user, token, auth.config.reset_expire_after):
                raise AuthError('expired')
            if password != password2:
                raise AuthError('match')
            if len(password) < auth.config.password_minlen:
                raise AuthError('bad password')

            auth.set_password(user.user_login, password)
            auth.login(user)
        except AuthError as e:
            auth.session.auth_error = str(e)
            web.found(web.ctx.path)
            return

        web.found(auth.config.url_after_login)
        return
