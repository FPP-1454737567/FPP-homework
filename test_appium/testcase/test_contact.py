# @Time : 2020/12/27 
# @Author : FPP
from test_appium.po.app import App


def test_add_member():
    app = App()
    app.start()
    app.goto_main().goto_address().add_member().add_member_manual().add_contact()
