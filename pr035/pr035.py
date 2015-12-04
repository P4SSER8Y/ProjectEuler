from usr import getPrimes

def pr035(n):
    def isCircularPrime(k):
        k = str(k)
        lst = [int((k[i:] + k[:i])) for i in range(len(k))]
        return all(map(lambda x: x in primes, lst))
    primes = set(getPrimes(n))
    circularPrimes = [2]
    for k in range(3, n + 1, 2):
        if (k in primes) and isCircularPrime(k):
            circularPrimes.append(k)
    return len(circularPrimes)

def run():
    return pr035(1000000)

if __name__ == "__main__":
    print(run())


