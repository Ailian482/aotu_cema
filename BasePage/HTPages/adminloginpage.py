# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 下午4:28

from Public.HTpublic.basedata import BaseMethod

# 获取页面元素


class AdminLogin(BaseMethod):
    """后台登录类"""

    def input_account(self, location_text, ele_text, input_text):
        """输入账号"""
        self.input_way(location_text, ele_text, input_text)

    def input_passwd(self, location_text, ele_text, input_text):
        """输入密码"""
        self.input_way(location_text, ele_text, input_text)

    def click_login(self, location_text, ele_text):
        """点击登录"""
        self.click_login(location_text, ele_text)


if __name__ == "__main__":
    pass
