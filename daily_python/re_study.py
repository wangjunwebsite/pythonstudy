'''
1.文字处理  re  正则表达式的缩写
2.日期类型的 time 、datetime
3.数字和数字类型的 math random
4.文件和目录访问的  pathlib os path
5.数据压缩和归档的 tarfile
6.通用操作系统的 os 、logging 、 argparse
7.多线程的 threading 、 queue
8.Internet数据处理的 base64 、 json 、 urllib
9.结构化标记处理工具的 html 、 xml
10.开发工具的 unitest
11.调试工具的 timeit
12.软件包发布的venv
13.运行服务的 _main_

'''

import re

# 正则表达式的元字符
'''
.   匹配任意的单个字符，可以用多个
p = re.compile('.')
print(p.match('b'))

^   从开头进行搜索
p = re.compile('^')
print(p.match(''))

$   从后边向前边进行匹配
p = re.compile('jpg$')
print(p.match('')

*   匹配前面的字符出现0次-多次
p = re.compile('ca*t')
print(p.match('ct')

+   前面的字符出现一次或多次

？   表示字符出现0次-1次

{m}  表示前面的字符出现m次
{m,n}  表示前面的字符出现m到n次
p = re.compile('ca{4}t')
print(p.match('caaaat')

[] 表示[]中任意一个字符串匹配成功就匹配成功
p = re.compile('c[bcd]t')

|  表示选择左边或者右边

\d 表示匹配的内容是一串数字，也可用[0-9]+
\D 表示匹配的内容不包含数字
\s 表示匹配的是一串字符串
() 表示进行分组
^$ 表示这一行为空行
.*? 不使用贪婪模式：
'''

# p = re.compile('.{3}')
# print(p.match('bag'))
p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2018-04-12').group(1,2,3))
# print(p.match('2018-04-12').groups())
#
# year,month,day = p.match('2018-04-12').groups()
# print(year,month,day)

# match & search
print(p.search('ssa2018-04-12jj'))

# sub函数 进行字符串的替换 sub('c','*','abc') abc中c替换成*
phone = '123-456-789 #电话号码'
p2 = re.sub(r'#.*$','',phone)
p3 = re.sub(r'-','',phone)
p4 = re.sub(r'\D','',phone)
print(p2,p3,p4)

#findall 匹配多次