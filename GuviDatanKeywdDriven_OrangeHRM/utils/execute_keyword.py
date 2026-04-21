from keywords.commonkeywords import CommonKeywords


class KeywordExecutor:
    def __init__(self):
        self.keywords = CommonKeywords()

    def execute(self, step, creds):
        keyword = step["Keyword"]
        locator = str(step["locator"])
        value = step["value"]

        print(f"Executing Keyword: {keyword}")

        if keyword == "open_browser":
            self.keywords.open_browser()

        elif keyword == "launch_url":
            self.keywords.launch_url(value)

        elif keyword == "enter_text":

            if "@U" in locator or value == "U":
                data_to_send = creds["Username"]
            elif "@P" in locator or value == "P":
                data_to_send = creds["Password"]
            else:
                data_to_send = value

            self.keywords.enter_text(locator, data_to_send)

        elif keyword == "click":
            self.keywords.click(locator)

        elif keyword == "verify_page":
            return self.keywords.verify_page(value)

        elif keyword == "close_browser":
            self.keywords.close_browser()

        else:
            raise Exception(f"Invalid Keyword: {keyword}")
