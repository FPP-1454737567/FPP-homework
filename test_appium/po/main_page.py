# @Time : 2020/12/27 
# @Author : FPP
from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.address_list_page import AddressListPage
from test_appium.po.base_page import BasePage


class MainPage(BasePage):
    """
    首页PO
    """

    def goto_address(self):
        # todo 点击通讯录按钮，return是为了链式调用
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)
