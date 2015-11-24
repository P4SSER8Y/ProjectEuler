from usr import getPrimes
from PBar import PBar

def pr069(n):
    def phi(n):
        ret = 1
        for x in primes:
            if x > n:
                break
            if n % x == 0:
                k = 0
                while (n % x == 0):
                    k += 1
                    n /= x
                ret *= (x**(k-1))*(x-1)
        return ret
    maxPhi = 0
    maxN = 0
    primes = getPrimes(n+1)
    pbar = PBar(n).start()
    for i in xrange(2, n+1):
        pbar.update(i)
        t = float(i) / phi(i)
        if t > maxPhi:
            maxPhi = t
            maxN = i
    pbar.finish()
    return maxN, maxPhi

def run():
    return pr069(1000000)

if __name__ == "__main__":
    print run()
