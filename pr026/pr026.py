def pr026(n):
    def getCycleLen(d):
        a = 1
        pre = {}
        cnt = 0
        while (a > 0):
            a *= 10
            cnt += 1
            if pre.get(a, 0) > 0:
                return cnt - pre[a]
            pre[a] = cnt
            a = a % d
        return 0
    cycleLenDict = {1:0}
    ret = 1
    for d in range(2, n + 1):
        t = getCycleLen(d)
        cycleLenDict[d] = t
        if t > cycleLenDict[ret]:
            ret = d
    return ret

def run():
    return pr026(999)

if __name__ == "__main__":
    print(run())

