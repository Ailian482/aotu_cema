# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/17 上午11:40


from Public.HTpublic.basedata import BaseMethod
from Public.readtestdata import ReadTestData
from Public.reconfig import ReadConfig
from BasePage.HTPages.adminloginpage import AdminLoginPage
import time


# import unittest

class AdminLogin(object):
    """后台用户登录"""
    def __init__(self):
        rd = ReadTestData('adminlogindata')
        self.account = rd['账号']
        self.passwd = rd['密码']

    def login(self):
        # 启动浏览器
        BaseMethod().open_browser('chrome')
        # 获取登录URL
        url = ReadConfig().get_config_message('http', 'login_url')
        # 打开网页
        BaseMethod().open_url(url)
        time.sleep(5)
        # 定位用户手机号元素
        AdminLoginPage().input_account(self.account)
        # 定位用户密码
        AdminLoginPage().input_passwd(self.passwd)
        # 定位登录按钮
        AdminLoginPage().click_login()


if __name__ == "__main__":
    AdminLogin().login()

