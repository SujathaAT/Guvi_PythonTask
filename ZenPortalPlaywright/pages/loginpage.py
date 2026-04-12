from playwright.sync_api import expect

from pages.basepage import basepage


class LoginPage(basepage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username = "Email"
        self.password = "Password"
        self.button = "Sign in"
        #self.launchalertclose = "//button[@class = 'custom-close-button']"

    def navigate(self):
        if "/login" not in self.page.url:
            self.page.goto("https://www.zenclass.in/login")

    def enter_credentials(self, username, pwd):
        self.navigate()
        self.page.get_by_role("textbox", name = self.username).wait_for(state="visible")
        self.page.get_by_role("textbox", name = self.username).fill(username)
        self.page.get_by_role("textbox", name = self.password).fill(pwd)

    def clicksignin(self):
        self.page.get_by_role("button", name = self.button, exact=False).click(force=True)



    # def closelaunchalert(self):
    #     try:
    #         self.page.get_by_role(self.launchalertclose).click()
    #     except:
    #         print("[!] Launch alert not available")



    def validate_zenportalsubmit(self):
        # self.navigate()
        submit_btn = self.page.get_by_role("button", name="Sign In")
        expect(submit_btn).to_be_visible()

        # self.checkButton(self.button, "Submit ")

    def verify_unsuccessfullogin(self,invalidemail, invalidpwd):
        self.page.goto("https://zenclass.in")
        self.enter_credentials(invalidemail, invalidpwd)
        self.clicksignin()
        self.checkPageurlnavigation("https://www.zenclass.in/login", "login")

        
        

    def validate_zenportalfields(self):
        # self.navigate()
        self.page.goto("https://zenclass.in")
        basepage.checkTextFields(self,"Email", "Email")
        basepage.checkTextFields(self, "Password", "Password")
        # username_text = page.get_by_label("Email")
        # expect(username_text).to_be_editable()
        # pwd_text = page.get_by_label("Password")
        # expect(pwd_text).to_be_editable()

        # self.checkTextFields(self.username, "Username")
        # self.checkTextFields(self.password, "Password")

    def user_logout(self):
        close_button = self.page.get_by_role("button", name="Close popup")
        # if close_button.is_visible():
        if close_button.is_visible():
            close_button.click()
        # page.get_by_role("button", name="Close popup").click())
        self.page.locator(".profile-click-icon-div").click()
        self.page.get_by_text("Log out").click()
        expect(self.page).to_have_url("https://www.zenclass.in/login")

    def handle_launch_alert(self):
        close_btn = self.page.get_by_role("button", name="Close popup").or_(
            self.page.locator("button.custom-close-button"))

        try:

            if close_btn.is_visible(timeout=5000):
                close_btn.click()
                print("Launch alert closed successfully.")
        except:
            print("No launch alert appeared.")
        profile_icon = self.page.locator(".profile-click-icon-div")
        profile_icon.dispatch_event("click")