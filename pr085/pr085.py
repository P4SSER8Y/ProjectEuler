#coding:utf8
from math import sqrt

def pr085():
    calc = lambda x, y: x * y * (x - 1) * (y - 1) / 4
    closest = 0
    closestA = 0
    closestB = 0
    for x in xrange(1, 2 * int(sqrt(sqrt(2000000*4)))):
        for y in xrange(1, 2 * int(sqrt(sqrt(2000000*4)))):
            if abs(closest - 2000000) > abs(closest - calc(x, y)):
                closest = calc(x, y)
                closestA = x - 1
                closestB = y - 1
    return closestA*closestB

def run():
    return pr085()

if __name__ == "__main__":
    print run()

