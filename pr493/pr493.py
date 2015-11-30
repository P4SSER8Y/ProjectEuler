#coding:utf8
from itertools import product

def pr493():
    C = [[1, 0]]
    for i in xrange(1, 71):
        C.append([1] + [0]*(i+1))
        for j in xrange(1, i+1):
            C[i][j] = C[i-1][j-1]+C[i-1][j]
    n = 0
    """ The easiest version
    for p in product(range(11), repeat=7):
        if sum(p) == 20:
            n += len(filter(lambda x: x>0, p))\
                *reduce(lambda x,y: x*y,
                        map(lambda x: C[10][x], p))
    """
# The fastest version
    for a in xrange(0, 11):
        for b in xrange(0, 11):
            for c in xrange(0, 11):
                if (a+b+c<=20):
                    for d in xrange(0, 11):
                        if (a+b+c+d<=20):
                            for e in xrange(0, 11):
                                if (a+b+c+d+e<=20):
                                    for f in xrange(0, 11):
                                        g = 20-a-b-c-d-e-f
                                        if (0 <= g) and (g <= 10):
                                            n += len(filter(lambda x: x>0,
                                                            [a,b,c,d,e,f,g]))\
                                                *reduce(lambda x,y: x*y,
                                                        map(lambda x: C[10][x],
                                                            [a,b,c,d,e,f,g]))
    return float(n) / float(C[70][20])

def run():
    return pr493()

if __name__ == "__main__":
    print run()

