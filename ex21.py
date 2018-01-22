# -*- coding:utf-8 -*-
def add(a, b):
	print("add {0} + {1}" .format(a, b))
	return a + b

def subtract(a, b):
	print(" subtract {} - {}" .format(a, b))
	return a - b

def multiply(a, b):
	print(" multiply {} - {}" .format(a, b))
	return a * b

def divide(a, b):
	print(" divide {} - {}" .format(a, b))
	return a / b

age = add(30, 2)
height = subtract(32, 3)
weight = multiply(40, 4)
iq = divide(100, 6)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print(what)
