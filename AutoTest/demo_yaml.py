# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2022/5/30 下午2:49

import yaml

my_dict = {'a': 1, 'b': 2, '姓名': "Ailian"}

# yaml.safe_dump()
with open('data.yaml', 'w', encoding='UTF-8') as yaml_file:
    # 需要加入 allow_unicode=True 参数，否则，中文会出现乱码
    yaml.safe_dump(my_dict, yaml_file, allow_unicode=True)

# yaml.dump()
with open("dum_data.yaml", "w", encoding="UTF-8") as yaml_file:
    yaml.dump(my_dict, yaml_file, allow_unicode=True)

yaml_string = yaml.dump(my_dict, allow_unicode=True)
print(type(yaml_string), '\n' + yaml_string)

with open('data.yaml', encoding='UTF-8') as yaml_file:
    data = yaml.safe_load(yaml_file)

print(data.get("姓名"))
print(type(data))
print(data)