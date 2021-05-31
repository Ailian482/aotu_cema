# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/31 下午5:02

import os
import yaml
from Config.ReadConfig import readconfig


class ReadElement(object):
    """获取元素目录及元素"""

    def __init__(self, name):
        self.filename = '{}.yaml'.format(name)
        self.element_path = os.path.join(readconfig.ELEMENT_PATH, self.filename)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError('{}文件不存在'.format(self.element_path))
        with open(self.element_path, encoding='utf-8') as f:
            self.datas = yaml.safe_load(f)  # 从yaml文件读取到数据，并且以字典形式储存

    def __getitem__(self, item):
        """获取yaml文件中的value值"""

        data = self.datas.get(item)
        print(type(data))
        if data:
            # location_text, ele_text = data.split('==')
            # return location_text, ele_text
            text = data.split('==')
            print(text)

        raise ArithmeticError("{0}中不存在关键字：{1}".format(self.filename, item))


if __name__ == "__main__":
    # print(ReadElement('adminlogin').data)
    print(ReadElement("adminlogin").datas['账号'])
