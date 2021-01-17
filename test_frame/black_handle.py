# @Time : 2021/1/10 
# @Author : FPP
import logging

import allure

logging.basicConfig(level=logging.INFO)


def black_wrapper(fun):
    def wrapper(*args, **kwargs):
        basepage = args[0]
        try:
            logging.info(f"开始查找元素： args是 {args},kwargs是 {kwargs}")
            return fun(*args, **kwargs)
        except Exception as e:
            # 截图
            basepage.screenshot("tmp.png")
            # 截图传给allure:先从本地读取图片，再以二进制形式传给allure
            with open("./tmp.png", 'rb') as f:
                picture = f.read()
            allure.attach(picture, attachment_type=allure.attachment_type.PNG)
            # allure.attach("./tmp.png", attachment_type=allure.attachment_type.PNG)
            # 遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                ele = basepage.finds(*black)
                # 黑名单被找到，可能有多个元素finds
                if len(ele) > 0:
                    # 对黑名单的第一个元素进行点击
                    ele[0].click()
                    # 弹窗点掉后，再去查找正常元素，比如”行情“
                    return fun(*args, **kwargs)
            raise e

    # 注意返回的此函数不能带括号，闭包的固定用法
    return wrapper
