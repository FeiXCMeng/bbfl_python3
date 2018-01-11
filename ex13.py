#-*- coding:utf-8 -*-
from sys import argv
# script, first, second, third = argv

# print("script here is:", script)
# print("your first val is:", first)
# print("your second val is:", second)
# print("your third val is:", third)

#-------------思考题------------
# script, name, age = input()
#
# print("your script name is: {}" .format(script))
# print("your name is: {}" .format(name))
# print("your age is: {}" .format(age))

#---------解包------------------
'''
解包：相当于把东西给拆分了，把tuple的（）去掉，
把字典中的{}去掉
'''
date = (2018, 1, 8) #这边存（2018， 01 ，08）有报错
year, month, day = date
print(year, month, day)

set1 = {'name': 'feixcmeng'}
set2 = {'name': 'admin'}

#pythonic 的合并集合的方法
print({**set1}['name'])
print({**set2 , **set1})
