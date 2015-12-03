from fractions import Fraction
def run():
    cnt = 0
    s = Fraction(1, 1)
    for _ in range(1000):
        s = 1 + 1 / (1 + s)
        if len(str(s.numerator)) > len(str(s.denominator)):
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(run())
