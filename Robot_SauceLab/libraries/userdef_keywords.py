from typing import cast

import SeleniumLibrary.keywords
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from SeleniumLibrary import SeleniumLibrary



@keyword("Verify page Url")
def verify_page_url(expected_url):
    selib = cast(SeleniumLibrary, BuiltIn().get_library_instance("SeleniumLibrary"))
    selib.wait_until_location_is(expected_url)
    selib.location_should_be(expected_url)
