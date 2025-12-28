from pages.loginpage import LoginPage
from pages.logoutpage import LogoutPage



def test_usercouldlogin(driver, get_yamldata):

    email = get_yamldata['email']
    pwd = get_yamldata['password']

    login_page = LoginPage(driver)
    login_page.validate_zenportalfields()
    login_page.validate_zenportalsubmit()
    login_page.enter_credentials(email, pwd)
    login_page.signin()
    login_page.closelaunchalert()
    login_page.checkPagetitle("GUVI", "Login is successful")

def test_validatePortalFields(driver):
    login_page = LoginPage(driver)
    login_page.validate_zenportalfields()

def test_validateZenPortalSubmit(driver):
    login_page = LoginPage(driver)
    login_page.validate_zenportalsubmit()

def test_validateunsuccessfullogin(driver):
    EMAIL = "Invalidemail@guvi,com"
    PWD = "ERRONEOUSPWD@1234"

    login_page = LoginPage(driver)
    login_page.enter_credentials(EMAIL, PWD)
    login_page.signin()
    login_page.verify_unsuccessfullogin()

def test_validateunsuccessfullogin_withblankcreds(driver):
    login_page = LoginPage(driver)
    login_page.enter_credentials("", "")
    login_page.signin()
    login_page.verify_unsuccessfullogin()


def test_usercouldlogout(driver, get_yamldata):
    login_page = LoginPage(driver)
    email = get_yamldata['email']
    pwd = get_yamldata['password']

    login_page.enter_credentials(email, pwd)
    login_page.signin()
    login_page.closelaunchalert()
    logout_page = LogoutPage(driver)
    logout_page.logout()
    logout_page.checkLogout_functionality()