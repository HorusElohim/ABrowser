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
import abc


@dataclass
class XPath:
    pass


class ABCBrowser(abc.ABC):
    driver: webdriver = None
    waiter: WebDriverWait = None

    def __init__(self, driver_path: Path, driver_option):
        self._init_driver_(driver_path, driver_option)

    @abc.abstractmethod
    def _init_driver_(self, driver_path: Path, driver_options: dict):
        pass

    def is_ready(self):
        return self.driver is not None and self.waiter is not None

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

    def close(self):
        self.driver.quit()
