#generic funtion
from _wait import _wait

class SeleniumWrapper:

    def __init__(self,driver):
        self.driver=driver

    @_wait  # enter_text=_wai-t(enter_text)
    def enter_text(self,locator,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @_wait  #click_element=_wait(click_element)
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
