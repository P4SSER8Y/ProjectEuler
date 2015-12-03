from math import sqrt, floor
from itertools import count

def get(n):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
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
            return _ - 1

def run():
    ret = 0
    for n in xrange(1, 10001):
        if get(n) % 2 == 1:
            ret += 1
    return ret

if __name__ == "__main__":
    print(run())

