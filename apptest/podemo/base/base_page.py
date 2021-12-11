"""
__author__ = 'hogwarts_xixi'
"""
# 基类，封闭基本的方法，通常封装基础框架级别的
# driver, find, find_and_click, find_and_send, swipe_find.....
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        # 查找元素,一定要加return
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        # 找到元素并点击
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        # 找到元素并输入
        self.find(by, locator).send_keys(text)

    def getattr(self, by, locator, attribute="text"):
        return self.find(by, locator).get_attribute(attribute)
