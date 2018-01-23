#-*- conding:utf-8 -*-
people = 30
cats = 20
dogs = 32

if people < cats:
    print("too many cats, not good!")
else:
    print("the world is good!")

people += 2

if people >= dogs:
    print("the people is equal to dogs!")

cats += 12
print(cats)

if people < cats:
    print("cats win:" + str(cats))
elif people > cats:
    print("people win:" + str(people))
else:
    print("no one win")