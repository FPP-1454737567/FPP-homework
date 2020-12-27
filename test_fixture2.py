# @Time : 2020/12/15 
# @Author : FPP

import pytest


class Test_firstFile2():

    def test_one2(self):
        print("执行test_one2")
        assert 2 + 3 == 5

    def test_two2(self, myfixture):
        print("执行test_two2")
        assert 1 == 1
        myenv = myfixture
        print("---------接收fixture返回测参数：%s" % myenv)

    def test_three2(self, connectdb):
        print("执行test_three2")
        assert 1 + 1 == 2
