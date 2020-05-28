""" Basic todo list using webpy 0.3 """
import web
import model

web.config.debug = False

### Url mappings

urls = ("/", "Index", 
		"/del/(\d+)", "Delete",
		"/privacypolicy", "PrivacyPolicy",
		"/contact", "Contact",
        "/account", "Account",
		)


### Templates
render = web.template.render("templates", base="base")


class Index:

    def GET(self):
        """ Show page """
        print ("bonjourlknsdjklsdfhhhqsdddddhhhhhiosdhsdwvuksdukfjkksdkjjk")
        print ("bosoirlknsdjklsdfhhhqsdddddhhhhhiosdhsdwvuksdukfjkksdkjjk")


        return render.index(urlapp)




class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother("/")

class PrivacyPolicy:

    def GET(self):
        """ Show page """
        return render.privacypolicy(urlapp)

class Contact:

    def GET(self):
        """ Show page """
        return render.contact(urlapp)
        
        
class Account:

    def GET(self):
        """ Show page """
        return render.account(urlapp)        





app = web.application(urls, globals())

if __name__ == "__main__":

	import builtins

	builtins.urlapp = "http://172.16.1.150:8080"

	builtins.sk_app = app

	app.run()
