# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/25 下午2:48


from Public.HTpublic.h_login import Login
from BasePage.HTPages.callcenter import CallCenter
from BasePage.HTPages.callcenter import CallCenterDetails
from Public.HTpublic.basedata import BaseMethod
import time

class ToFlights(object):
    def __init__(self):
        Login().login()
    def web_teyixing(self):
        # 输入「姓名」进行查询
        name_ele = ('xpath', "//se[@label='姓名']/div/div/span/input", '公孙离')
        submit_ele = ('css', "button[type='submit']")
        # 「选择」按钮
        # select_text = "//tbody/tr[1]/td[10]/span[2]/span[2]"
        select_text = ("xpath", "//tbody/tr[1]/td[10]/span[2]/span[2]")
        # 「代客预订」按钮
        button_daike = "//nz-tabset/div/div/button[2]"
        CallCenter().query_customer_1(name_ele, submit_ele)
        # BaseMethod().waiting('xpath', select_text)
        BaseMethod().waiting(*select_text)
        # CallCenter().select_customer('xpath', select_text)
        CallCenter().select_customer(*select_text)
        BaseMethod().waiting('xpath', button_daike)
        BaseMethod().click_way('xpath', button_daike)
        time.sleep(2)
        # 切换窗口
        CallCenterDetails().switch_window()


if __name__ == "__main__":
    ToFlights().web_teyixing()
    # BaseMethod().quit_browser()
