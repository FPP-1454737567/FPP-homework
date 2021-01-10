# @Time : 2021/1/8 
# @Author : FPP
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage
from test_frame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")
        # //*[@resource-id='android:id/tabs']
        return Market(self.driver)
