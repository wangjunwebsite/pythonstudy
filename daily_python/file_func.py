#文件内建函数
'''
open(name,mode)        打开文件
read()        输入,读取
readline()    输入一行
seek()        文件内移动，第一个参数代表偏移位置，第二个参数 0表示从开头开始偏移，1表示当前位置，2从文件结尾
write()       输出，输入
close()       关闭 文件
tell()        告诉指针位置
'''
# _*_ coding: UTF-8 _*_
#给文件添加一个主角名
# file1 = open('name.txt','w',encoding='UTF-8')
# file1.write('诸葛亮')
# file1.close()
#
# file2 = open('name.txt',encoding='UTF-8')
# print(file2.read())
# file2.close()
#
#
# file3 = open('name.txt','a',encoding= 'utf-8')
# file3.write('曹操')
# file3.close()

# file4 = open('name.txt',encoding= 'utf-8')
# print(file4.readline())
#
# file5 = open('name.txt',encoding= 'utf-8')
# for line in file5.readlines():
#     print(line)
#     print('=====')

file6 = open('name.txt',encoding='utf-8')
print(file6.tell())
file6.read(3)
print(file6.tell())
file6.seek(1,0)
print(file6.tell())
file6.close()