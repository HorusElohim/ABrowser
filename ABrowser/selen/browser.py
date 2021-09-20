# -*- coding: utf-8 -*-
# @author: MarkNo1 aka HorusElohim
# @desc:
#        Simple Selenium Wrapper to accelerate usage

from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from dataclasses import dataclass


@dataclass
class XPath:
    pass


class ABrowser:
    driver: webdriver.Chrome
    waiter: WebDriverWait

    def __init__(self, driver_path: Path, incognito=False):
        user_agent = "Android KitKat", "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-agent={}'.format(user_agent))
        if incognito:
            chrome_options.add_argument('--incognito')
        self.driver = webdriver.Chrome(driver_path, options=chrome_options)
        self.waiter = WebDriverWait(self.driver, timeout=30)

    # Get when available
    def get_xpath(self, xpath) -> WebElement:
        return self.waiter.until(ec.visibility_of_element_located((By.XPATH, xpath)))

    def open_url(self, url):
        self.driver.get(url)

    def execute(self, cmd):
        return self.driver.execute_script(cmd)

    def get_user_agent(self):
        return self.execute("return navigator.userAgent")

    def clear(self):
        self.driver.get("about:blank")
        self.driver.delete_all_cookies()
        self.driver.execute_script('localStorage.clear();')
