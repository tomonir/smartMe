from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lib.logger import Logger
logger = Logger()



class SeleniumParger:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        #pass
    def __del__(self):
        self.driver.close()
        
    def setUrl(self,url):
        self.url    = url
        self.driver.get(self.url)

    def setTextFiled(self,txt,_xpath):
        try:
            element = self.driver.find_element_by_xpath(_xpath)
            element.clear()
            element.send_keys(txt)
        except NoSuchElementException:
            logger.getLogger(__name__).debug( _xpath + ' Not found !')
            return    
        except:
            logger.getLogger(__name__).debug('setTextFiled Failed!')
            return

        
   
    def clickOntheButton(self,_xpath):
        try:
            element = self.driver.find_element_by_xpath(_xpath)
            element.click()
        except NoSuchElementException:
            logger.getLogger(__name__).debug('Button Not found !')
            return
        except:
            logger.getLogger(__name__).debug('clickOntheButton Failed !')
            return

    def getResult(self,_xpath):
        try:
            element = self.driver.find_element_by_xpath(_xpath)
            return (element.text)
        except NoSuchElementException:
            logger.getLogger(__name__).debug('Button Not found !')
            return ""
        except:
            logger.getLogger(__name__).debug('clickOntheButton Failed !')
            return ""




    