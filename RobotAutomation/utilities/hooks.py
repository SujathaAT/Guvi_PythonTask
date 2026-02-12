from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

selib = BuiltIn().get_library_instance("SeleniumLibrary")

@keyword("Start Browser")
def start_browser():
    selib.open_browser("https://robotsparebinindustries.com/", "chrome")
    selib.maximize_browser_window()


@keyword("Stop Browser")
def stop_browser():
    selib.close_all_browsers()
