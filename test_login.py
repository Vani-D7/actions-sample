##### using parametrize

from Selenium_Wrapper import SeleniumWrapper
import pytest

header="email,password"  ### comma sepearted
data=[("Rajupatil@company.com","Passwor123"),("Seetharam@company.com","Password231")] ### list of tuples


@pytest.mark.parametrize(header,data)
def test_login(func,email,password): 
    sw=SeleniumWrapper(func)
    sw.click_element(("xpath","//a[text()='Log in']"))
    sw.enter_text(("id","Email"),value=email)
    sw.enter_text(("id","Password"),value=password)
    sw.click_element(("xpath","//input[@value='Log in']"))


 