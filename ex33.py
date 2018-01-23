# -*- coding:utf-8 -*-
def while_example(the_one, grade):
    i = 0
    num = []

    while i < the_one:
        num.append(i)
        i += grade

    print(num)

if __name__ == "__main__":
    while_example(20, 3)