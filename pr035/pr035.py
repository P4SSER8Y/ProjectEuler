from PBar import PBar

def pr035(n):
    def genPrimeDict():
        print("===Generate Prime Number Dict===")
        pbar = PBar(maxval=n).start()
        pLst = {2:True}
        k = 3
        while k <= n:
            pbar.update(k)
            while (k <= n) and (not pLst.get(k, True)): k += 2
            if k > n:
                break
            pLst[k] = True
            t = k * 2
            while t <= n:
                pLst[t] = False
                t += k
            k += 2
        pbar.finish()
        return pLst
    def isCircularPrime(k):
        k = str(k)
        lst = [int((k[i:] + k[:i])) for i in range(len(k))]
        return all(map(lambda x:pDict.get(x, False), lst))
    pDict = genPrimeDict()
    circularPrimes = [2]
    print("===Checking===")
    pbar = PBar(maxval = n).start()
    for k in xrange(3, n + 1, 2):
        pbar.update(k)
        if pDict[k] and isCircularPrime(k):
            circularPrimes.append(k)
    pbar.finish()
    return len(circularPrimes)

def run():
    return pr035(1000000)

if __name__ == "__main__":
    print(run())


