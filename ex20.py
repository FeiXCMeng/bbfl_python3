#-*- coding:utf-8 -*-
from sys import argv
script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(1) #移动文件指针到指定位置

def  print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("first, print the whole file:\n")
print_all(current_file)

print("now, rewind, kind of like a tape\n")
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)