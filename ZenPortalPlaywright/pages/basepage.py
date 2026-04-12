import pytest
from playwright.sync_api import expect


class basepage:
    def __init__(self, page):
        self.page = page

    def checkPagetitle(self, title, message):
        actualtitle = self.page.title()
        assert actualtitle == title, message
    
    def checkPageurlnavigation(self, url,message):
        # actualurl = self.page.url
        expect(self.page).to_have_url(url, timeout=10000)

        print(f"User stays in page : {message}")

    def checkTextFields(self, locator, field):

        # try:
        #
        #     expect(self.page.get_by_role("textbox", name =locator)).to_be_editable()
        #     print(field + "is available")
        # except:
        #     pytest.fail("Unable to find " + field)


        try:
            el = self.page.get_by_role("textbox", name=locator)
            expect(el).to_be_visible(timeout=5000)
            expect(el).to_be_editable()
            print(f"{field} is available")
        except Exception as e:
            pytest.fail(f"Unable to find {field}: {str(e)}")

    def checkButton(self, locator, field):
        try:
            self.page.get_by_role("button", name = locator).is_displayed()

            print("Button is displayed" + field)
        except:
            pytest.fail(field + "is not displayed")