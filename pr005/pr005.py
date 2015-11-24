def pr005(n):
    def primeIter():
        primes = []
        k = 2
        while True:
            if all(map(lambda x: k % x != 0, primes)):
                primes.append(k)
                yield k
            k += 1
    num = range(1, n+1)
    fac = []
    prime = primeIter()
    p = prime.next()
    while max(num) >= p:
        while 2 <= sum(map(lambda x: {False: 0, True: 1}[x % p == 0], num)):
            fac.append(p)
            for i in range(len(num)):
                if num[i] % p == 0:
                    num[i] = num[i] / p
        p = prime.next()
    return reduce(lambda x, y: x * y, num + fac, 1)

def run():
    return pr005(20)

if __name__ == "__main__":
    print run()

