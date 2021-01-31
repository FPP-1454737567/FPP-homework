# @Time : 2021/1/31 
# @Author : FPP
import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = Session()
        self.orpid = "ww88eabb74914f63c9"
        self.corpsecret = "VGda4erlfUAj11iv6pmIIVEJrlUrKd8MCLDiUZRmkNw"
        self.s.params["access_token"] = self.get_token()["access_token"]

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.orpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        response = requests.get(url, params=params)
        print(response.json())
        return response.json()


if __name__ == '__main__':
    a = Base().get_token(None, None)
