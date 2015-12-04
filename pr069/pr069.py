from usr import getPrimes

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
                    n //= x
                ret *= (x**(k-1))*(x-1)
        return ret
    maxPhi = 0
    maxN = 0
    primes = getPrimes(n+1)
    for i in range(2, n+1):
        t = float(i) / phi(i)
        if t > maxPhi:
            maxPhi = t
            maxN = i
    return maxN

def run():
    return pr069(1000000)

if __name__ == "__main__":
    print(run())
