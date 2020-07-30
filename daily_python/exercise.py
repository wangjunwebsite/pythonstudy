# 练习一 变量的定义和使用
#
# 1. 定义两个变量分别为美元和汇率
# 2. 通过搜索引擎找到美元兑人民币汇率
# 3. 使用Python计算100美元兑换的人民币数量并用print( )进行输出
# dol = 100
# rate = 7.0753
# china = dol * rate
# print(china)

# 练习一 字符串

# 1. 定义一个字符串Hello Python 并使用print( )输出
# 2. 定义第二个字符串Let‘s go并使用print( )输出
# 3. 定义第三个字符串"The Zen of Python" -- by Tim Peters 并使用print( )输出
# str1 = 'Hello Python'
# str2 = "Let's go"
# str3 = '"The Zen of Python" -- by Tim Peters'
# print(str1,str2,str3)

#
# 练习二 字符串基本操作
#
# 1. 定义两个字符串分别为 xyz 、abc
# 2. 对两个字符串进行连接
# 3. 取出xyz字符串的第二个和第三个元素
# 4. 对abc输出10次
# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出
# str1 = 'xyz'
# str2 = 'abc'
# str3 = str1 +str2
# print(str1[1])
# print(str1[2])
# print(str2*10)
# print('a' in str1)
# print('a' in str2)
#
# 练习三 列表的基本操作
#
# 1. 定义一个含有5个数字的列表
#
# 2. 为列表增加一个元素 100
#
# 3. 使用remove()删除一个元素后观察列表的变化
#
# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素
# list1 = [1,4,6,8,3]
# list1.append(100)
# list1.remove(6)
# print(list1)
# print(list1[0:3],list1[-1])
# 练习四 元组的基本操作
#
# 1. 定义一个任意元组，对元组使用append() 查看错误信息
# 2. 访问元组中的倒数第二个元素
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
# 4. 计算元组元素个数
# couple1 = (1,2,3,4,'ggg')
# # couple1.append(33)   #'tuple' object has no attribute 'append'
# print(couple1[-2])
# couple2 = (7,3,5,6,'hfd')
# couple3 = couple1 + couple2
# print(len(couple3))

# 练习一 条件语句的使用

# 1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
# 2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
# str = input('请输入任意字符串：')
# if len(str) > 10 :
#     print('您输入的字符串长度大于10')
# elif len(str) == 10 :
#     print('您输入的字符串长度为10')
# else:
#     print('您输入的字符串长度小于10')
# num = int(input('请输入1-40之间的数字：'))
# if num < 1 or num >40 :
#     print('输入不规范')
# elif 1 <= num <= 10:
#     print('您输入的数字在1-10之间')
# elif 11 <= num <= 20:
#     print('您输入的数字在11-20之间')
# elif 21 <= num <= 30:
#     print('您输入的数字在21-30之间')
# else:
#     print('您输入的数字在31-40之间')

#
# 练习二 循环语句的使用
# 1. 使用for语句输出1-100之间的所有偶数
# 2. 使用while语句输出1-100之间能够被3整除的数字
# for num in range(1,101):
#     if num % 2 == 0:
#         print(num)
#
# i = 1
# while i <= 100:
#     if i % 3 == 0:
#         print(i)
#     i += 1
# 练习一 字典的使用

# 1. 定义一个字典，分别使用a、b、c、d作为字典的关键字，值为任意内容
# 2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕
# 3. 取出字典中关键字为d的值
# dict1 = {'a':56,'b':'gag','c':[1,3,4],'d':True}
# dict1['c'] = 'cake'
# print(dict1)
# print(dict1['d'])
#
# #练习二 集合的使用
# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
# str = 'hello'
# print(set(str))

# 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期
# 2. 再次打开这个文件，读取文件的前4个字符后退出
# import datetime
# time = (datetime.datetime.now())
# file = open('time.txt','w')
# print(file.write('%s'%time))
# file.close()
# file2 = open('time.txt')
# print(file2.read(4))


