import time

print(time.time())

def timer(func):
    def warpper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数运行了%s秒' % (end_time - start_time))
    return warpper()

@timer
def i_can_sleep():
    time.sleep(3)

# start_time = time.time()
# i_can_slepp()
# end_time = time.time()
# print('函数运行了%s秒'%(end_time-start_time))