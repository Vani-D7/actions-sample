from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class _visibility_of_element_located(visibility_of_element_located):

    def __init__(self,locator):
        self.locator=locator

    def __call__(self,driver):  # redefining the parent class __call___ # for adding one funtionality webelement is enabled?
        result=super().__call__(driver)  # parent __call__ its check loaded on dom ,visible on webpage ,it wont check for enable
        if isinstance(result,WebElement):  # __call___ ::::: returns Webelement if true ,,,return False if WE is not loaded on DOM ,not visible on webpage
            return result.is_enabled()   ### if element not findng after timeout the Timeoutexception
        else:
            return False
    

def _wait(func):
    def wrapper(*args,**kwargs):   # args:(self,("id","FirstName"))    Kwargs:{"value":"hello"}
        instance=args[0]    #self
        locator=args[1]      #("id","FirstName")


        w = WebDriverWait(instance.driver,20)
        v=_visibility_of_element_located(locator)

        w.until(v)
        
        return func(*args,**kwargs)
    return wrapper