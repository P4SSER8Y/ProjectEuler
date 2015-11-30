#coding:utf8
from math import log
from itertools import count

def getSum(n):
    ret = 0
    while n:
        ret += n % 10
        n /= 10
    return ret

def pr119():
    num = []
    for x in xrange(1, 100):
        for y in xrange(0, 15):
            n = x ** y
            if getSum(n) == x:
                num.append(n)
    num = [x for x in num if x >= 10]
    num.sort()
    return num[29]

def run():
    return pr119()

if __name__ == "__main__":
    print run()

