from fractions import Fraction as F
def pr033():
    ret = []
    for x in xrange(1, 10):
        for a in xrange(1, 10):
            for b in xrange(1, 10):
                t = [F(x*10+a, x*10+b), F(x*10+a, b*10+x), F(a*10+x, x*10+b), F(a*10+x, b*10+x)]
                ret += [y for y in t if (y == F(a, b)) and (y < 1)]
    return str(reduce(lambda x, y: x * y, ret, F(1, 1)))

def run():
    return pr033()

if __name__ == "__main__":
    print(run())

