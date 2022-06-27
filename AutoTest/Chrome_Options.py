# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/6/24 14:54

from selenium import webdriver
from selenium.webdriver import ChromeOptions

"""
可以通过隐藏WebDriver提示条和自动化扩展信息来跳过百度安全验证
"""


class ChromeOption(object):

    def options(self):
        """隐藏WebDriver提示条"""
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        return option



if __name__ == "__main__":
    d = webdriver.Chrome(options=ChromeOption().options())
    # 隐藏自动化扩展信息
    d.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'})
    d.get("https://www.baidu.com")