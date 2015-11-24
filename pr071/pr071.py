#coding:utf8
from fractions import Fraction
from PBar import PBar

def pr071():
    base = Fraction(3, 7)
    ret = Fraction(0, 1)
    pbar = PBar(int(1e6)+1).start()
    for d in xrange(3, int(1e6) + 1):
        pbar.update(d)
        n = int(3.0/7*d)
        t1 = Fraction(n, d)
        if (t1 < base) and (t1 > ret):
            ret = t1
    pbar.finish()
    return ret.numerator

def run():
    return pr071()

if __name__ == "__main__":
    print run()

