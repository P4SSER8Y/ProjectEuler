def pr039():
    ret = [0] * 1001
    for a in xrange(1, 1000):
        for b in xrange(1, 1000):
            c = int((a * a + b * b) ** 0.5)
            if (a * a + b * b == c * c) and (a + b + c <= 1000):
                ret[a + b + c] += 1
    return ret.index(max(ret))

def run():
    return pr039()

if __name__ == "__main__":
    print run()

