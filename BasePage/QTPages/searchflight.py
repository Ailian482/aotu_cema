# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/25 下午4:13


from BasePage.HTPages.callcenter import BaseMethod
from Public.HTpublic.to_flights import ToFlights
from BasePage.HTPages.callcenter import CallCenterDetails
import time


class SearchFlight(object):
    # 选择选框「出发/到达城市」
    def select_city(self, location_text1, location_text2, location_text3):
        # 每一个location_text都需要有2个参数（定位方式，定位文本）
        # # 如果出发城市输入框出现了继续往下走
        # BaseMethod().waiting(*location_text1)
        # # 点击「输入框」
        # BaseMethod().click_way(*location_text1)
        try:
            # 如果出发城市输入框出现了继续往下走
            BaseMethod().waiting(*location_text1)
            # 点击「输入框」
            BaseMethod().click_way(*location_text1)
            try:
                # 等待需要定位城市分类出现
                BaseMethod().waiting(*location_text2)
                # 选择「城市分类」
                BaseMethod().click_way(*location_text2)
                try:
                    # 等待需要定位的城市名称出现
                    BaseMethod().waiting(*location_text3)
                    # 选择「具体某个城市」
                    BaseMethod().click_way(*location_text3)
                except:
                    # 转到日志中，目前不会转
                    print('城市数据未加载出来')
            except:
                # 转到日志中，目前不会转
                print('选择框未出现或者城市分类标签未出现')
        except:
            # 转到日志中，目前不会转
            print('城市输入框不存在')

    # 输入「出发/到达城市」，再选择
    def input_city(self, *input_ele):
        # 传入一个列表或元组大于或者等于三个元素，每个元素需要传入
        location_text1 = input_ele[0]  # 需要两个参数（定位方式，定位文本，输入文本）
        location_text2 = input_ele[1]  # 需要三个参数（定位方式，定位文本，输入文本）
        location_text3 = input_ele[2]
        try:
            # 如果出发城市输入框出现了继续往下走
            BaseMethod().waiting(*location_text1)
            # 点击「输入框」
            BaseMethod().click_way(*location_text1)
            # 输入你要查找的城市
            BaseMethod().input_way(*location_text1)
            try:
                # 等待输入城市出现
                BaseMethod().waiting(*location_text2)
                # 选择「城市」
                BaseMethod().click_way(*location_text2)
            except:
                # 转到日志中，目前不会转
                print('选择框未出现或者城市分类标签未出现')
        except:
            # 转到日志中，目前不会转
            print('城市输入框不存在')

    # 选择「出发/返程日期」
    def select_depdate(self):
        pass

    # 输入「出发/返程日期」
    def select_bacdate(self):
        pass

    #


if __name__ == "__main__":
    ToFlights().web_teyixing()
    dep_city1 = ('xpath', "//div/nz-form-item[1]/nz-form-control/div/span/airport-picker/input")
    dep_city2 = ("css", "div.ant-tabs-nav-wrap>div>div>div>div:nth-child(1)")
    dep_city3 = ("xpath", "//span[@title='北京']")
    arr_city1 = ('xpath', "//div/nz-form-item[2]/nz-form-control/div/span/airport-picker/input")
    arr_city2 = ('css', "div.ant-tabs-nav-wrap>div>div>div>div:nth-child(1)")
    arr_city3 = ('xpath', "//span[@title='深圳']")

    SearchFlight().select_city(dep_city1, dep_city2, dep_city3)
    time.sleep(2)
    SearchFlight().select_city(arr_city1, arr_city2, arr_city3)
    time.sleep(10)
    BaseMethod().quit_browser()