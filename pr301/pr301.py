#coding:utf8
from itertools import ifilter

def pr301():
    ret = 0
    for n in xrange(1, 2**30+1):
        if (n ^ (2*n) ^ (3*n)) == 0:
            ret += 1
    return ret

def run():
    return pr301()

if __name__ == "__main__":
    print run()
