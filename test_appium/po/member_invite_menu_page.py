# @Time : 2020/12/27 
# @Author : FPP
from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.base_page import BasePage
from test_appium.po.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    """
    添加成员页 PO
    """

    def add_member_manual(self):
        """
        点击手动添加成员
        :return:
        """
        # todo 点击手动添加成员菜单
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAddPage(self.driver)
