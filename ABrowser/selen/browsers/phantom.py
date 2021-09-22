from . import ABCBrowser
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Phantom(ABCBrowser):
    def _init_driver_(self, driver_path: Path, driver_option: dict):
        self.driver = webdriver.PhantomJS(driver_path)
        self.waiter = WebDriverWait(self.driver, timeout=30)
