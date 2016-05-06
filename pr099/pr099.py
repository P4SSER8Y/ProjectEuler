#coding:utf8
from __future__ import division
from os.path import realpath, split, sep 
from math import log

class SuperFloat(object):
    def __init__(self, s = 0.0, e = 0):
        while s >= 10:
            s /= 10.0
            e += 1
        self.s = s
        self.e = e

    def __mul__(self, other):
        return SuperFloat(self.s * other.s, self.e + other.e)

    def __str__(self):
        return str(self.s)+'e'+str(self.e)

    def __gt__(self, other):
        return (self.e > other.e) or ((self.e == other.e) and (self.s > self.s))

def superPow(a, b):
    if b == 0:
        return SuperFloat(1)
    if b & 1 == 0:
        return superPow(a * a, b >> 1)
    else:
        return superPow(a * a, b >> 1) * a

def pr099():
    f = open(split(realpath(__file__))[0] + sep + 'data099.txt')
    maxN = 0
    maxK = 0
    k = 0
    for x in f.readlines():
        k += 1
        t = x.split(',')
        a = int(t[0])
        b = int(t[1])
        n = b * log(a)
        if n > maxN:
            maxN = n
            maxK = k
    return maxK
    f.close()

def run():
    return pr099()

if __name__ == "__main__":
    print(run())

