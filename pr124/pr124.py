#coding:utf8
from functools import reduce
from usr import getPrimes, isPrimeMR
from math import sqrt

def pr124():
    def rad(n):
        if isPrimeMR(n):
            return n
        ret = 1
        for x in primes:
            if x * 2 > n:
                break
            if n % x == 0:
                ret *= x
        return ret
    primes = getPrimes(100000)
    ret = list(range(1, 100001))
    ret.sort(key = lambda x: (rad(x), x))
    return ret[10000 - 1]

def run():
    return pr124()

if __name__ == "__main__":
    print(run())
