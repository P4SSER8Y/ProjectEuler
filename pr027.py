#encoding:utf8
from PBar import PBar

def pr027():
    def primeDict(n):
        pbar = PBar(maxval=n).start()
        primeDict = {2:True}
        for k in xrange(3, n + 1, 2):
            if primeDict.get(k, True):
                pbar.update(k)
                primeDict[k] = True
                t = k + k
                while (t <= n):
                    primeDict[t] = False
                    t += k
        pbar.finish()
        return primeDict
    primeDict = primeDict(2000000)
    maxN = 0
    ret = 0
    for a in xrange(-1000, 1001):
        for b in xrange(2, 1000):
            n = 0
            while primeDict.get(n * n + a * n + b, False):
                n += 1
            n -= 1
            if n > maxN:
                maxN = n
                ret = a * b
    return ret

def run():
    return pr027()

if __name__ == "__main__":
    print run()

