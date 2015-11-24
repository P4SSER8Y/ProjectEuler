def pr023(n):

    n = min(28123, n)
    abundantNum = [x for x in range(12, n + 1) if x < sum([y for y in range(1, x / 2 + 1) if x % y == 0])]
    abundantDict = dict.fromkeys(abundantNum, True)
    ret = 0
    for x in xrange(1, n + 1):
        flag = True
        for y in abundantNum:
            if y > x:
                break
            if abundantDict.get(x - y, False):
                flag = False
                break
        if flag:
            ret += x
    return ret

def run():
    return pr023(28124)

if __name__ == "__main__":
    print run()

