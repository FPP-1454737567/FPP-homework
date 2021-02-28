# @Time : 2021/1/31 
# @Author : FPP
import pytest
import requests


def get_access_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww88eabb74914f63c9&corpsecret=VGda4erlfUAj11iv6pmIIVEJrlUrKd8MCLDiUZRmkNw"
    response = requests.get(url, verify=False)
    return response.json()["access_token"]


def test_add_member():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_access_token()}"
    data = {
        "userid": "fpp20200131001",
        "name": "fpp",
        "mobile": "17711111111",
        "department": [2]
    }
    r = requests.post(url, json=data)
    print(r.json()['errcode'])
    assert 0 == r.json()['errcode']


@pytest.mark.parametrize("tmp", [1, 2])
def test_get_member(tmp):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_access_token()}&userid=FangPanPan"
    r = requests.get(url)
    print(r.json())
    assert "方盼盼" in r.json()["name"]


def test_update_member():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_access_token()}&userid=FangPanPan"
    data = {
        "userid": "FangPanPan",
        "name": "方盼盼fpp"
    }
    r = requests.post(url, json=data)
    print(r.json())


def test_delete_member():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_access_token()}&userid=fpp20200131001"
    # 在Python3.7及以上版本中基于requests模块使用代理，传给proxies的参数值必须加上http://或者https://，不加就会报错，proxies的参数值为{'http': 'http://ip:port'}键值对类型的字典
    # proxies = {"https": "https://127.0.0.1:8888"}
    r = requests.get(url, verify=False)
    print(r.json())
    # print(set(url))
