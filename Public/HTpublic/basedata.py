# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/17 上午11:46

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标类，进行鼠标悬停等操作
import logging
from Config.config import ConfigManger  # 导入配置文件，读取元素定位方式

# 显示等待需要导入的模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseMethod(object):
    def __init__(self):
        """获取元素定位方式"""
        self.rl = ConfigManger.LOCATOR_METHOD

    @staticmethod
    def open_browser(browser_type):
        """获取浏览器驱动"""
        # 如果是使用 chrome 浏览器运行
        global driver
        if browser_type == 'chrome':
            driver = webdriver.Chrome()
            driver.maximize_window()
            time.sleep(2)
            # return driver
        # 如果是使用 Firefox 浏览器运行
        elif browser_type == 'firefox':
            driver = webdriver.Firefox()
            driver.maximize_window()
            time.sleep(2)
            # return driver
        else:
            print('type Error')

    # 打开网页
    def open_url(self, url):
        openurl = driver.get(url)
        return openurl

    def locator(self, name, ele_text):
        """查找单个元素"""
        name = self.rl[name]
        el = driver.find_element(name, ele_text)
        return el
        # if name == 'xpath':
        #     el = driver.find_element_by_xpath(ele_text)
        #     return el
        # elif name == 'css':
        #     el = driver.find_element_by_css_selector(ele_text)
        #     return el

    def find_elements(self, name, ele_text):
        """查找多个相同元素"""
        name = self.rl[name]
        el = driver.find_elements(name, ele_text)
        return el

    # 隐式等待方法
    def implicit_wait(self, *args):
        driver.implicitly_wait(60)
        self.locator(*args)

    # 显示等待方法
    def waiting(self, name, ele_text):
        """name为元素定位方式，ele_text为定位文本"""
        name = self.rl[name]
        el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((name, ele_text)))
        return el
        # if name == 'xpath':
        #     el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((self.name, ele_text)))
        #     return el
        # elif name == 'css':
        #     el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ele_text)))
        #     return el

    # 点击方法
    def click_way(self, *args):
        """需要传入两个参数：定位方式，定位文本"""
        el = self.locator(*args).click()
        logging.info('点击元素：{}'.format(*args))
        return el

    # 输入方法
    def input_way(self, *args, input_text):
        """args需要两个参数：定位方式，定位文本"""
        # ele_text参数是控件元素文本
        # input_text参数是输入文本
        # 防止有些控件需要点击一下光标才能定位到输入框
        self.click_way(*args)
        # 输入前清空输入框
        self.locator(*args).clear()
        # 往输入框输入内容
        self.locator(*args).send_keys(input_text)
        logging.info('输入文本：{}'.format(*args, input_text))

    # 获取悬停类控件
    def hover(self, *args):
        ele = self.locator(*args)
        ActionChains(driver).move_to_element(ele).perform()

    # 获取跳转页面类控件(多窗体)
    def switch_window(self):
        # driver.window_handles：打印所有窗体信息
        # driver.window_handles[-1]：获取最后打开的窗体信息
        driver.switch_to.window(driver.window_handles[-1])
        # 跳转后等待，等待这块可以根据后期需求使用显示等待或者隐身等待
        # self.waiting(location_text, ele_text)

    # 获取控件文本信息方法
    def get_ele_text(self, *args):
        text = self.locator(*args).text
        return text

    # 切换到 iframe 框架里面
    def switch_iframe(self, *args):
        to_frame = self.locator(*args)
        driver.switch_to.frame(to_frame)

    # 从 iframe 切换到 父iframe
    def to_parent_frame(self):
        driver.switch_to.parent_frame()

    # 从 iframe 切换到 html
    def switch_html(self):
        driver.switch_to.default_content()

    # 关闭浏览器方法
    def quit_browser(self):
        driver.quit()


if __name__ == '__main__':
    pass
    BaseMethod().open_browser('chrome')
    url = 'https://test-tehang-system-env-3.teyixing.com/login'
    BaseMethod().open_url(url)
