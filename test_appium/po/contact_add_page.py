# @Time : 2020/12/27 
# @Author : FPP
from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.base_page import BasePage


class ContactAddPage(BasePage):
    """
    成员信息编辑
    """

    def add_contact(self):
        """
        添加信息,注意姓名后有空格的定位
        :return:
        """
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']", "fpp1")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_send(MobileBy.XPATH, "//*[@text='手机号']", "17711111110")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return True
