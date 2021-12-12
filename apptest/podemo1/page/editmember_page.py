"""
__author__ = 'hogwarts_xixi'
"""

# 编辑成员页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from apptest.podemo1.base.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phonenum):
        # input name
        self.find_and_send(MobileBy.XPATH,
                           "//*[contains(@text,'姓名')]/../android.widget.EditText",
                           name)

        # input phonenum
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText",
                           phonenum)
        # click 保存
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        from apptest.podemo1.page.addmember_page import AddMemberPage
        return AddMemberPage(self.driver)
