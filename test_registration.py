##### using paraametrize
from pytest
from Selenium_Wrapper import SeleniumWrapper



headers="gender,fname,lname,email,password,confirmpass"

data=[("male","Steve","harvel","steveharvel@company.com","password123","password123"),("female","Marry","jim","Marryjim@company.com","password456","password456")]


@pytest.mark.parametrize(headers,data)
def test_registration(func,gender,fname,lname,email,password,confirmpass):
    obsw=SeleniumWrapper(func)

    obsw.click_element(("link text","Register"))
    if gender=="female":
        obsw.click_element(("id","gender-female"))

    else:
        obsw.click_element(("id","gender-male"))

    obsw.enter_text(("id","FirstName"),value=fname)
    obsw.enter_text(("id","LastName"),value=lname)
    obsw.enter_text(("id","Email"),value=email)
    obsw.enter_text(("id","Password"),value=password)
    obsw.enter_text(("id","ConfirmPassword"),value=confirmpass)
    obsw.click_element(("id","register-button"))