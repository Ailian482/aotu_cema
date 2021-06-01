# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 下午5:02

import os
import yaml
from Config.config import ConfigManger


class ReadTestData(object):
    """获取元素目录及元素"""

    def __init__(self, name):
        self.filename = '{}.yaml'.format(name)
        self.testdata_path = os.path.join(ConfigManger.TESTDATA_PATH, self.filename)
        if not os.path.exists(self.testdata_path):
            raise FileNotFoundError('{}文件不存在'.format(self.testdata_path))
        with open(self.testdata_path, encoding='utf-8') as f:
            self.datas = yaml.safe_load(f)  # 从yaml文件读取到数据，并且以字典形式储存

    def __getitem__(self, item):
        """获取yaml文件中的value值"""
        data = self.datas.get(item)
        return data
        # return 16
        # print(type(data))
        # if data:
        #     location_text, ele_text = data.split('==')
        #     return location_text, ele_text
        # raise ArithmeticError("{0}中不存在关键字：{1}".format(self.filename, item))


if __name__ == "__main__":
    # 当实例对象通过[] 运算符取值时，会调用它的方法__getitem__
    ele = ReadTestData("adminlogindata")  # 实例对象
    print(ele.testdata_path)
    print(ele['账号'])  # 通过[]取值，调用__getitem__方法

