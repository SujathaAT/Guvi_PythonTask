import re

from playwright.sync_api import expect

from pages.loginpage import LoginPage


def test_usercouldlogin(zen_page, get_yamldata):

    email = get_yamldata['email']
    pwd = get_yamldata['password']

    login_page = LoginPage(zen_page)

    login_page.validate_zenportalfields()
    login_page.validate_zenportalsubmit()
    login_page.enter_credentials(email, pwd)
    login_page.clicksignin()
    # login_page.closelaunchalert()
    login_page.checkPagetitle("GUVI", "Login is successful")

def test_invalidlogin(zen_page, get_yamldata):
    email = get_yamldata['invalidemail']
    pwd = get_yamldata['invalidpwd']

    login_page = LoginPage(zen_page)
    
    login_page.verify_unsuccessfullogin(email,pwd)
    #  enter_credentials(email, pwd))
    # login_page.clicksignin()
    
def test_logout(zen_page, get_yamldata):

    email = get_yamldata['email']
    pwd = get_yamldata['password']

    login_page = LoginPage(zen_page)

    login_page.validate_zenportalfields()
    login_page.validate_zenportalsubmit()
    login_page.enter_credentials(email, pwd)
    login_page.clicksignin()
    login_page.handle_launch_alert()

    # test_usercouldlogin(page, get_yamldata)
    # assert "dashboard" not in zen_page.url
    login_page.user_logout()

    # expect(zen_page).to_have_url("https://zenclass.in")
    expect(zen_page).to_have_url(re.compile(".*login"))
    zen_page.screenshot(path="reports/logout.png", full_page=True)