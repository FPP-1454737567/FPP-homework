# @Time : 2020/12/27 
# @Author : FPP
from appium import webdriver

from test_appium.po.base_page import BasePage
from test_appium.po.main_page import MainPage


class App(BasePage):
    def start(self):
        """
        做一个判断:没有driver就初始化,有driver就直接启动launch_app
        """
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        # 隐式等待
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)
