"""
__author__ = 'hogwarts_xixi'
"""
import logging
import os

from faker import Faker

from apptest.podemo1.base.app import App
from apptest.podemo1.utils.generate_info import GenerateInfo


class TestContact:

    def setup_class(self):
        # 启动app
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        # 关闭app
        self.app.stop()

    def test_addcontact(self):
        name = GenerateInfo.get_name()
        phonenum = GenerateInfo.get_phonenum()
        logging.info(f"添加联系人姓名：{name},添加电话号码{phonenum}")

        result = self.main.goto_addresslist().click_addmember(). \
            addmember_menual().edit_member(name, phonenum).get_result()

        assert "添加成功" == result

    def test_addcontact1(self):
        name = GenerateInfo.get_name()
        phonenum = GenerateInfo.get_phonenum()
        logging.info(f"添加联系人姓名：{name},添加电话号码{phonenum}")

        result = self.main.goto_addresslist().click_addmember(). \
            addmember_menual().edit_member(name, phonenum).get_result()

        assert "添加成功" == result
