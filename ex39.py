# -*- coding:utf-8 -*-

# province
provinces = {
    "广东省": "粤",
    "江苏省": "苏",
    "浙江省": "浙",
    "安徽省": "皖",
    "山东省": "鲁"
}

cities = {
    "粤": "广州",
    "苏": "南京",
    "浙": "杭州",
}

cities["皖"] = "合肥"
cities["鲁"] = "济南"

print('-' * 20)
print("安徽的简称是:", provinces["安徽省"])
print("安徽的省会是:", cities["皖"])

print('-' * 20)
print("山东的简称是:", provinces["山东省"])
print("山东的省会是:", cities[provinces["山东省"]])

print('-' * 20)
for province, abbrev in provinces.items():
    print("{0}de简称是： {1}" .format(province, abbrev))

print('-' * 20)
for city, abbrev in cities.items():
    print("{0}de省会是： {1}" .format(city, abbrev))

print('-' * 20)
for province, abbrev in provinces.items():
    print("{0}的简称是：{1}，{0}的省会是：{2}" .format(province, abbrev, cities[abbrev]))

print('-' * 20)
province = provinces.get('福建省')

if not "福建省":
    print("不是湖建省的！")

city = cities.get("敏", "not exist")
print("福建省的省会是：{}" .format(city))

