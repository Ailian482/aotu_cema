# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/6/7 下午12:37

from AutoTest.UI_wait import WebPage
# from selenium.webdriver.common.by import By


Key = WebPage("Chrome")
Key.open("https://baidu.com/")
Key.click_ele("id", 'kw')
Key.input_text("id", "kw", "小白猪")
Key.assert_input("id", "kw", "小白猪")
Key.click_ele("id", 'su')

