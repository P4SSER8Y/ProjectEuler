#coding:utf8
from fractions import Fraction

def foo(turn, red, blue, blueCnt, redCnt):
    if turn == 0:
        if blueCnt > redCnt:
            return Fraction(1, 1)
        else:
            return Fraction(0, 1)
    return foo(turn - 1, red + 1, blue, blueCnt, redCnt + 1) * Fraction(red, red + blue) +\
           foo(turn - 1, red + 1, blue, blueCnt + 1, redCnt) * Fraction(blue, red + blue)

def pr121():
    winProb = foo(15, 1, 1, 0, 0)
    return winProb.denominator // winProb.numerator

def run():
    return pr121()

if __name__ == "__main__":
    print(run())
