from math import sqrt, fabs, floor
from itertools import count, cycle
from fractions import Fraction

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def get(n):
    if n == (int(sqrt(n)))**2:
        return 0
    an = lambda k, c, d: int(floor(((k*sqrt(n)-c)/d)))
    pn = lambda k, c, d: [d*k,
                          -d*(c+d*an(k,c,d)),
                          k*k*n-(c+d*an(k,c,d))**2]
    a = [0]
    p = [[1, 0, 1]]
    a.append(an(*p[-1]))
    t = pn(*p[-1])
    g = gcd(gcd(t[0], t[1]), t[2])
    p.append([t[0]/g, t[1]/g, t[2]/g])
    for _ in count(2):
        a.append(an(*p[-1]))
        t = pn(*p[-1])
        g = gcd(gcd(t[0], t[1]), t[2])
        p.append([t[0]/g, t[1]/g, t[2]/g])
        if p[-1] == p[1]:
            return a[1:]

def getConFrac(n):
    def iter():
        yield fra[0]
        for _ in cycle(fra[1:]):
            yield _
    fra = get(n)
    yield fra[0], 1
    for x in count(2):
        t = iter()
        lst = [t.next() for _ in xrange(x)]
        lst.reverse()
        f = reduce(lambda x, y: y + 1/x, lst[1:], Fraction(lst[0], 1))
        yield f.numerator, f.denominator

def pr066(n):
    def isInt(n):
        return fabs(floor(n) - n) <= 1e-7
    maxD = 0
    maxX = 0
    for D in xrange(n+1):
        if not isInt(sqrt(D)):
            f = getConFrac(D)
            x, y = f.next()
            while x*x-D*y*y != 1:
                x, y = f.next()
            if x > maxX:
                maxX = x
                maxD = D
    return maxD

def run():
    return pr066(1000)

if __name__ == "__main__":
    print(run())

