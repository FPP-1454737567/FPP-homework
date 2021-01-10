# @Time : 2021/1/10 
# @Author : FPP
def black_wrapper(fun):
    def wrapper(*args, **kwargs):
        basepage = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception as e:
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
