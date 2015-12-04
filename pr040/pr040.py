from PBar import PBar

def pr040():
    def iter():
        k = 0
        while True:
            k += 1
            for c in str(k):
                yield int(c)
    i = iter()
    ret = 1
    for _ in range(1, 1000001):
        d = next(i)
        if _ in [1, 10, 100, 1000, 10000, 100000, 1000000]:
            ret *= d
    return ret 

def run():
    return pr040()

if __name__ == "__main__":
    print(run())

