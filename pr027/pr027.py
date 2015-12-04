#encoding:utf8

def pr027():
    def primeDict(n):
        primeDict = {2:True}
        for k in range(3, n + 1, 2):
            if primeDict.get(k, True):
                primeDict[k] = True
                t = k + k
                while (t <= n):
                    primeDict[t] = False
                    t += k
        return primeDict
    primeDict = primeDict(2000000)
    maxN = 0
    ret = 0
    for a in range(-1000, 1001):
        for b in range(2, 1000):
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
    print(run())

