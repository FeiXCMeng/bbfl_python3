#-*- coding:utf-8 -*-
def print_two(*args):
	arg1, arg2 = args
	print("arg1: {}, arg2: {}" .format(arg1, arg2))

def print_two_again(arg1, arg2):
	print("arg1: {}, arg2: {}" .format(arg1, arg2))

print_two("jack", "rose")
print_two_again("jack", "rose")