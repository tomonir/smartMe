from lib.logger import Logger
import importlib

from lib.selenium_parger import SeleniumParger 


logger = Logger()


class Command(object):
    def __init__(self,fileds,selinum_parger):
        self.fields = fileds
        self.selinum_parger = selinum_parger
    def process(self):
        pass
    
class textFiled(Command):
    def __init__(self,fields,selinum_parger):
        super(self.__class__, self).__init__(fields,selinum_parger)

    def process(self):
        #print (self.fields)
        print (self.fields['filed_name'])
        print (self.fields['text'])
        self.selinum_parger.setTextFiled(self.fields['filed_name'],self.fields['text'])     
        
class search_button(Command):
    def __init__(self,fields,selinum_parger):
        super(self.__class__, self).__init__(fields,selinum_parger)
                    
    def process(self):
        print (self.fields['filed_name'])
        self.selinum_parger.clickOntheButton(self.fields['filed_name'])
          
class output_area(Command):
    def __init__(self,fields,selinum_parger):
        super(self.__class__, self).__init__(fields,selinum_parger)
                    
    def process(self):
        print (self.fields['area_name']+"<<")
        return self.selinum_parger.getResult(self.fields['area_name'])    

        


class SeleniumBroker:
    def __init__(self):
        self.myseleniumParger = SeleniumParger()
        
    
    def getSearchOutput(self,config):
        #print config
        url=config["url"]

        try:
            url=config["url"]
            self.myseleniumParger.setUrl(url)
        except:
            logger.getLogger(__name__).error('url NOT FOUND!')
            return ""

        try:
            self.__prepareSearchSetup(config["search_setup"],self.myseleniumParger)
        except:
            logger.getLogger(__name__).debug('search_setup NOT FOUND!')
            
        try:
            print (config["action"])
            self.__prepareAction(config["action"],self.myseleniumParger)
        except:
            logger.getLogger(__name__).debug('action NOT FOUND!')
            
        try:
            return self.__prepareOutput(config["search_output"],self.myseleniumParger)
        except:
            logger.getLogger(__name__).debug('search_output NOT FOUND!')
            return "" 
                               
               
    def __prepareSearchSetup(self,config,selinum_parger):        
        for fileds  in config:
            for filed  in fileds:
                if (filed=="textFiled"):
                    textFiled(fileds[filed],selinum_parger).process()                    
                    
    def __prepareAction(self,fileds,selinum_parger):
            search_button(fileds,selinum_parger).process()
                    
                                                    
    def __prepareOutput(self,fileds,selinum_parger):
        print (output_area(fileds,selinum_parger).process())    