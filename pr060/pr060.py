#coding:utf8
from usr import getPrimes, isPrimeMR

def pr060():
    isValid = lambda a, b: isPrimeMR(int(str(a)+str(b))) and isPrimeMR(int(str(b)+str(a)))
    p = getPrimes(10000)
    pN = len(p)
    for a in xrange(pN):
        for b in xrange(a + 1, pN):
            if isValid(p[a], p[b]):
                for c in xrange(b + 1, pN):
                    if isValid(p[c], p[a]) and isValid(p[c], p[b]):
                        for d in xrange(c + 1, pN):
                            if isValid(p[d], p[a]) and isValid(p[d], p[b])\
                                and isValid(p[d], p[c]): 
                                for e in xrange(d + 1, pN):
                                    if isValid(p[e], p[d]) and isValid(p[e], p[c]) and\
                                        isValid(p[e], p[b]) and isValid(p[e], p[a]):
                                        print p[a], p[b], p[c], p[d], p[e]
                                        return p[a] + p[b] + p[c] + p[d] + p[e]

def run():
    return pr060()

if __name__ == "__main__":
    print run()

