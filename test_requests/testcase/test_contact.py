# @Time : 2021/1/31 
# @Author : FPP
import requests

from test_requests.req_page.contact_page import Contact


class TestContact:
    def setup(self):
        self.contact = Contact()
        self.userid = "fpp20210131003"
        self.name = "fpp名字"

    def test_create_member(self):
        result = self.contact.create_member(userid=self.userid, name=self.name, mobile='17712341113', department=[1],
                                            position="测试经理")
        # 方法一：自己一步步写的断言
        # assert "created" == result["errmsg"]
        # s = self.contact.get_member(userid=self.userid)
        # print(s)
        # assert s["name"] == "fpp名字"
        # #清洗数据
        # r = self.contact.delete_member(userid=self.userid)
        # 方法二
        try:
            result = self.contact.get_member(userid=self.userid)
        finally:
            # 测试的数据一定要清理掉
            self.contact.delete_member(userid=self.userid)
        assert result["name"] == "fpp名字"

    def test_token(self):
        token = self.contact.get_token()
        assert token["errcode"] == 0

    def test_find_member(self):
        r = self.contact.get_member("FangPanPan")
        assert r["name"] == "方盼盼fpp"

    def test_delete_member(self):
        # 在增加成员里清洗数据时已经做了删除了
        pass

    def test_update_member(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="17712341113", department=[1])
        self.contact.update_member(userid=self.userid, name=self.name, mobile="17712341114", department=[2],
                                   address="地址")
        try:
            result = self.contact.get_member(userid=self.userid)
        finally:
            self.contact.delete_member(userid=self.userid)
        print(result)
        assert result["mobile"] == "17712341114"
