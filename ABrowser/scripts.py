from ABrowser import ABrowser
import time

chrome_driver = '/he/ABrowser/ABrowser/selen/drivers/chrome/93/chromedriver'


def ABrowser_console():
    ab = ABrowser(chrome_driver)
    time.sleep(10)
    print("DEMO TIME ENDED! BYE BYE")
