#-*- coding:utf-8 -*-
import  random
print("输入一个数字，猜测是否正确")

the_one = random.randint(1, 20)
print(the_one)

# num = input(">")
#
# if int(num) > the_one:
#     print("输入的值大了")
# elif int(num) < the_one:
#     print("输入的值小了")
# else:
#     print("bingo!")

def judge_num():
    num = input(">>>")
    if int(num) > the_one:
        print("bigger")
        judge_num()
    elif int(num) < the_one:
        print("smaller")
        judge_num()
    else:
        print("same")

if __name__ == "__main__":
    judge_num()