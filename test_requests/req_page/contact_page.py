# @Time : 2021/1/31 
# @Author : FPP

from test_requests.req_page.base import Base


class Contact(Base):
    def create_member(self, userid: str, name: str, mobile: str, department: list[int], **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        # 字典的修改值和追加值用法
        data.update(kwargs)
        r = self.s.post(url, json=data)
        return r.json()

    def get_member(self, userid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {"userid": userid}
        r = self.s.get(url, params=params, verify=False)
        return r.json()

    def delete_member(self, userid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {"userid": userid}
        r = self.s.get(url, params=params)
        return r.json()

    def update_member(self, userid: str, name: str, mobile: str, department: list[int], **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        params = {"userid": userid}
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        r = self.s.post(url=url, params=params, json=data)
        return r
