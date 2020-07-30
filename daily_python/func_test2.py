def counter(First = 0):
    cnt = [First]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one

num5 = counter(5)
print(num5())
print(num5())
print(num5())