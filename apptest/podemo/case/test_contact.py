"""
__author__ = 'hogwarts_xixi'
"""
from faker import Faker

from apptest.podemo.base.app import App


class TestContact:

    def setup(self):
        self.fake = Faker("zh_CN")
        # 启动app
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        # 关闭app
        self.app.stop()

    def test_addcontact(self):
        name = self.fake.name()
        phonenum = self.fake.phone_number()

        result = self.main.goto_addresslist().click_addmember(). \
            addmember_menual().edit_member(name, phonenum).get_result()

        assert "添加成功" == result
