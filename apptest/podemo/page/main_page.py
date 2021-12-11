"""
__author__ = 'hogwarts_xixi'
"""
# 首页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from apptest.podemo.base.base_page import BasePage
from apptest.podemo.page.addresslist_page import AddressListPage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # click [通讯录]
        self.find_and_click(*self.addresslist_element)
        return AddressListPage(self.driver)
