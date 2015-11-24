from PBar import PBar

def pr012(n):
    primes = [2]
    def primeIter():
        t = primes[-1] + 1
        while True:
            flag = False
            for x in primes:
                if t % x == 0:
                    flag = True
                    break
            if flag:
                t += 1
            else:
                break
        primes.append(t)
    def cntDivisors(n):
        lst = []
        k = 0
        while n > 1:
            if k >= len(primes):
                primeIter()
            if n % primes[k] == 0:
                cnt = 1
                while (n % primes[k] == 0):
                    cnt += 1
                    n /= primes[k]
                lst.append(cnt)
            k += 1
        return reduce(lambda x, y: x * y, lst, 1)

    pbar = PBar(maxval = n).start()
    triIndex = 0
    triNum = 0
    t = cntDivisors(triNum)
    while t < n:
        triIndex += 1
        triNum += triIndex
        t = cntDivisors(triNum)
        pbar.update(min(t, n))
    pbar.finish()
    return triNum

def run():
    return pr012(500)

if __name__ == "__main__":
    print run()

