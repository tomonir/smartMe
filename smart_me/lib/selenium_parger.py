from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lib.logger import Logger
logger = Logger()



class SeleniumParger:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

        self.textFileds    =[]
        self.actionFileds  =[]
        self.resultFileds  =[]

        self.output = []
        #pass
    def __del__(self):
        self.driver.close()

    def setUrl(self,url):
        self.url    = url
        self.driver.get(self.url)

    def setTextFiled(self,_xpath,txt):
        self.textFileds.append((_xpath,txt))

    def setActionFiled(self,type,_xpath):
        self.actionFileds.append((_xpath,type))

    def setResultFiled(self,_xpath):
        self.resultFileds.append(_xpath)        

    def submitTheForm(self):

        #fill the text fileds
        for txtfield in self.textFileds:
            try:
                print (txtfield[0])
                print (txtfield[1])
                element = self.driver.find_element_by_xpath(txtfield[0])
                element.clear()
                element.send_keys(txtfield[1])
            except NoSuchElementException:
                logger.getLogger(__name__).debug( txtfield[0] + ' Not found !')    
            except:
                logger.getLogger(__name__).debug('fill the text fileds Failed!')    


        #prepare action
        for actionFiled in self.actionFileds:
            try:
                print(actionFiled[0])
                print(actionFiled[1])
                element = self.driver.find_element_by_xpath(actionFiled[0])

                if actionFiled[1]=="enterOnTextFiled":
                    element.send_keys(Keys.RETURN)
                elif actionFiled[1]=="clickOntheButton":
                    element.click()
            except NoSuchElementException:
                logger.getLogger(__name__).debug( actionFiled[0] + ' Not found !')    
            except:
                logger.getLogger(__name__).debug('prepare action Failed!')


         #colect resultFileds
        for resultFiled in self.resultFileds:
            try:
                print(resultFiled)
                element = self.driver.find_element_by_xpath(resultFiled)
                self.output = element.text
                print (element.text)
            except NoSuchElementException:
                logger.getLogger(__name__).debug( resultFiled + ' Not found !')    
            except:
                logger.getLogger(__name__).debug('colect resultFileds Failed!')


    def getOutput(self):
        return  self.output





    