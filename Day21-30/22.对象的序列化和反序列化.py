"""
读写JSON格式的数据
"""

import json

my_dict = {
    "name": "骆昊",
    "age": 40,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 280},
    ],
}
print(json.dumps(my_dict))

my_dict = {
    "name": "骆昊",
    "age": 40,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 280},
    ],
}
# with open("data.json", "w") as file:
#     json.dump(my_dict, file)


with open("data.json", "r") as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)


"""
包管理工具pip
pip3 --version

安装
pip3 install ujson

更新
pip3 install -U ujson

卸载
pip3 uninstall -y ujson

查看
pip3 list
"""