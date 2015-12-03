from PBar import PBar

def pr021(n):
    def getD(n):
        if d.get(n, 0) > 0:
            return d[n]
        d[n] = sum([x for x in range(1, n) if n % x == 0])
        return d[n]
    def isAmicable(n):
        return (n == getD(getD(n))) and (n != getD(n))
    d = {1:1}
    ret = 0
    pbar = PBar(maxval = n).start()
    for k in range(1, n + 1):
        pbar.update(k)
        if isAmicable(k):
            ret += k
    pbar.finish()
    return ret

def run():
    return pr021(10000)

if __name__ == "__main__":
    print(run())

