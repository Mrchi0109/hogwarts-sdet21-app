"""
__author__ = 'hogwarts_xixi'
"""
# 通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from apptest.podemo.base.base_page import BasePage
from apptest.podemo.page.addmember_page import AddMemberPage


class AddressListPage(BasePage):
    def click_addmember(self):
        # click [添加成员]
        self.find_and_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return AddMemberPage(self.driver)
