# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 上午9:51

"""
pytest简介


pytest的默认读取规则
    默认读取 test开头或者test结尾 的文件夹和文件，如果不是test开头命名的文件夹、文件、函数，pytest是识别不了的
    运行程序的时候，会找到当前路径下所有test开头或者结尾的文件夹、文件、函数
    默认不输出任何打印信息，如果要看打印信息，需要在运行时加上 -s 的指令：python3 -m pytest -s
    可以批量化运行（按照顺序执行，而不是按照文件命名执行）
    指定文件或者指定用例执行，可以通过两个冒号 :: 实现，例如
        python3 -m pytest -s test_pytest.py::test_01   # 指定执行某个用例：文件名称::用例名称
        python3 -m pytest -s test_pytest.py  # 指定执行某个文件
    多条指令同时运行时，是通过空格进行区分，在main()函数中是通过list里面的逗号 , 区分的
    -v 详细记录运行结果，会把所有执行过的用例通过与失败都记录，用PASSED和FALSE记录
    -rA 简单统计的运行结果（结果 用例），比较清晰明了

pytest的配置文件
    pytest有8个 setup和teardown，通过配置文件来实现，配置文件命名一定是：conftest.py
    类外定义的setup、teardown对内里面的函数是没有作用的，如果类里面需要setup、teardown，那么就在类里面定义setup、teardown

"""


import pytest

# 前置与后置条件
def setup_function():
    print("function")

def teardown_function():
    print("tfunction")

def setup_module():
    print("module")

def teardown_module():
    print("tmodule")


def test_02(Ailian):
    print('test_02')

# pytest中的class对象定义:要以test开头定义
class TestDemo():
    def setup_function(self):
        print("function")

    def teardown_function(self):
        print("tfunction")

    def test_01(self):
        print('test01!')

    def test_02(self):
        print('test02!')

def test_01(Ailian):
    print('test_01')


# pytest函数主入口
if __name__ == "__main__":
    # main()可以加参数，里面加的是 list，以空格隔开来区分指令
    pytest.main(['-s', "test_pytest.py"])  # '-sv'与 '-s','-v'是一样的的效果
    # pytest.main(['-rA'])
