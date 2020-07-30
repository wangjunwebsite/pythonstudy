# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 100}
#
#
# def print_role(role_name):
#     print('name is %s ,hp is %s' % (role_name['name'], role_name['hp']))
#
#
# print_role(user1)
# print_role(user2)


# 定义一个类为Player,规范为类第一个字母大写
class Player():
    def __init__(self, name, hp, occu):
        self.name = name
        self.hp = hp
        self.occu = occu
        #类的属性不想被访问可以在前面加两个下划线：__,类的封装
    def print_role(self):  # 定义一个方法
        print('%s : %s : %s' % (self.name, self.hp, self.occu))

    def update_name(self,newname):
        self.name = newname

class Master:

    def __init__(self,hp=100):
        self.hp = hp
        print('怪物的hp:%s'%hp)
    def run(self):
        print('怪物移动了一下')

class Animal(Master):
    def __init__(self,hp=100):
        super().__init__(hp)
class Boss(Master):
    def __init__(self, hp=1000):
        super().__init__(hp)
    def word(self):
        print('说道：人类你终于来了')


# user1 = Player('tom', 100, 'war')  # 类的实例化
# user2 = Player('jerry', 100, 'shhhf')
# user1.print_role()
# user2.print_role()
#
# user1.update_name('sdf')
# user1.print_role()
user1 = Master(100)
user1.run()

user2 = Animal(10)
user2.run()

user3 = Boss(800)
user3.word()


print('user1的类型是%s'%type(user1))
print('user2的类型是%s'%type(user2))
print('user3的类型是%s'%type(user3))

print(isinstance(user1,Master))
