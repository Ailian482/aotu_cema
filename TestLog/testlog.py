# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/17 下午5:15

"""
#  日志级别
# CRITICAL 50
# ERROR  40
# WARNING 30
# INFO   20
# DEBUG  10
"""

import logging
import os


# # logging.info('info message')
# # logging.warning('warning message')
# logging.basicConfig(filename=os.path.join(os.getcwd(), 'log.txt'), level=logging.DEBUG)
# logging.debug('this is a message')
# logging.debug('debug message')

import pretty_errors

def console_out(logFilename):

    logging.basicConfig(
        level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s %(filename)s : %(levelname)s %(message)s',  # 定义输出log的格式
        # datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        datefmt='%a, %d %b %Y %H:%M:%S',  # 时间
        filename=logFilename,  # log文件名
        filemode='a'  # 写入模式"w"或'a'
    )
    #
    console = logging.StreamHandler()  # 定义console handler
    console.setLevel(logging.DEBUG)  # 定义handler级别
    formatter = logging.Formatter('%(asctime)s %(filename)s : %(levelname)s %(message)s')  # 定义该handler格式
    console.setFormatter(formatter)
    # Create an instance
    logging.getLogger().addHandler(console)  # 实例化添加 handler
    logging.debug('logger debug message')
    logging.info('logger info message')
    logging.warning('logger warning message')
    logging.error('logger error message')
    logging.critical('logger critical message')

if __name__ == "__main__":
    filename = os.path.join(os.getcwd(), 'log.txt')
    console_out(filename)
