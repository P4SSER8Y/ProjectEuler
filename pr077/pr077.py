#coding:utf8
from usr import getPrimes

def pr077():
    N = 80
    primes = getPrimes(N) 
    f = [0] * N
    f[0] = 1
    for x in primes:
        for i in range(len(f)):
            if i + x >= N:
                break
            if f[i]:
                f[i + x] += f[i]
    for i in range(len(f)):
        if f[i] > 5000:
            return i

def run():
    return pr077()

if __name__ == "__main__":
    print(run())
