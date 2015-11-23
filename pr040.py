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
    pbar = PBar(maxval = 1000000).start()
    for _ in xrange(1, 1000001):
        pbar.update(_)
        d = i.next()
        if _ in [1, 10, 100, 1000, 10000, 100000, 1000000]:
            ret *= d
    pbar.finish()
    return ret 

def run():
    return pr040()

if __name__ == "__main__":
    print run()

