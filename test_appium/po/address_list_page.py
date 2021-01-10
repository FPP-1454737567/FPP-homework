# @Time : 2020/12/27 
# @Author : FPP
from test_appium.po.base_page import BasePage
from test_appium.po.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录 PO
    """

    def add_member(self):
        """
        添加成员信息
        :return:
        """
        # todo 点击添加成员信息
        self.scroll_find_click("添加成员")
        return MemberInviteMenuPage(self.driver)
