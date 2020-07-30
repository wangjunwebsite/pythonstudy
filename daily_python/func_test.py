#迭代
#iter()   next()

# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#yield生产器迭代

# def frange(start,end,step):
#     i = start
#     while i < end:
#         yield(i)
#         i += step
#
# for i in frange(10,20,0.5):
#     print(i)


# lambda表达式s
fun = (lambda x,y:x+y)
print(fun(1,2))

sum = lambda a_num:a_num+1
print(sum(5))