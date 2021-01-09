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
        
class action(Command):
    def __init__(self,fields,selinum_parger):
        super(self.__class__, self).__init__(fields,selinum_parger)
                    
    def process(self):
        print (self.fields['action_type'])
        print (self.fields['filed_name'])
        self.selinum_parger.setActionFiled(self.fields['action_type'],self.fields['filed_name'])
          
          
class output_area(Command):
    def __init__(self,fields,selinum_parger):
        super(self.__class__, self).__init__(fields,selinum_parger)
                    
    def process(self):
        print (self.fields['area_name'])
        self.selinum_parger.setResultFiled(self.fields['area_name'])   

        


class SeleniumBroker:
    def __init__(self):
        self.myseleniumParger = SeleniumParger()
         
    def __del__(self):
        del self.myseleniumParger

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
            #print (config["action"])
            self.__prepareAction(config["action"],self.myseleniumParger)
        except:
            logger.getLogger(__name__).debug('action NOT FOUND!')
            
        try:
            self.__prepareOutput(config["search_output"],self.myseleniumParger)
        except:
            logger.getLogger(__name__).debug('search_output NOT FOUND!')
            return ""

        try:
            print ("caling submission########################")
            self.myseleniumParger.submitTheForm()
            print (self.myseleniumParger.getOutput())
        except:
            logger.getLogger(__name__).debug('SUBMISSION FAILED!')

                               
               
    def __prepareSearchSetup(self,config,selinum_parger):        
        for fileds  in config:
            for filed  in fileds:
                if (filed=="textFiled"):
                    textFiled(fileds[filed],selinum_parger).process()                    
                    
    def __prepareAction(self,fileds,selinum_parger):
        action(fileds,selinum_parger).process()
                    
                                                    
    def __prepareOutput(self,fileds,selinum_parger):
        output_area(fileds,selinum_parger).process()    