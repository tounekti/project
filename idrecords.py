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
        "/checkout", "Checkout",
        "/tapes", "Tapes",
        "/merch_clothing", "MerchClothing",
        "/records_product", "RecordsProduct",
        "/vinyl_used", "VinylUsed",
        "/tapes_used_hiphop", "TapesUsedHiphop",
        "/info_gdpr", "InfoGdpr",
        "/customer_returns", "CustomerReturns",
        "/extras_affiliate", "ExtrasAffiliate",
        "/newvinyl_dance_hiphop", "NewVinylDanceHiphop",
        "/new_tapes_hiphop", "NewTapesHiphop",
        "/used_hiphop_albums", "UsedHiphopAlbums",
        "/used_hiphop_singles", "UsedHiphopSingles",
        "/used_dansk_hiphop_albums","UsedDanskHiphopAlbums",
        "/used_dansk_hiphop_singles","UsedDanskHiphopSingles",
        "/used_beats","UsedBeats",
        "/used_hiphop_sued_norveg","UsedHipHopSuedNorveg",
        "/used_djtools","UsedDjTools",
        "/used_electro_hiphop","UsedElectroHiphop",
        "/used_electronic","UsedElectronic",
        "/used_funk_soul_disco","UsedFunkSoulDisco",
        "/used_jazz","UsedJazz",
        "/used_library","UsedLibrary",
        "/used_rock_pop","UsedRockPop",
        "/used_world","UsedWorld",
        "/used_reggae_ragga","UsedReggaeRagga",
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



class Checkout:

    def GET(self):
        """ Show page """
        return render.checkout(urlapp)      



class Tapes:

    def GET(self):
        """ Show page """
        return render.tapes(urlapp)    




class MerchClothing:

    def GET(self):
        """ Show page """
        return render.merch_clothing(urlapp)      


class RecordsProduct:

    def GET(self):
        """ Show page """
        return render.records_product(urlapp)           



class VinylUsed:

    def GET(self):
        """ Show page """
        return render.vinyl_used(urlapp)           

class TapesUsedHiphop:

    def GET(self):
        """ Show page """
        return render.tapes_used_hiphop(urlapp)    

class InfoGdpr:

    def GET(self):
        """ Show page """
        return render.info_gdpr(urlapp)    

class CustomerReturns:

    def GET(self):
        """ Show page """
        return render.customer_returns(urlapp)    


class ExtrasAffiliate:

    def GET(self):
        """ Show page """
        return render.extras_affiliate(urlapp)    


class NewVinylDanceHiphop:

    def GET(self):
        """ Show page """
        return render.newvinyl_dance_hiphop(urlapp)    

class NewTapesHiphop:

    def GET(self):
        """ Show page """
        return render.new_tapes_hiphop(urlapp)      
        

class UsedHiphopAlbums:

    def GET(self):
        """ Show page """
        return render.used_hiphop_albums(urlapp)      
        
class UsedHiphopSingles:

    def GET(self):
        """ Show page """
        return render.used_hiphop_singles(urlapp)   

class UsedDanskHiphopAlbums :
        
        
    def GET(self):
        """ Show page """
        return render.used_dansk_hiphop_albums(urlapp)   
        
        
class UsedDanskHiphopSingles :
        
        
    def GET(self):
        """ Show page """
        return render.used_dansk_hiphop_singles(urlapp)   
        
        
        
class UsedBeats :
        
        
    def GET(self):
        """ Show page """
        return render.used_beats(urlapp)   
        
class UsedHipHopSuedNorveg :
        
        
    def GET(self):
        """ Show page """
        return render.used_hiphop_sued_norveg(urlapp)   
        
        
class UsedDjTools :
        
        
    def GET(self):
        """ Show page """
        return render.used_djtools(urlapp)   
        
class UsedElectroHiphop :
    
    def GET(self):
        """ Show page """
        return render.used_electro_hiphop(urlapp)   
        

class UsedElectronic :
        
        
    def GET(self):
        """ Show page """
        return render.used_electronic(urlapp)   
        
        
class UsedFunkSoulDisco:
        
        
    def GET(self):
        """ Show page """
        return render.used_funk_soul_disco(urlapp)   
        

class UsedJazz:
        
        
    def GET(self):
        """ Show page """
        return render.used_jazz(urlapp)   
        

class UsedLibrary:
        
        
    def GET(self):
        """ Show page """
        return render.used_library(urlapp)   
        

class UsedRockPop:
        
        
    def GET(self):
        """ Show page """
        return render.used_rock_pop(urlapp)   
        
class UsedWorld:
        
        
    def GET(self):
        """ Show page """
        return render.used_world(urlapp)   


class UsedReggaeRagga:
        
        
    def GET(self):
        """ Show page """
        return render.used_reggae_ragga(urlapp)   
        
        





app = web.application(urls, globals())

if __name__ == "__main__":

	import builtins

	builtins.urlapp = "http://172.16.1.150:8080"

	builtins.sk_app = app

	app.run()
