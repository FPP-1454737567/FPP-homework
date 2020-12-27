# @Time : 2020/12/15 
# @Author : FPP
import pytest


@pytest.fixture(params=["*****参数1****", "****参数2****"])
def myfixture(request):
    print("执行myfixture，参数名称为%s" % request.param)
    yield request.param  # 相当于return
    print("激活fixture里面的teardown操作")


@pytest.fixture()
def connectdb():
    print("执行myfixture---connectdb")
