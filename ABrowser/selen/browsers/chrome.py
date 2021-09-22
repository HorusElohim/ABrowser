from . import ABCBrowser
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Chrome(ABCBrowser):
    def _init_driver_(self, driver_path: Path, driver_option: dict):
        chrome_options = webdriver.ChromeOptions()
        for arg, value in driver_option.items():
            chrome_options.add_argument(f'{arg}={value}')
        self.driver = webdriver.Chrome(driver_path, options=chrome_options)
        self.waiter = WebDriverWait(self.driver, timeout=30)
