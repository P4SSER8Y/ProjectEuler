from usr import getPrimes
from math import sqrt

def isValid(a, b):
    if len(str(a)) != len(str(b)):
        return False
    a = ''.join(sorted(str(a)))
    b = ''.join(sorted(str(b)))
    return a == b

def pr070(n):
    primes_1 = getPrimes(int(sqrt(n)))
    primes_2 = getPrimes(n/2)

    minValue = 2147483647
    minN = 0
    for x in primes_1:
        for y in primes_2:
            if x * y > n:
                break
            phi = (x - 1) * (y - 1)
            if isValid(x*y, phi) and float(x*y)/float(phi) < minValue:
                minN = x * y
                minValue = float(x*y)/phi 
    return minN 

def run():
    return pr070(int(1e7))

if __name__ == "__main__":
    print(run())
