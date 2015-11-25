#coding:utf8

def pr091(n):
    isValid = lambda a, b, c: (a + b == c) or (a + c == b) or (b + c == a)
    ret = 0
    for x1 in xrange(n + 1):
        for y1 in xrange(n + 1):
            for x2 in xrange(n + 1):
                for y2 in xrange(n + 1):
                    if (x1*y2 != x2*y1)\
                       and isValid((x1-x2)**2+(y1-y2)**2, x1**2+y1**2, x2**2+y2**2):
                           ret += 1
    return ret >> 1

def run():
    return pr091(50)

if __name__ == "__main__":
    print run()

