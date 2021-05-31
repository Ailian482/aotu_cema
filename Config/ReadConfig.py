#!/usr/local/bin/python3.8.8
import configparser
import os

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

class readconfig:
    def __init__(self):
        path = os.path.split(__file__)[0]  # 获取当前文件所在绝对路径
        self.filepath = os.path.join(path, 'config.ini')
        self.readconfig = configparser.ConfigParser()
        self.readconfig.read(self.filepath, encoding='UTF-8')
        # self.readconfig.write(filepath)

    # 获取http配置信息
    def get_URL(self, name):
        self.name = self.readconfig.get('http', name)
        return self.name


if __name__ == "__main__":
    print(readconfig().get_URL("login_url"))
