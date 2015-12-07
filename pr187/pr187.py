#coding:utf8
from usr import getPrimes

def pr187(n):
    primes = getPrimes(n)
    i = 0
    j = len(primes) - 1
    while primes[i] * primes[j] >= n:
        j -= 1
    ret = 0
    while i <= j:
        ret += j - i + 1
        i += 1
        while primes[i] * primes[j] >= n:
            j -= 1 
    return ret

def run():
    return pr187(int(1e8))

if __name__ == "__main__":
    print(run())
