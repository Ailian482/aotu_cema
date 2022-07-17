# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/28 下午8:25

"""
工具类：结构中层级属于底层逻辑代码层级

"""
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from cema.config import config
from cema.config.Chrome_Options import ChromeOption
from selenium.webdriver.support.relative_locator import locate_with
from lxml import etree


def open_browser(type_):
    if type_ == "Chrome":
        driver = webdriver.Chrome(options=ChromeOption().options())
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                               {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'})
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception as e:
            print("Exception Information" + str(e))
            driver = webdriver.Chrome()
    return driver


"""
Python 的反射机制：
    四大内置函数：其中常用的是 getattr 函数，就是获取指定类的指定属性
    getattr(类, 属性)，相当于 类.属性 的意思
    例如：
        webdriver.Chrome == getattr(webdriver, 'Chrome')
    基于反射获取属性是这个反射函数的基本定义。获取函数就需要在末尾加上括号 ()
    例如：
        webdriver.Chrome() == getattr(webdriver, 'Chrome')()
        
反射机制可以使用的场景：
    当某个类或者函数需要根据 传入的参数进行判断，而这个参数刚好是 需要调用的某个类下面的一个成员(属性或者方法）
    简言之就是：需要基于传入的参数来决定需要调用什么属性或者函数，而这个属性或者函数跟这个参数数相关联的，那么就可以用这个反射机制来简化代码
    这样就可以将复杂是 if ... else 判断结构简化
    
        
例如 open_browser() 函数：
    不用反射的形态：
        if type_ == "Chrome":
            driver = webdriver.Chrome()
        elif type_ == "Firefox":
            driver = webdriver.Firefox()
        elif type_ == "Ie":
            driver = webdriver.Ie()
        elif type_ == "Safari":
            driver = webdriver.Safari()
        elif type_ == "Edge":
            driver = webdriver.Edge()
        
"""


# 基于 type_值决定生成的 driver 对象是什么类型
class Keys(object):
    # 构造函数
    def __init__(self, text):
        # 创建临时 driver
        self.driver = open_browser(text)
        # 一般创建了 webdriver 之后就会设置一个 隐式等待
        self.driver.implicitly_wait(10)
        self.log = config.get_log('../config/log.ini')

    # 访问 url
    def open(self, text):
        self.driver.get(text)

    # 定位元素
    def locate_ele(self, name, value):
        return self.driver.find_element(name, value)

    # 点击操作
    def click(self, name, value):
        self.locate_ele(name, value).click()

    # 输入
    def input(self, name, value, text):
        self.locate_ele(name, value).send_keys(text)

    # 获取元素中的文本内容
    def get_text(self, name, value, text):
        if text == 'text()':
            html = etree.HTML(self.driver.page_source)
            text_translation = html.xpath(value + '/text()')[0]
            return text_translation
        else:
            text_translation = self.locate_ele(name, value).text
            return text_translation

    # 退出
    def quit(self):
        self.driver.quit()

    # 显示等待, 会返回一个操作元素，所以需要用 return
    def web_driver_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda ele: self.locate_ele(name, value), message='查找元素失败')

    # 强制等待
    def wait_(self, text):
        time.sleep(text)

    # 切换 iframe 句柄
    def switch_frame(self, value, name=None):
        """
        传入一个参数，可以是id、name、webelement
        :param value:
        :param name:
        :return:
        """

        if name is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate_ele(name, value))

    # 切换 default 窗体
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 相对定位器
    def locate_with(self, el_name, el_value, method, value, direction):
        el = self.locate_ele(el_name, el_value)
        direction_dict = {
            'left': 'to_left_of',  # 左侧
            'right': 'to_right_of',  # 右侧
            'above': 'above',  # 上方
            'below': 'below',  # 下方
            'near': 'near'  # 靠近
        }
        if isinstance(method, str):
            method_dict = {
                'id': By.ID,
                'xpath': By.XPATH,
                'css': By.CSS_SELECTOR,
                'name': By.NAME,
                'class': By.CLASS_NAME,
                'tag_name': By.TAG_NAME,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT
            }
            return self.driver.find_element(getattr(
                locate_with(method_dict.get(method), value), direction_dict.get(direction)
            )(el))

    # 句柄的切换(考虑不同场景的不同切换）
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 句柄切换2
    # def switch_handle_1(self, index):
    #     handles = self.driver.window_handles
    #     self.driver.switch_to.window(handles[index])

    # 文本断言
    def assert_text(self, name, value, text, expect):
        log = config.get_log('../config/log.ini')
        try:
            reality_text = self.get_text(name, value, text)
            assert expect == reality_text, "断言失败，实际结果为：{}".format(reality_text)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            # self.log.info("断言失败，实际结果为：{}".format(e))
            log.exception("断言失败，实际结果为：{}".format(e))
            return False

    def assert_input(self, name, value, expect):
        """断言文本框的内容为 输入的内容"""
        try:
            reality_text = self.locate_ele(name, value).get_attribute("value")
            assert expect == reality_text, "断言失败，实际结果为：{}".format(reality_text)
        except Exception as e:
            print('断言失败信息：' + str(e))
            # self.log.exception("断言失败，实际结果为：{}".format(e))
            return False


log = Keys('Chrome').log
# if __name__ == "__main__":
# d = Keys("chrome")
# d.open("https://www.baidu.com/")
# # d.click_ele(By.ID, 'kw')
# # d.wait_(5)
# d.input_text(By.ID, 'kw', "小白猪")
