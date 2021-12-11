"""
__author__ = 'hogwarts_xixi'
"""
# appium-python-client
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.common.exceptions import NoSuchElementException

"""
前提条件：

1、提前注册企业微信管理员帐号
2、手机端安装企业微信
3、企业微信 app 处于登录状态
通讯录添加成员用例步骤
"""


class TestContact:
    def setup_class(self):
        # pip install Faker
        self.fake = Faker("zh_CN")
        # 初始化操作：打开应用
        desire_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            # 重要的：通过命令获取package/activity :
            # adb logcat ActivityManager:I | grep "cmp"
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            # 跳过设备初始化 ,跳过settings.apk的安装与设置
            "skipDeviceInitialization": True,
            # 跳过uiautomato2 服务安装
            "skipServerInstallation": True,
            # 在运行测试之前，不停止 app ，或者说不重新启动app，
            # 之前在哪个页面上，就在那个页面上继续执行
            # "dontStopAppOnReset": True,
            # 防止 清缓存数据
            "noReset": "True",
            # 等待页面处于idle状态 ，默认10s
            "settings[waitForIdleTimeout]": 0
        }
        # 客户端与服务端建立连接的关键语句
        # 启动app
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # 隐式等待，每一次查找元素的时候，动态的查找
        self.driver.implicitly_wait(5)

    def back(self, num=3):
        for i in range(num):
            self.driver.back()

    def teardown(self):
        self.back()

    def teardown_class(self):
        # 关闭应用
        self.driver.quit()

    def test_addcontact(self):
        # mock name 和phonenum数据
        name = self.fake.name()
        phonenum = self.fake.phone_number()
        # 打开【企业微信】应用
        # 进入【通讯录】页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        # 输入【姓名】【手机号】并点击【保存】第一次出现的元素
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys("hogwarts001")
        # 方法一：通过 xpath 父子关系查找元素
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText"). \
            send_keys(name)
        # 方法二：通过 xpath 父子关系查找元素
        # //*[contains(@text,'姓名')]/../*[@text='必填']
        # 方法三：通过兄弟关系查找元素 following-sibling::
        # //*[contains(@text,'姓名')]/following-sibling::android.widget.EditText
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//android.widget.EditText"). \
            send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 验证点：登录成功提示信息
        # while True:
        #     if "添加成功" in self.driver.page_source:
        #         print(self.driver.page_source)
        #         break

        # assert "添加成功" in self.driver.page_source
        result = self.driver.find_element(MobileBy.XPATH,
                                          "//*[@class='android.widget.Toast']").get_attribute("text")
        # 断言
        assert "添加成功" == result

    def swipe_find(self, text, num=3):
        # 循环三次查找
        for i in range(num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                return ele
            except:
                # 滑动操作
                # 获取屏幕的尺寸 'width', 'height'
                size = self.driver.get_window_size()
                # 屏幕宽
                width = size.get("width")
                # 屏幕高
                height = size.get("height")
                # 起点x
                start_x = width / 2
                # 起点y  屏幕的y*0.8
                start_y = height * 0.8
                # 终点x
                end_x = start_x
                # 终点y
                end_y = height * 0.2
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                raise NoSuchElementException(f"找了{num}次，未找到")

    def test_daka(self):
        # 实现打卡功能
        # 打开【企业微信】应用
        # 进入【工作台】页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 点击【打卡】
        self.swipe_find("打卡").click()
        # 先由向至下滑动两次，然后再向上滑动查找想要的元素，
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, \
        #                          'new UiScrollable(new UiSelector().scrollable(true).instance(0))\
        #                          .scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        # 选择【外出打卡】tab
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 点击【第N次打卡】
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # 验证点：提示【外出打卡成功】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def test_delete_contact(self):
        name = "倪"
        # 打开【企业微信】应用
        # 进入【通讯录】页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击右上角搜索图标，进入搜索页面
        # following-sibling:: 获取当前节点的后面的兄弟结点
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='测试公司']/../../../following-sibling::android.widget.LinearLayout/*[1]").click()
        # 输入搜索内容（已添加的联系人姓名）
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(name)
        sleep(2)
        # 有两种情况
        # 第一种情况：提示:  无搜索结果
        if "无搜索结果" in self.driver.page_source:
            pytest.xfail(f"无搜索结果：{name}")

        # 第二种情况：有搜索结果
        # 判断联系人的个数
        # find_elements 会返回一个元素列表[element1,element2,....]列表里是 WebElement类型的元素
        elements = self.driver.find_elements(MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::*")
        num = len(elements)
        print(f"删除前搜索出来的联系人个数：{num}")

        # 点击展示的第一个联系人（有可能多个），进入联系人详情页面
        # 1,3,5 奇数对应的是名字，偶数对应的是公司
        element = \
        self.driver.find_elements(MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::*//android.widget.TextView")[
            0]
        element.click()
        # 点击右上角三个点，进入个人信息页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]").click()
        # 点击【编辑成员】进入编辑成员页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 点击【删除成员】并确定
        self.swipe_find("删除成员").click()
        self.swipe_find("确定").click()
        sleep(2)
        # 验证点：搜索结果页面联系人个数少一个
        elements_after = self.driver.find_elements(MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::*")

        # 找到的元素个数，result 代表删除之后的个数
        result = len(elements_after)
        assert result == num - 1