# 练习一 异常
# 1. 在Python程序中，分别使用未定义变量、访问列表不存在的索引、访问字典不存在的关键字观察系统提示的错误信息
# 2. 通过Python程序产生IndexError，并用try捕获异常处理
#未定义变量错误
# a = fs   NameError: name 'fs' is not defined
#访问列表不存在的
# a = [1,2,3]
# print(a[3])  IndexError: list index out of range
#访问字典不存在的关键字
# a = {'a':45,'b':True}
# print(a['c'])     KeyError: 'c'

# try:
#     a = [1, 2, 3]
#     print(a[3])
# except IndexError as b:
#     print(b)

#funcexe
# 1. 创建一个函数，用于接收用户输入的数字，并计算用户输入数字的和
# def sum():
#     num1 = (int(input('请输入第一个数字：')))
#     num2 = (int(input('请输入第二个数字：')))
#     print(num1,'+',num2,'=',num1+num2)
# sum()
# 2. 创建一个函数，传入n个整数，返回其中最大的数和最小的数
# def max_min(*nums):
#     #创建一个函数
#     print(max(list(nums)))
#     #返回最大数
#     print(min(list(nums)))
#     #返回最小数
#
# max_min(12,345,789,45,3,68,356,79)

# 3. 创建一个函数，传入一个参数n，返回n的阶乘
# def facorial(n):
#     #创建一个函数，定义一个参数n
#
#     if n == 1 or n == 0:
#         return(1)
#     else:
#         return(n * facorial(n-1))
#
# print(facorial(10))
#1.导入os模块，并使用help(os)查看os模块的帮助文档
# import os
# help(os)
# 练习一 定义装饰器，用于打印函数执行的时间
# 1. 统计函数开始执行和结束执行的时间
# 2. 扩展练习：为装饰器传入超时时间，函数执行超过指定时间后退出
#设计函数执行时间本体
# import time
# def timeer(func):
#     def timer():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print('函数运行时间为：%s s'%(end_time-start_time))
#
#     return timer
#
# @timeer
# def nomal_func():
#     time.sleep(6)
#
# nomal_func()

# 练习二 定义装饰器，实现不同颜色显示执行结果的功能
# 1. 向装饰器传递参数，通过传递的参数获取到输出的颜色
# 2. 被装饰函数的print( )输出根据装饰器得到的颜色进行输出
#定义一个装饰器
# def color(func):
#     def get_color(c):
#         c = input('请输入你要的颜色:')
#         get = ('您要的颜色是：%s' % c)
#         print(get)
#     return get_color
#
# #创建函数打印颜色
# @color
# def print_color(c):
#     print(get)
#
# print_color('c')



# 练习一 多线程文件名称查找
# 1. 对某一文件夹启动10个线程查找文件包含abc三个字符的文件名，并显示该文件所在的路径
# 2. 尽量使用面向对象编程方式实现




# 练习二 扩展练习：使用多线程编写一个简单的聊天室
# 1. 接收用户的网络连接可以使用socketserver库
# 2. 用户首次登陆输入自己的名字和当前在线的用户，支持多人同时登陆
# 3. 用户默认发的消息全部人可以收到，用户使用@某一用户可以进行私聊
#
# 提示： 服务端执行后会监听指定的端口， 客户端可以通过 nc <服务器ip地址>  <服务器端口> 方式连接， 如：
# 服务端执行 python server.py 后进行监听8000端口， 客户端执行 nc 127.0.0.1 8000 后可以连接到服务端
# 客户端A 发送消息给全体人员可以直接输入消息内容， 回车后，其他客户端可见，  客户端A发给客户端B私信可以使用
# @客户端B的名字  聊天内容，只有客户端B能够看到聊天内容
print('safa',
      'sagaf',
      'gsagag')