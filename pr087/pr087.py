from usr import getPrimes
from math import sqrt

def pr087(n):
    primes = getPrimes(int(sqrt(n))+1)
    p2 = set()
    for k in primes:
        if k ** 2 <= n:
            p2.add(k**2)
    p3 = set()
    for k in primes:
        for x in p2:
            if k ** 3 + x <= n:
                p3.add(k**3+x)
    p4 = set()
    for k in primes:
        for x in p3:
            if k ** 4 + x <= n:
                p4.add(k**4+x)
    return len(filter(lambda x: x<=n, p4))

def run():
    return pr087(50000000)

if __name__ == "__main__":
    print(run())
