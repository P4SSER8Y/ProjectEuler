#coding:utf8
from usr import getPrimes
from itertools import count

def pr123(exceed):
    def powerMod(b, e, m):
        if e == 0:
            return 1
        if e == 1:
            return b % m
        if (e & 1 == 0):
            return powerMod(b * b % m, e >> 1, m)
        else:
            return (powerMod(b * b % m, e >> 1, m) * b) % m
    primes = getPrimes(int(1e6))
    t = int(exceed**0.5)
    for n in count(0):
        if primes[n] >= t:
            break
    while True:
        p = primes[n]
        m = p * p
        if (powerMod(p-1, n+1, m) + powerMod(p+1, n+1, m)) % m >= exceed:
            return n+1
        n += 1
    return "FAILED"

def run():
    return pr123(int(1e10))

if __name__ == "__main__":
    print run()

