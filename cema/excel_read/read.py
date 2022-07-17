# -*- coding:utf-8 -*-
# 作    者：Ailian
# 开发时间：2022/6/27 22:20

"""
基于Excel文件的内容去进行读取，并结合获取的数据进行自动化的测试执行
"""
# 读取 Excel 中的用例正文

import openpyxl

from cema.config import config
from cema.excel_read import excel_conf
from cema.底层代码封装.keys import Keys,log


def read(file):
    # log = config.get_log('../config/log.ini')
    excel = openpyxl.load_workbook(file)
    try:
        for name in excel.sheetnames:
            sheet = excel[name]
            print('***********{}*************'.format(name))
            for values in sheet.values:
                # 如果第一个单元格是 int 类型，则表示进入了测试用例的核心内容
                if type(values[0]) is int:
                    log.info('当前正在执行{}'.format(values[5]))
                    # print(values)
                    # 接收每一行操作行为对应的参数内容
                    data = dict()
                    data['name'] = values[2]
                    data['value'] = values[3]
                    data['text'] = values[4]
                    data['expect'] = values[6]
                    # print(data)
                    # 清除参数字典中为 None 的参数键值对
                    for key in list(data.keys()):
                        if data[key] is None:
                            del data[key]

                    # 基于操作行为和对应参数来执行自动化操作
                    """
                        用例的操作行为主要分为：
                            1. 实例化，通过一个操作行为实例化关键字驱动类对象
                            2. 常规操作，通过调用实例化的对象执行对应的函数
                            3. 断言操作，判断预期与实际是否符合，将结果写入测试用例中。
                    """

                    # 实例化关键字驱动
                    if values[1] == 'open_browser':
                        keys = Keys(**data)
                    # 断言操作
                    elif 'assert' in values[1]:
                        status = getattr(keys, values[1])(**data)
                        # 基于断言结果True or False 来进行写入操作
                        if status:
                            excel_conf.write_result(sheet.cell, row=values[0] + 2, column=8)
                        else:
                            excel_conf.write_result(sheet.cell, row=values[0] + 2, column=8, status=2)
                        # 断言后的 Excel 写入
                        excel.save(file)
                    # 常规操作
                    else:
                        getattr(keys, values[1])(**data)
    except Exception as e:
        log.exception('运行异常：{}'.format(e))

    finally:
        excel.close()


if __name__ == "__main__":
    read('../excel_data/excel_driver.xlsx')
    # my_dict = {'date': '2022-06-30', 'time': '11:05'}
    # print(len(my_dict))
