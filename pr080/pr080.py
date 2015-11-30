#coding:utf8
from math import sqrt, fabs

def pr080():
    def superSqrt(n):
        yield int(sqrt(n))
        x = int(sqrt(n))
        r = n - (int(sqrt(n)))**2
        while r:
            r *= 100
            for t in xrange(9, -1, -1):
                if (20*x+t)*t < r:
                    break
            r -= (20*x+t)*t
            x = x * 10 + t
            yield t
    def isInt(n):
        return fabs(int(n) - n) < 0.00001
    ret = 0
    for n in xrange(100):
        if not isInt(sqrt(n)):
            iter = superSqrt(n)
            for _ in xrange(100): 
                ret += iter.next()
    return ret

def run():
    return pr080()

if __name__ == "__main__":
    print run()

