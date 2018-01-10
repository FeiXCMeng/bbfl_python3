#-*- coding:utf-8 -*-
#打印必须加一个end参数？
print("what is your name?", end='')
name = input("like joe or jack?")
print("how are you?", end='')
age = int(input("you must input like 23 or 34, otherwise you will get error:"))

print("your name is {}, and you are {} years old." .format(name, age))
