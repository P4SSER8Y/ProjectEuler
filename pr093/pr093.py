#coding:utf8
from itertools import permutations, count, combinations, product
from operator import add, sub, mul, truediv
from math import fabs

def foo(a, b, c, d):
    isInt = lambda x: fabs(x - int(x)) <= 0.00000001
    ans = set()
    for p in permutations((a, b, c, d)):
        for op in product((add, sub, mul, truediv), repeat=3):
            t = op[2](op[1](op[0](p[0], p[1]), p[2]), p[3])
            if isInt(t) and (t > 0):
                ans.add(int(t))
            t = op[2](op[0](p[0], p[1]), op[1](p[2], p[3]))
            if isInt(t) and (t > 0):
                ans.add(int(t))
    for k in count(1):
        if not k in ans:
            return k - 1

def pr093():
    maxN = 0
    ret = ''
    for p in combinations(range(1, 10), 4):
        t = foo(*p)
        if t > maxN:
            maxN = t
            ret = p
    return reduce(lambda x, y: x * 10 + y, ret)
 
def run():
    return pr093()

if __name__ == "__main__":
    print(run())

