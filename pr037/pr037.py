from usr import getPrimes

def pr037():
    def pIter():
        k = 9
        while True:
            if pDict.get(k, False):
                yield k
            k += 2
    def genPrime(n):
        k = 3
        while k <= n:
            while not pDict.get(k, True): k += 2
            if k > n : break
            pDict[k] = True
            t = k * 2
            while t <= n:
                pDict[t] = False
                t += k
            k += 2
    def isVaild(x):
        t = x // 10
        while t > 0:
            if not pDict.get(t):
                return False
            t //= 10
        t = str(x)[1:]
        while t:
            if not pDict.get(int(t)):
                return False
            t = t[1:]
        return True
    pDict = dict.fromkeys(getPrimes(2000000), True)
    ret = []
    prime = pIter()
    for _ in range(11):
        p = next(prime)
        while not isVaild(p):
            p = next(prime)
        ret.append(p)
    return sum(ret)

def run():
    return pr037()

if __name__ == "__main__":
    print(run())

