#-*-coding:utf-8 -*-
the_count = [1, 3, 5, 7, 9]
fruits = ["apple", "oranges", "pears", "bananas"]
change = [2, "pennies", 4, "dimes", 6, "quarters", 8]

for number in the_count:
    print("the count is {}" .format(number), end=" ")

for fruit in fruits:
    print("the fruit is {}" .format(fruit))

for i in change:
    print("i got %s" % i)

elements = []

for i in range(1, 19):
    elements.append(i)
print(elements)

