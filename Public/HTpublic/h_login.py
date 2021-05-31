# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/17 上午11:40


from Public.HTpublic.basedata import BaseMethod
from Config.ReadConfig import readconfig
import time


# import unittest

class Login():
    def login(self):
    # 启动浏览器
        BaseMethod().open_browser('chrome')
    # 获取登录URL
        url = readconfig().get_URL('login_url')
    # 打开网页
        BaseMethod().open_url(url)
        time.sleep(5)
    # 定位用户手机号元素
        ele1 = '//div[@class="ant-spin-container"]/div/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input'
        BaseMethod().input_way('xpath', ele1, '111190')
    # 定位用户密码
        ele2 = '//div[@class="ant-spin-container"]/div/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input'
        BaseMethod().input_way('xpath', ele2, '@12345678')
    # 定位登录按钮
        ele3 = '//div[@class="ant-spin-container"]/div/form/nz-form-item[3]/button'
        BaseMethod().click_way('xpath', ele3)

if __name__ == "__main__":
    Login().login()
    BaseMethod.quit_browser()
