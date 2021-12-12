"""
__author__ = 'hogwarts_xixi'
"""
from faker import Faker


# mock一些测试数据
class GenerateInfo:

    @classmethod
    def get_name(cls):
        # 生成姓名
        return Faker("zh_CN").name()

    @classmethod
    def get_phonenum(cls):
        # 生成电话号
        return Faker("zh_CN").phone_number()
