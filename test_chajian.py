# @Time : 2020/12/13
# @Author : FPP
import pytest


class Test_demo():
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_demo(self):
        print("我的第一个测试用例1")

    def test_two(self):
        print("我的第二个测试用例2")

    def test_three(self):
        print("我的第三个测试用例3")
        pytest.assume(1 == 3)
        pytest.assume(4 == 5)
        pytest.assume(6 == 7)
        assert 1 == 2
        assert 2 == 3
        assert 3 == 4

    def test_four4(self):
        print("我的第二个测试用例4")

    def test_four5(self):
        print("我的第二个测试用例5")

    def test_four6(self):
        print("我的第二个测试用例6")

    @pytest.mark.run(order=2)
    def test_four7(self):
        print("我的第二个测试用例7")

    def test_four8(self):
        print("我的第二个测试用例8")

    @pytest.mark.run(order=-2)
    def test_four9(self):
        print("我的第二个测试用例9")

    def test_four10(self):
        print("我的第二个测试用例10")
