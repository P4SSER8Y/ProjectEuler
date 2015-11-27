#coding:utf8
def isPrimeMR(n):
    def powMod(a, d, n):
        if d == 0:
            return 1
        if d == 1:
            return (a % n)
        if d & 1 == 0:
            return powMod(a * a % n, d >> 1, n) % n
        else:
            return (powMod(a * a % n, d >> 1, n) * a % n)
    def WITNESS(a):
        if n == 2:
            return True
        if (n == 1) or (n & 1 == 0):
            return False
        d = n - 1
        while (d & 1 == 0):
            d >>= 1
        t = powMod(a, d, n)
        while ((d != n - 1) and (t != 1) and (t != n - 1)):
            t = (t * t) % n
            d <<= 1
        return ((t == n - 1) or (d & 1 == 1))
    foo = [2, 3, 7, 11, 61, 24251]
    for a in foo:
        if a < n:
            if not WITNESS(a):
                return False
    return True

def pr387(maxN):
    def isHarshad(n):
        t = n
        s = 0
        while t:
            s += t % 10
            t /= 10
        return (n % s == 0)
    def isStrongHarshad(n):
        t = n
        s = 0
        while t:
            s += t % 10
            t /= 10
        return isPrimeMR(n / s)
    def iter(n):
        if n >= maxN:
            return
        for x in xrange(10):
            if isHarshad(n*10+x):
                if isStrongHarshad(n*10+x):
                    for y in xrange(1, 10, 2):
                        if n*100+x*10+y >= maxN:
                            break
                        if isPrimeMR(n*100+x*10+y):
                            ret.append(n*100+x*10+y)
                iter(n*10+x)
    ret = []
    for x in xrange(1, 10):
        iter(x)
    return sum(ret)

def run():
    return pr387(int(1e14))

if __name__ == "__main__":
    print run()

