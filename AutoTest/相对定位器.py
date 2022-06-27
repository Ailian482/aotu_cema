# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/6/24 17:02

"""
selenium 4.0 相对定位器
"""
from selenium import webdriver
from AutoTest.Chrome_Options import ChromeOption
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


driver = webdriver.Chrome(options=ChromeOption().options())
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                       {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'})

driver.get('https://baidu.com/')
# 定位输入框
el = driver.find_element('xpath', '//input[@id="kw"]')

el.send_keys("小白猪")
# 右侧
search = driver.find_element(locate_with(By.TAG_NAME, 'input').to_right_of(el))
search.click()
# 左侧
search_1 = driver.find_element(locate_with(By.TAG_NAME, 'input').to_left_of(el))
search.click()
# 上方
img = driver.find_element(locate_with(By.TAG_NAME, 'img').above(el))
print(img)
# 下方
div = driver.find_element(locate_with(By.TAG_NAME, 'div').below(el))
print(div)
# 靠近
span = driver.find_element(locate_with(By.TAG_NAME, 'span').near(el))
print(span)

iframe = driver.find_elements_by_tag_name()


