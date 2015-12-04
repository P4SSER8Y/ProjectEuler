#coding:utf8
from usr import getPrimes
from itertools import count
from math import log, floor

def pr347(N): 
    primes = getPrimes(N)
    ret = 0
    for i in range(len(primes) - 1):
        p = primes[i]
        j = i + 1
        while p * primes[j] <= N:
            pn = p
            M = 0
            while pn < N:
                t = int(log(float(N)/pn) / log(primes[j]))
                if not t:
                    break
                if (pn * (primes[j] ** t) > M):
                    M = pn * (primes[j] ** t)
                pn *= p 
            ret += M
            j += 1
    return ret

def run():
    return pr347(10000000)

if __name__ == "__main__":
    print(run())

