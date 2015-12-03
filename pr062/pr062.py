#coding:utf8

def pr062():
    def count(n):
        tmp = [0] * 10
        while n:
            tmp[n % 10] += 1
            n /= 10
        return tuple(tmp)

    minValue = {}
    cnt = {}
    for x in xrange(int(1e4)):
        tmp = count(x ** 3)
        minValue[tmp] = min(minValue.get(tmp, float("Inf")), x ** 3)
        cnt[tmp] = cnt.get(tmp, 0) + 1
    for x in cnt.keys():
        if cnt[x] >= 5:
            return minValue[x]

def run():
    return pr062()

if __name__ == "__main__":
    print(run())

