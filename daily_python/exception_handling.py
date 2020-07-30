#测试error类型

# a = j   #NameError

# try:
#     a = j
# except NameError as b :
#     print(b)


# a = {'a':'b','b':65}
# print(a['c'])   KeyError


# try:
#     a = {'a': 'b', 'b': 65}
#     print(a['c'])
# except KeyError :
#     print('fsafsafa')



try:
    a = open('name.txt',encoding='utf-8')
except Exception as d:
    print(d)
finally:
    print(a.read(3))
    a.close()