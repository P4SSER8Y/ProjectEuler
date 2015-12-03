import itertools
from operator import add, sub
from math import sqrt, fabs
from PBar import PBar

def pr044(limit):
    pentagon = set(n*(3*n-1)/2 for n in range(1, limit))
    isPentagon = lambda x: x in pentagon
    cp = itertools.combinations(pentagon, 2)
    for x in cp:
        if isPentagon(add(*x)) and isPentagon(abs(sub(*x))):
            return abs(sub(*x))
    return "Not Found"

def run():
    return pr044(3000)

if __name__ == "__main__":
    print(run())

