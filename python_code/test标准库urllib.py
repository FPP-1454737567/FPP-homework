# @Time : 2021/1/12 
# @Author : FPP
# python自带的标准库
import urllib.request
# 对上述的封装后的第三方库
import requests

response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)

import time

print(time.strftime("%Y %m %d"))
print(time.ctime())
