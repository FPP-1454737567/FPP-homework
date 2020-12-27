# @Time : 2020/12/13 
# @Author : FPP
import pytest


class Test_demo():
    @pytest.mark.demo
    def test_demo(self):
        print("我的第一个测试用例")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_two(self):
        print("我的第二个测试用例")

    def test_three(self):
        print("我的第三个测试用例")
