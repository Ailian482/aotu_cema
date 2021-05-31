# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/17 上午11:46

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标类，进行鼠标悬停等操作
import logging

# 显示等待需要导入的模块
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseMethod(object):

    # 获取浏览器驱动
    def open_browser(self, browser_type):
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

    def locator(self, name, value):
        if name == 'xpath':
            el = driver.find_element_by_xpath(value)
            return el
        elif name == 'css':
            el = driver.find_element_by_css_selector(value)
            return el
        elif name == 'id':
            el = driver.find_element_by_id(value)
            return el
        elif name == 'name':
            el = driver.find_element_by_name(value)
            return el
        elif name == 'class':
            el = driver.find_element_by_class_name(value)
            return el
        elif name == 'link':
            el = driver.find_element_by_link_text(value)
            return el
        elif name == 'plink':
            el = driver.find_element_by_partial_link_text(value)
            return el
        elif name == 'tag':
            el = driver.find_element_by_tag_name(value)
            return el

    # 隐式等待方法
    def implicit_wait(self, location_text, ele_text):
        driver.implicitly_wait(60)
        self.locator(location_text, ele_text)

    # 显示等待方法
    def waiting(self, name, ele_text):
        if name == 'xpath':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.XPATH, ele_text)))
            return el
        elif name == 'css':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ele_text)))
            return el
        elif name == 'id':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.ID, ele_text)))
            return el
        elif name == 'name':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.NAME, ele_text)))
            return el
        elif name == 'class':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, ele_text)))
            return el
        elif name == 'link':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, ele_text)))
            return el
        elif name == 'plink':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, ele_text)))
            return el
        elif name == 'tag':
            el = WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.TAG_NAME, ele_text)))
            return el

    # 点击方法
    def click_way(self, location_text, ele_text):
        el = self.locator(location_text, ele_text).click()
        logging.info('点击元素：{}'.format(location_text, ele_text))
        return el

    # 输入方法
    def input_way(self, location_text, ele_text, input_text):
        # ele_text参数是控件元素文本
        # input_text参数是输入文本
        # 防止有些控件需要点击一下光标才能定位到输入框
        self.click_way(location_text, ele_text)
        # 输入前清空输入框
        self.locator(location_text, ele_text).clear()
        # 往输入框输入内容
        self.locator(location_text, ele_text).send_keys(input_text)
        logging.info('输入文本：{}'.format(location_text, ele_text, input_text))

    # 获取悬停类控件
    def hover(self, location_text, ele_text):
        ele = self.locator(location_text, ele_text)
        ActionChains(driver).move_to_element(ele).perform()

    # 获取跳转页面类控件(多窗体)
    def skip(self):
    # def skip(self, location_text, ele_text):
        # driver.window_handles：打印所有窗体信息
        # driver.window_handles[-1]：获取最后打开的窗体信息
        driver.switch_to.window(driver.window_handles[-1])
        # 跳转后等待，等待这块可以根据后期需求使用显示等待或者隐身等待
        # self.waiting(location_text, ele_text)

    # 获取控件文本信息方法
    def get_ele_text(self, location_text, ele_text):
        text = self.locator(location_text, ele_text).text
        return text

    # 获取有 iframe 框架类控件

    @ classmethod
    # 关闭浏览器方法
    def quit_browser(cls):
        driver.quit()


if __name__ == '__main__':
    pass
    # BasePage().open_browser('chrome').get('https://test-tehang-system-env-3.teyixing.com/login')
    # time.sleep(5)
    # BasePage().input_way('xpath', '//div[@class="ant-spin-container"]/div/form/nz-form-item[1]/nz-form-control/div/span/nz-input-group/input', '111190')
    # ele2 = '//div[@class="ant-spin-container"]/div/form/nz-form-item[2]/nz-form-control/div/span/nz-input-group/input'
    # BasePage().input_way('xpath', ele2, '@12345678')
    BaseMethod().open_browser('chrome')
    url = 'https://test-tehang-system-env-3.teyixing.com/login'
    BaseMethod().open_url(url)
