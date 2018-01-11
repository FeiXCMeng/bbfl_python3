from sys import argv
#执行脚本是，命令类似：python ex15.py ex15_data.py
#有几个参数，就加几个参数
script, filename = argv

txt = open(filename)

print("your filename is {}:" .format(filename))
print(txt.read())

print("tpye the filename again:")
new_file = input('>')

new_txt = open(new_file)
print("you new file is:")
print(new_txt.read())
