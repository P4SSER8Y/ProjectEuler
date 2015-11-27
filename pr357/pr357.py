#coding:utf8
from math import sqrt
from usr import getPrimes
from PBar import PBar

def pr357(n):
    ret = 3
    primes = set(getPrimes(2*n))
    pbar = PBar(n).start()
    for x in xrange(3, n + 1):
        if not x in primes:
            pbar.update(x)
            flag = True
            for y in xrange(1, int(sqrt(x))+1):
                if (x % y == 0):
                    if not (y + x / y) in primes:
                        flag = False
                        break
            if flag:
                ret += x
    pbar.finish()
    return ret 

def run():
    return pr357(100000000)

if __name__ == "__main__":
    print run()

