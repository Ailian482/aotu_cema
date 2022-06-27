# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/7/15 下午3:11

import json
import browsercookie
# from time import sleep
# from selenium import webdriver
# import requests
# import utils
#
#
# def get_cookie(account, password):
#     url = 'https://ct.ctrip.com/biztravel/login/index?lang=zh-cn'
#     dr = webdriver.Chrome()
#     dr.implicitly_wait(10)
#     dr.maximize_window()
#     dr.get(url)
#     dr.find_element_by_id("nloginName").click()
#     dr.find_element_by_id("nloginName").clear()
#     sleep(2)
#     dr.find_element_by_id("nloginName").send_keys(account)
#     dr.find_element_by_id("passwd").click()
#     dr.find_element_by_id("passwd").clear()
#     dr.find_element_by_id("passwd").send_keys(password)
#     sleep(2)
#     dr.find_element_by_xpath("//*[@zz-data-lang='login_block_btn_login']").click()
#     sleep(1)
#     cookie_items = dr.get_cookies()
#     print(cookie_items)
#     dr.quit()
#     cookie = ""
#     for item in cookie_items:
#         if item["name"] == "cticket":
#             cookie = item["value"]
#     return cookie
#
#
# cookie = get_cookie('13632296409', 'ailian11041996')
# print(cookie)


# def get_cookies(domain, browser='chrome'):
#    browser_cookies = getattr(browsercookie, browser.lower())()
#    domain_specified_cookies = [c for c in browser_cookies if domain in c.domain]
#    cookies = [
#        {
#            'name': getattr(cookie, 'name'),
#            'value': getattr(cookie, 'value'),
#            'path': getattr(cookie, 'path'),
#            'domain': getattr(cookie, 'domain'),
#            'secure': bool(getattr(cookie, 'secure')),
#            'expires': getattr(cookie, 'expires')
#        }
#        for cookie in domain_specified_cookies
#    ]
#    cookies_len = len(cookies)
#    # print(cookies_len)
#    for n in range(0, cookies_len-1):
#        cookie_dict = cookies[n]
#        # print(cookie_dict)
#        cookie_name = cookie_dict["name"]
#        # print(cookie_name)
#        if cookie_name == "cticket":
#            cticket_cookie = cookie_dict["value"]
#            # print(cticket_cookie)
#            return (cookie_name,cticket_cookie)
#
#
# print(get_cookies("ctrip.com"))