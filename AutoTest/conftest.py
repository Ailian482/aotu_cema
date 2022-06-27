# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 上午10:53

"""
这是一个pytest的 setup和teardown 配置文件
这是一个pytest中的预置函数定义的配置文件
    fixtrue是pytest的一大利器
调用该配置文件下的方法很简单：直接在用例方法传入 配置文件下的方法名 作为用例方法的入参
    例如：在test_pytest.py文件下的用例 test_01() 调用 Ailian()方法
        test_01(Ailain)
scope参数定义的四种等级（默认等级是function）
    session：在本次session级别中只执行一次
    module：在模块级别中只执行一次，只要有符合pytest运行的.py文件及函数，就会去运行它一次
        如果在每个module中都调用了module级别，那么只会在第一个module级别中运行一次，后面的不会再去取了
    class：在类级别中只执行一次
    function：在函数级别中执行，每有一个函数就执行一次


"""

import pytest

# 定义一个基本的setuph和teardown

# 可以用作前期的数据准备

@pytest.fixture(scope='class')
def Ailian():
    print("用电鳗的电电电鳗电鳗会被电鳗的电电死吗！！！")


@pytest.fixture()
def Ailian1():
    return 1

