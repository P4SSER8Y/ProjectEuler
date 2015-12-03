def powerMod(base, N, m):
    ret = 1
    for _ in xrange(N):
        ret = (ret * base) % m
    return ret

def run():
    ret = 0
    for x in xrange(1, 1001):
        ret = (ret + powerMod(x, x, int(1e10))) % int(1e10)
    return ret

if __name__ == "__main__":
    print(run())

