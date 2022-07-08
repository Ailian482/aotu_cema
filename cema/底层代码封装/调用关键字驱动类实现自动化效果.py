# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/6/7 下午12:37

from cema.底层代码封装.keys import Keys
# from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
from lxml import etree
import requests

# Key = Keys("Chrome")
# Key.open("https://baidu.com/")
# Key.click("id", 'kw')
# Key.input("id", "kw", "小白猪")
# Key.assert_input("id", "kw", "小白猪")
# Key.click("id", 'su')

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=option)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                  {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'})

driver.get("https://baidu.com/")
ele = driver.find_element("id", 'kw')
ele.click()
ele.send_keys('小白猪')
ele_2 = driver.find_element('id', 'su')
ele_2.click()
time.sleep(3)

# print(driver.find_element('xpath', '//div[@id="tsn_inner"]/div[2]/div').get_attribute('innerText'))

html = etree.HTML(driver.page_source)
text_translation = html.xpath('//div[@id="tsn_inner"]/div[2]/div/text()')[0]
print(text_translation)

driver.quit()

