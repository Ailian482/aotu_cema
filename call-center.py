# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/21 下午2:46

from Public.HTpublic.basedata import BaseMethod
from Public.HTpublic.h_login import Login
import time

class CallCenter(object):
    # 单个搜索条件
    def query_customer_1(self, input_ele, submit_ele):
        # 姓名控件参数，需要三个参数（定位方式，定位元素文本，输入文本）
        input_ele = input_ele
        # 查询控件参数，需要两个参数（定位方式，定位元素文本）
        submit_ele = submit_ele
        # 显示等待姓名输入框控件出现
        BaseMethod().waiting(input_ele[0], input_ele[1])
        # 输入姓名
        # BasePage().input_way(name_ele[0], name_ele[1], name_ele[2])
        BaseMethod().input_way(*input_ele)
        # 点击查询
        # BasePage().click_way(submit_ele[0], [1])
        BaseMethod().click_way(*submit_ele)
        time.sleep(2)

    # 两个搜索条件
    def query_customer_2(self, input_ele1, input_ele2, submit_ele):
        # 等待控件出现
        BaseMethod().waiting(input_ele1[0], input_ele1[1])
        # 定位输入第一个控件
        BaseMethod().input_way(*input_ele1)
        # 定位输入第二个控件
        BaseMethod().input_way(*input_ele2)
        # 点击查询
        BaseMethod().click_way(*submit_ele)
        time.sleep(2)

    # 三个搜索条件
    def query_customer_3(self, input_ele1, input_ele2, input_ele3, submit_ele):
        # 等待控件出现
        BaseMethod().waiting(input_ele1[0], input_ele1[1])
        # 定位输入第一个控件
        BaseMethod().input_way(*input_ele1)
        # 定位输入第二个控件
        BaseMethod().input_way(*input_ele2)
        # 定位输入第三个控件
        BaseMethod().input_way(*input_ele3)
        # 点击查询
        BaseMethod().click_way(*submit_ele)
        time.sleep(2)

    # 四个搜索条件
    def query_customer_4(self, input_ele1, input_ele2, input_ele3, input_ele4, submit_ele):
        # 等待控件出现
        BaseMethod().waiting(input_ele1[0], input_ele1[1])
        # 定位输入第一个控件
        BaseMethod().input_way(*input_ele1)
        # 定位输入第二个控件
        BaseMethod().input_way(*input_ele2)
        # 定位输入第三个控件
        BaseMethod().input_way(*input_ele3)
        # 定位输入第四个控件
        BaseMethod().input_way(*input_ele4)
        # 点击查询
        BaseMethod().click_way(*submit_ele)
        time.sleep(2)

    # 获取列表某条记录的某项信息
    def get_text_value(self, location_text, ele_text):
        text = BaseMethod().get_ele_text(location_text, ele_text)
        return text

    # 选择某个客户
    def select_customer(self, location_text, ele_text):
        BaseMethod().click_way(location_text, ele_text)


class CallCenterDetails(object):
    # 点击某个按钮
    def click_ele(self, location_text, ele_text):
        BaseMethod().click_way(location_text, ele_text)

    # 切换窗体
    def switch_window(self):
        BaseMethod().skip()



if __name__ == '__main__':
    Login().login()
    name_ele = ('xpath', "//se[@label='姓名']/div/div/span/input", '公孙离')
    phone_ele = ['xpath', "//se[@label='手机']/div/div/span/input", '13632296609']
    submit_ele = ('css', "button[type='submit']")
    # CallCenter().submit_customer('姓名', name_ele, submit_ele)
    CallCenter().query_customer_1(phone_ele, submit_ele)
    print(CallCenter().get_text_value('xpath', "//tbody/tr[1]/td[2]/span[2]/span"))
    # 点击选择按钮
    select_text = "//tbody/tr[1]/td[10]/span[2]/span[2]"
    CallCenter().select_customer('xpath', select_text)
    time.sleep(2)
    # 代客预订按钮
    button_daike = "//nz-tabset/div/div/button[2]"
    CallCenterDetails().click_ele('xpath', button_daike)
    time.sleep(2)

    # 聚焦窗体信息到最新打开的窗口
    CallCenterDetails().switch_window()
    # 等出发城市输入控件出现
    ccity_ele = "//div/nz-form-item[1]/nz-form-control/div/span/airport-picker/input"
    BaseMethod().waiting('xpath', ccity_ele)
    BaseMethod().click_way('xpath', ccity_ele)
    time.sleep(2)
    # 某个城市
    city_name = "//span[@title='北京']"
    BaseMethod().click_way('xpath', city_name)
    time.sleep(2)
    BaseMethod().quit_browser()




