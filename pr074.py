from PBar import PBar

def run():
    def calc(n):
        ret = 0
        while n > 0:
            ret += fac[n % 10]
            n /= 10
        return ret 
    def chain(n):
        cnt = 0
        f = set()
        while not n in f:
            f.add(n)
            n = calc(n)
        return len(f)
    fac = [1] * 10
    for i in range(1, 10):
        fac[i] = i * fac[i-1]
    cnt = 0
    pbar = PBar(1000000).start()
    for x in xrange(1, 1000000):
        pbar.update(x)
        if chain(x) == 60:
            cnt += 1
    pbar.finish()
    return cnt

if __name__ == "__main__":
    print run()
