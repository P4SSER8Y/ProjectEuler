def run():
    def chainIter(n):
        if d.get(n, False):
            return d[n]
        s = 0
        t = n
        while t > 0:
            s += (t % 10) ** 2
            t //= 10
        d[n] = chainIter(s)
        return d[n]
    d = {1:1, 89:89}
    cnt = 0
    for x in range(1, 10000000):
        if chainIter(x) == 89:
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(run())

