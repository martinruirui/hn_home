#encoding=utf8
import random

l1 = []

while len(l1) < 100000:
    l1.append(random.randrange(-10000000, 1000000))

def timer(fn, *args):
    import time
    start = time.clock()
    return fn(*args), time.clock() - start

def find():
    '''
    add your code
    '''
    nums = dict((k,k) for k in l1)
    negative_nums = [n for n in l1 if n < 0]
    positive_nums = [nums.get(abs(n), '') for n in negative_nums if nums.get(abs(n))]
    return len(positive_nums)

if __name__ == '__main__':
    print timer(find)


