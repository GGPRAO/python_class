from robot.api.deco import keyword
import pandas

@keyword("Wait Until I Close Browser")
def wait_until_i_close_browser():
    input("Close the browser manually, then press ENTER here...")

