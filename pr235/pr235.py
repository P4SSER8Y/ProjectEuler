#coding:utf8
from math import fabs, pow

def s(r, n):
    ret = 0.0
    for k in range(1, n + 1):
        ret += (900 - 3*k)*pow(r, k - 1)
    return ret

def pr235():
    delta = 1e-12
    isFinished = lambda a, b: fabs(a - b) < delta
    n = 5000
    l = 1.0 
    r = 1.1
    while not isFinished(l, r):
        m = (l + r) / 2.0
        if s(m, n) > -600000000000.0:
            l = m
        else:
            r = m
    return format(l, ".12f")

def run():
    return pr235()

if __name__ == "__main__":
    print(run())
