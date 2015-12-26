#coding:utf8
from math import sqrt

def isValid(g):
    head = str(g[1])[:10]
    tail = str(g[2])[-9:]
    for c in '123456789':
        if (not c in head) or (not c in tail):
            return False
    return True

def pr104():
    MOD = int(1e12)
    def fibGen():
        phi = (1 + sqrt(5)) / 2
        a = 1
        b = 1
        f = phi / sqrt(5)
        n = 1
        yield n, f, a
        while True:
            n += 1
            a, b = b, (a + b) % MOD
            f *= phi
            while f >= 10:
                f /= 10
            yield n, f, a
    fib = fibGen()
    while next(fib)[2] < 1e8: pass
    g = next(fib)
    while not isValid(g):
        g = next(fib)
    return g[0]
        
def run():
    return pr104()

if __name__ == "__main__":
    print(run())

