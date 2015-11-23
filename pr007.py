from PBar import PBar

def pr007(n):
    pbar = PBar(maxval=n).start()
    def primeIter():
        primes = []
        k = 2
        while True:
            flag = True
            for x in primes:
                if k % x == 0:
                    flag = False
                    break
            if flag:
                primes.append(k)
                yield k
            k += 1
    prime = primeIter()
    for _ in xrange(n):
        pbar.update(_)
        p = prime.next()
    pbar.finish()
    return p

def run():
    return pr007(10001)

if __name__ == "__main__":
    print run()

