from threading import Thread,current_thread
import time,random
from queue import Queue

queue = Queue(5)

class Produce_thread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('生产者 %s 生产了数据 %s'%(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print('生产者 %s 睡眠了 %s' % (name, t))



class Consumer_thread(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者 %s 消耗了数据 %s'%(name,num))
            t = random.randint(1,3)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s s' % (name, t))


p1 = Produce_thread(name = '一号生产者')
p1.start()
p2 = Produce_thread(name = '二号生产者')
p2.start()

c1 = Consumer_thread(name = '一号消费者')
c1.start()
c2 = Consumer_thread(name = '一号消费者')
c2.start()

