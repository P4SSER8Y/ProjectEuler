#coding:utf8
from os import path
import re

Rchar = "IVXLCDM"
Rweight = [1, 5, 10, 50, 100, 500, 1000]
N2RDict = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL', 
        50: 'L',
        90: 'XC', 
        100: 'C', 
        400: 'CD', 
        500: 'D', 
        900: 'CM', 
        1000: 'M', }

def r2n(roman):
    t = [Rweight[Rchar.index(x)] for x in roman] + [0]
    ret = 0
    i = 0
    while (t[i] > 0):
        if (t[i] < t[i+1]):
            ret += t[i+1]-t[i]
            i += 2
        else:
            ret += t[i]
            i += 1
    return ret

def n2r(n):
    ret = ''
    while n > 0: 
        m = 0
        for x in N2RDict.keys():
            if (x > m) and (n >= x):
                m = x
        ret += N2RDict[m]
        n -= m
    return ret

def pr089():
    ret = 0

    f = open(path.split(path.realpath(__file__))[0] + '\\data089.txt', 'r')
    for s in f.readlines():
        origin = re.findall(r'[A-Z]+', s)[0]
        n = r2n(origin)
        best = n2r(n)
        ret += len(origin) - len(best)
    f.close()

    return ret

def run():
    return pr089()

if __name__ == "__main__":
    print(run())
