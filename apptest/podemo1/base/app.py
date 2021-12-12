"""
__author__ = 'hogwarts_xixi'
"""
# 专门存放 app 相关的操作
import logging
import os

from appium import webdriver

from apptest.podemo1.base.base_page import BasePage
from apptest.podemo1.page.main_page import MainPage


# self.driver 是App的实例
class App(BasePage):

    def start(self):
        udid = os.getenv("udid")
        port = os.getenv("port")
        logging.info(f"传入参数 ===>>> udid:{udid}, port:{port}")
        if self.driver == None:
            logging.info(f"driver 为 {self.driver}")
            # 启动app
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
                "udid": udid,
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
            self.driver = webdriver.Remote(f"http://127.0.0.1:{port}/wd/hub", desire_caps)
            # 隐式等待，每一次查找元素的时候，动态的查找
            self.driver.implicitly_wait(5)

        else:
            logging.info(f"复用 driver. ")
            # 启动app 默认启动desire里的app
            self.driver.launch_app()
            # self.driver.start_activity()
        return self

    def stop(self):
        # 停止 app
        self.driver.quit()

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def goto_main(self):
        # 入口
        return MainPage(self.driver)
