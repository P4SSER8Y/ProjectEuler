from fractions import Fraction
def run():
    Peter = [a+b+c+d+e+f+g+h+i
         for a in range(1, 5)
         for b in range(1, 5)
         for c in range(1, 5)
         for d in range(1, 5)
         for e in range(1, 5)
         for f in range(1, 5)
         for g in range(1, 5)
         for h in range(1, 5)
         for i in range(1, 5)]
    Colin = [a+b+c+d+e+f
         for a in range(1, 7)
         for b in range(1, 7)
         for c in range(1, 7)
         for d in range(1, 7)
         for e in range(1, 7)
         for f in range(1, 7)]
    sPeter = {}
    sColin = {}
    for x in Peter: sPeter[x] = sPeter.get(x, 0) + 1
    for x in Colin: sColin[x] = sColin.get(x, 0) + 1
    for x in sPeter.keys(): sPeter[x] = Fraction(sPeter[x], len(Peter))
    for x in sColin.keys(): sColin[x] = Fraction(sColin[x], len(Colin))
    ret = 0
    for p in sPeter.keys():
        for c in sColin.keys():
            if p > c:
                ret += sPeter[p] * sColin[c]
    return "{:0.7f}".format(float(ret))

if __name__ == "__main__":
    print(run())

