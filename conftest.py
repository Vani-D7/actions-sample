from time import sleep
from selenium.webdriver import Chrome
from pytest import fixture



@fixture
def func():
    driver=Chrome(r"C:\Users\DELL\Desktop\Training\_Selenium\training\_Selenium_practice\chromedriver.exe")
    driver.get(r"https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    

    sleep(5)

    yield driver
    
    driver.quit()
