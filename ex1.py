#-*- coding:utf-8 -*-
# print('Hello World!')

# print('Hello Again')

# print('i like typing this')

# print('this is fun')

# print('yay! Printing')

# print('i have much rather you "not".')

# print(' i "said" do not touch this')

# list_p = [1, 2, 3, 5, 8]
# a = [list_p.index(i) for i in list_p if i == 8][0]
# print(a)

# a = []
# for x in range(1,10):
# 	a.append(x)
# print(a)
# list1 = []
dict1 = {'name':'nanjing', 'value':50}
# dict2 = {'name':'beijing', 'value':30}
# list1.append(dict1)
# # list1.append(dict3)

# print(list1)
# print(dict1['name'])


# dict_kv = dict1.items()
# print(dict_kv)

# new_dict = dict(dict_kv)
# print(new_dict)

raw = "Do you love Canglaoshi? Canglaoshi is a good teacher."
raw_list = raw.split(" ")
for i, string in enumerate(raw_list):
	if 'Canglaoshi' in string:
		raw_list[i] = "PHP"
print(raw_list)
new_raw = ' '.join(raw_list)
print(new_raw)


