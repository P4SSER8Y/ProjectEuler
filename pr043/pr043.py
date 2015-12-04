def pr043():
    def fix(x):
        for c in '123456789':
            if not c in str(x):
                return int(c + str(x))
    def isPandigital(x):
        for c in '0123456789':
            if not c in str(x):
                return False
        return True
    def isValid(x):
        y = str(x)
        t = zip(range(1, 8), [2, 3, 5, 7, 11, 13, 17])
        return all(map(lambda t: int(y[t[0]:t[0] + 3]) % t[1] == 0, t))
    ret = 0
    for x in range(1, 500):
        for y in range(1, 1000 // 7):
            for z in range(1, 1000 // 17):
                t = fix(2 * x * 1000000 + 7 * y * 1000 + 17 * z)
                if isPandigital(t) and isValid(t):
                    ret += t
    return ret

def run():
    return pr043()

if __name__ == "__main__":
    print(run())

