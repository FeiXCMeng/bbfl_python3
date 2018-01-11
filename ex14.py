#-*- coding:utf-8 -*-
promot = '>>>>>>'
print('Do you like me?')
likes = input(promot)

print('where are you from?')
area = input(promot)

print('what kind of computer do you have?')
computer = input(promot)

print('''
ok, you said you {} me;
and you are from {};
and you hava a {} computer.
''' .format(likes, area, computer))
