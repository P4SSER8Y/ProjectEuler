#coding:utf8
from usr import getPrimes

def pr249():
    m = int(1e16)
    primes = getPrimes(5000)
    maxSum = sum(primes)
    f = [0] * (maxSum + 1)
    f[0] = 1
    g = [0] * (maxSum + 1)
    currSum = 0
    for x in primes:
        for i in range(currSum + 1):
            if f[i]:
                g[i+x] += f[i]
        currSum += x
        for i in range(currSum + 1):
            f[i] = (f[i] + g[i]) % m
            g[i] = 0
    ret = 0
    for x in getPrimes(maxSum):
        ret += f[x]
    return ret % m

def run():
    return pr249()

if __name__ == "__main__":
    print(run())
