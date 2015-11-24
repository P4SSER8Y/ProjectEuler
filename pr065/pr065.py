from fractions import Fraction
from itertools import count

def eConvergents(n):
    def gen():
        yield 2
        for k in count(1):
            yield 1
            yield 2*k
            yield 1
    tmp = gen()
    lst = [tmp.next() for _ in range(n)]
    lst.reverse()
    ret = Fraction(lst[0], 1)
    for x in lst[1:]:
        ret = x + 1/ret
    return ret

def run():
    n = eConvergents(100).numerator
    ret = 0
    while n:
        ret += n % 10
        n /= 10
    return ret

if __name__ == "__main__":
    print run()
