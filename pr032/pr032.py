def pr032():
    def isValid(a, b, c):
        s = str(a) + str(b) + str(c)
        if len(s) != 9:
            return False
        return all(map(lambda c: c in s, list('123456789')))
    ret = {}
    for b in range(1111, 10000):
        for a in range(1, 10):
            if isValid(a, b, a*b):
                ret[a * b] = None
    for b in range(111, 1000):
        for a in range(11, 100):
            if isValid(a, b, a*b):
                ret[a * b] = None
    return sum(ret.keys())

def run():
    return pr032()

if __name__ == "__main__":
    print(run())

