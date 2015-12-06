#coding:utf8
from usr import getPrimes, isPrimeMR
from PBar import PBar

def pr214():
    def phi(n):
        if isPrimeMR(n):
            return n - 1
        ret = n
        for x in primes:
            if x << 1 > n:
                break
            if n % x == 0:
                ret = ret // x * (x - 1)
        return ret
    def getChainLen(n): 
        if d[n]:
            return d[n]
        t = getChainLen(phi(n)) + 1
        d[n] = t
        return t 
    primes = getPrimes(40000000)
    d = [0] * 40000000
    d[0] = 1
    d[1] = 1
    ret = 0
    pbar = PBar(40000000).start()
    for x in primes:
        pbar.update(x)
        if getChainLen(x) == 25:
            ret += x
    pbar.finish()
    return ret 

def run():
    return pr214()

if __name__ == "__main__":
    print(run())
