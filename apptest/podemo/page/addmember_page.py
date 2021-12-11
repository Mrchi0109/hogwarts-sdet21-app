"""
__author__ = 'hogwarts_xixi'
"""
# 添加成员页
from appium.webdriver.common.mobileby import MobileBy

from apptest.podemo.base.base_page import BasePage


class AddMemberPage(BasePage):
    def addmember_menual(self):
        # click [手动输入添加]
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from apptest.podemo.page.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def get_result(self):
        # 获取结果
        result = self.getattr(MobileBy.XPATH,
                              "//*[@class='android.widget.Toast']",
                              "text")
        return result
