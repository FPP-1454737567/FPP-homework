# @Time : 2021/1/6 
# @Author : FPP
import pytest


def test_answer():
    assert 5 == 5
    print("OK")


# 用python解释器来运行
if __name__ == '__main__':
    test_answer()
# 用python解释器来运行
# if __name__ == '__main__':
#     pytest.main(['test_pytest解释器demo.py'])
