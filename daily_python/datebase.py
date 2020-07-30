# -*- coding:utf-8 -*-
import pymysql


# 景区开放平台测试
# config = {
#     'host':'172.29.2.3'
#     'port':'3306'
#     'user':'open_platform_qa'
#     'passwd':'92@atVPFUWAkz53K'
#     'db':'open_platform_test'
#     'charset':'utf8'
# }

# 景区管理平台测试连接数据库
connection = pymysql.connect(host='172.17.2.40',
                             port=3306,
                             user='scenic_mp_QA',
                             password='@Cb86@epMtOMjBk#',
                             db='scenic_manage_platform',
                             charset='utf8')
# 景区开放平台测试连接数据库
# connection = pymysql.connect(host='172.29.2.3',
#                              port=3306,
#                              user='open_platform_qa',
#                              password='92@atVPFUWAkz53K',
#                              db='open_platform_test',
#                              charset='utf8')

# 通过cursor创建游标

cursor = connection.cursor()

# 执行数据查询

cursor.execute('SELECT VERSION()')

# 使用fetchone()获取一条数据

data = cursor.fetchone()

print('Database version : %s'%data)
# 关闭数据连接
connection.close()
