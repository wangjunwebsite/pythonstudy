def tips1(argv):
    def tips(func):
        def nei(a, b):
            print('start%s' % argv)
            func(a, b)
            print('end')
        return nei
    return tips


@tips1('add')
def add(a, b):
    print(a + b)


@tips1('del')
def sub(a, b):
    print(a - b)


print(add(4, 6))
print(sub(4, 5))
