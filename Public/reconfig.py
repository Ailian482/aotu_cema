# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/6/1 下午2:38

import os
import configparser
# 是用来读取配置文件的包，配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容。
"""
例如：
[section]
option = value
"""
from Config.config import ConfigManger


class ReadConfig(object):
    def __init__(self):
        # self.path = os.path.split(__file__)[0]  # 获取当前文件所在绝对路径
        # # print(path)
        # self.filepath = os.path.join(self.path, 'config.ini')
        self.readconfig = configparser.ConfigParser()
        self.readconfig.read(ConfigManger().ini_file, encoding='utf-8')
        # self.readconfig.write(filepath)

    # 获取配置信息
    def get_config_message(self, section, option):
        """获取"""
        return self.readconfig.get(section, option)

    # 修改配置信息
    def set_config_message(self, section, option, value):
        """更新"""
        self.readconfig.set(section, option, value)
        with open(ConfigManger().ini_file, 'w') as f:
            self.readconfig.write(f)


if __name__ == "__main__":
    # print(ReadConfig().path)
    print(ReadConfig().get_config_message('browser', 'name'))
    ReadConfig().set_config_message('browser', 'window_weight', '500')