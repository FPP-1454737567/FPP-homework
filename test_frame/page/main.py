# @Time : 2021/1/8 
# @Author : FPP
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage
from test_frame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")
        # 加载yaml文件，注意路径必须是相对于执行路径来写，执行路径即测试用例文件的路径
        self.load('../page/main.yaml')
        return Market(self.driver)
