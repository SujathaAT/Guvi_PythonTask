from selenium.common import InvalidSessionIdException
from selenium.webdriver.common.by import By

from tests.Commonpage import Commonutils


class HomePage(Commonutils):
    POPCOUNT = "//div[@class ='counter-ticker is-size-2-mobile']"
    POPULATION = (By.XPATH, POPCOUNT)
    presence_flag = False

    def check_popcount(self, driver):
        presence_flag = Commonutils.checkElement_availability(self,self.POPULATION,"Population count")

        while (presence_flag == True):

            try:
                curr_pop = (driver.find_element(By.XPATH, self.POPCOUNT)).text
                print(f"World Population Count :{curr_pop}")
                presence_flag = Commonutils.checkElement_availability(self,self.POPULATION,"Population count")

            except KeyboardInterrupt:
                    print("\n Interrupted by user")

            # except (urllib3.exceptions.MaxRetryError, WebDriverException):
            #     print("\n The Connection has been lost.Browser session ended.")
            except InvalidSessionIdException:
                print("\n Connection lost. Retrying ")
                time.sleep(2)
            except ConnectionRefusedError:
                print("\n Server connection refusal. Please give a higher delay")
            except Exception as e:
                print("Error Occurred:" + e)
            # finally:
            #     driver.close()
            #     driver.quit()
