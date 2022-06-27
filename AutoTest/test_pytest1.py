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

"""


import pytest

def test_02():
    print('test_101')

def test_01():
    print('test_102')


# pytest函数主入口
if __name__ == "__main__":
    # main()可以加参数，里面加的是 list，以空格隔开来区分指令
    pytest.main(['-s'])
