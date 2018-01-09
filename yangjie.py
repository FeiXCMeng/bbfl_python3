# -*- coding:utf-8-*-

'''方法一：边读边写'''
# def read_txt():
#     with open('F:\\111.txt', 'r') as f:
#         for line in f.readlines():
#             with open('F:\\222.txt', 'a') as p:
#                 p.write(line.strip()+'=FLOAT\n')
#
#     p.close()
#     f.close()

'''方法二：读完，存到list，在从list读，写到另外一个文件中'''
def read_txt():

    with open('F:\\111.txt', 'r') as r:
        a = []
        for line in r.readlines():
            a.append(line.strip()+'=FLOAT\n')
        return a
        # print(a)
        r.close()

def print_txt(a):
    with open('F:\\222.txt', 'a') as p:
        for i in a:
            p.write(i)
        p.close()

if __name__ == '__main__':
    a= read_txt()
    print_txt(a)
