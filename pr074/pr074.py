def run():
    def calc(n):
        ret = 0
        while n > 0:
            ret += fac[n % 10]
            n //= 10
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
    for x in range(1, 1000000):
        if chain(x) == 60:
            cnt += 1
    return cnt

if __name__ == "__main__":
    print(run())
