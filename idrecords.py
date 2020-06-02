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
        "/cart", "Cart",
        "/vinyl", "Vinyl",
        "/cd_dvd", "CdDvd",
        "/sale", "Sale",
        "/vinyl_new", "VinylNew",
        "/tapes_new_hiphop", "TapesNewHiphop",
        "/merch_clothing_rekords", "MerchClothingRekordsProduct",
        "/merch_clothing_dengale", "MerchClothingDengale",
        "/cd_dvd_usuk", "CdDvdUsUk",
        "/cd_dvd_scand_singles", "CdDvdScandSinglesProduct",
        "/cd_dvd_scand_albums", "CdDvdScandAlbums",
        "/customer_sitemap", "CustomerSiteMap",
        "/extras_voucher", "ExtrasVoucher",
        "/used_tapes_hiphop", "UsedTapesHiphop",
        "/newvinyl_dance_hiphop", "NewVinylDanceHiphop",
        "/newninyl_funk_soul", "NewVinylFunkSoul",
        "/newvinyl_hiphop", "NewVinylHiphop",
        "/newvinyl_jazz", "NewVinylJazz",
        "/newvinyl_reggae", "NewVinylReggae",
        "/newvinyl_world", "NewVinylWorld",
        "/newvinyl_beats", "NewVinylBeats",
        "/new_tapes_hiphop", "NewTapesHiphop",
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

class Cart:

    def GET(self):
        """ Show page """
        return render.cart(urlapp)
        
class Vinyl:

    def GET(self):
        """ Show page """
        return render.vinyl(urlapp)

class CdDvd:

    def GET(self):
        """ Show page """
        return render.cd_dvd(urlapp)           

class Sale:

    def GET(self):
        """ Show page """
        return render.sale(urlapp)
        
class VinylNew:

    def GET(self):
        """ Show page """
        return render.vinyl_new(urlapp) 

class TapesNewHiphop:

    def GET(self):
        """ Show page """
        return render.tapes_new_hiphop(urlapp) 
        

class CdDvdScandSinglesProduct:

    def GET(self):
        """ Show page """
        return render.cd_dvd_scand_singles(urlapp) 
        
class CdDvdScandAlbums:

    def GET(self):
        """ Show page """
        return render.cd_dvd_scand_albums(urlapp)     
        
class  CdDvdUsUk:

    def GET(self):
        """ Show page """
        return render.cd_dvd_usuk(urlapp)          
        
        
class MerchClothingRekordsProduct:

    def GET(self):
        """ Show page """
        return render.merch_clothing_rekords(urlapp)         

class MerchClothingDengale:

    def GET(self):
        """ Show page """
        return render.merch_clothing_dengale(urlapp)    


class CustomerSiteMap:

    def GET(self):
        """ Show page """
        return render.customer_sitemap(urlapp)          

class ExtrasVoucher:

    def GET(self):
        """ Show page """
        return render.extras_voucher(urlapp)   
        
class UsedTapesHiphop:

    def GET(self):
        """ Show page """
        return render.used_tapes_hiphop(urlapp)  
        
class NewVinylDanceHiphop:

    def GET(self):
        """ Show page """
        return render.newvinyl_dance_hiphop(urlapp)       

class NewVinylFunkSoul:

    def GET(self):
        """ Show page """
        return render.newninyl_funk_soul(urlapp)      

class NewVinylHiphop:

    def GET(self):
        """ Show page """
        return render.newvinyl_hiphop(urlapp) 

class NewVinylJazz:

    def GET(self):
        """ Show page """
        return render.newvinyl_jazz(urlapp)    


class NewVinylReggae:

    def GET(self):
        """ Show page """
        return render.newvinyl_reggae(urlapp)         
        
class NewVinylWorld:

    def GET(self):
        """ Show page """
        return render.newvinyl_world(urlapp)       

class NewVinylBeats:

    def GET(self):
        """ Show page """
        return render.newvinyl_beats(urlapp)    

class NewTapesHiphop:

    def GET(self):
        """ Show page """
        return render.new_tapes_hiphop(urlapp)          

app = web.application(urls, globals())

if __name__ == "__main__":

	import builtins

	builtins.urlapp = "http://172.16.1.150:8080"

	builtins.sk_app = app

	app.run()
