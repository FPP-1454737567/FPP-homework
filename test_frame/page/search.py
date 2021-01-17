# @Time : 2021/1/8 
# @Author : FPP
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        # self.find_and_send(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "顺丰")
        self.load('../page/search.yaml')
        return True
