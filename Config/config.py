#!/usr/local/bin/python3.8.8
import configparser
import os, sys
from selenium.webdriver.common.by import By
import time

'''os.path.split()与os.path.join()配合使用的用法'''
# path1 = os.path.split(__file__)  # 返回文件的绝对路径和文件名，元组
# path2 = os.path.split(__file__)[0]  # 返回文件的绝对路径
# path3 = os.path.split(__file__)[1]  # 返回文件名
# path4 = (os.path.split(__file__)[0])[0]  # 返回文件所在项目的项目路径
# file_path = os.path.join(path2, "config.ini")  # 拼接的config文件所在的路径
#
# print(path1)
# print(path2)
# print(path3)
# print(path4)


class ConfigManger(object):
    # 项目目录
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_PATH, 'PageElements')

    # 测试报告路径
    REPORT_PATH = os.path.join(BASE_PATH, 'Report')

    # 测试数据路径
    TESTDATA_PATH = os.path.join(BASE_PATH, 'TestData')

    # 元素定位方式
    LOCATOR_METHOD = {
        'xpath': By.XPATH,
        'css': By.CSS_SELECTOR,
        'id': By.ID,
        'name': By.NAME,
        'class': By.CLASS_NAME,
        'link': By.LINK_TEXT,
        'plink': By.PARTIAL_LINK_TEXT,
        'tag': By.TAG_NAME
    }

    # 邮件信息
    EMAIL_MESSAGE = {
        'username': 'Ailian_1104',
        'passwd': 'ailian1104'
    }

    # 收件人
    ADDRESSEE = [
        '1479844088@qq.com'
    ]

    # 获取配置文件
    @property    # 创建只读属性，将类函数内部的方法修饰成同名的只读属性，调用的时候按照调用属性方法
    def ini_file(self):  # 调用该方法的时候需要 实例化一个对象
        ini_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(ini_file):
            raise FileNotFoundError('{}文件不存在，请检查配置文件'.format(ini_file))
        return ini_file

    # 获取日志文件
    @property
    def log_file(self):
        # log_path = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
        log_path = self.BASE_PATH
        log_file = os.path.join(log_path, 'TestLog')
        # 获取当前时间
        # now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        now_date = time.strftime("%Y年-%m月-%d日", time.localtime(time.time()))
        if not os.path.exists(log_file):  # 如果不存在log_file文件夹就创建这个文件夹
            os.makedirs(log_file)
        # 创建日志文件，格式：xxxx年-xx月-xx日
        file_name = os.path.join(log_file, log_file, '{}.log'.format(now_date))
        fp = open(file_name, 'wb')
        fp.close()
        return file_name

if __name__ == "__main__":
    print(ConfigManger.BASE_PATH)
    print(ConfigManger.REPORT_PATH)
    print(ConfigManger.LOCATOR_METHOD['css'])
    print(ConfigManger().ini_file)
    print(ConfigManger.TESTDATA_PATH)
    # print(ConfigManger().log_file)
    # print(By.CSS_SELECTOR)
