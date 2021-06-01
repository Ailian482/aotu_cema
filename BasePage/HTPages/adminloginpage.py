# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 下午4:28

from Public.HTpublic.basedata import BaseMethod
from Public.readelement import ReadElement
from Public.reconfig import ReadConfig
import time

# 实例化获取页面元素对象
read_ele = ReadElement("adminlogin")


class AdminLoginPage(BaseMethod):
    """后台登录类"""

    def input_account(self, input_text):
        """输入账号"""
        args = read_ele['账号']
        self.input_way(*args, input_text=input_text)

    def input_passwd(self, input_text):
        """输入密码"""
        args = read_ele['密码']
        self.input_way(*args, input_text=input_text)

    def click_login(self):
        """点击登录"""
        args = read_ele['登录按钮']
        self.click_way(*args)


if __name__ == "__main__":
    BaseMethod().open_browser('chrome')
    url = ReadConfig().get_config_message('http', 'login_url')
    BaseMethod().open_url(url)
    time.sleep(5)
    AdminLoginPage().input_account('111190')
    AdminLoginPage().input_passwd('@12345678')
    AdminLoginPage().click_login()
