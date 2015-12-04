#coding:utf8
from itertools import permutations
from functools import reduce
from PBar import PBar

def rearrange(p):
    def finished():
        for x in range(1, len(p)):
            if p[x] < p[x - 1]:
                return False
        return True
    def split():
        a = []
        for x in range(len(p)):
            if p[x] == x:
                a.append(x)
            else:
                break
        i = p.index(len(a))
        l = p[len(a):i]
        r = p[i+1:]
        return a, l, [p[i]], r
    ret = 0
    while not finished():
        a, l, x, r = split() 
        if r:
            ret += 2
            l.reverse()
            p = a + x + r + l
        else:
            ret += 1
            l.reverse()
            p = a + x + l
    return ret 

def pr336(n, s):
    maxA = []
    maxN = 0
    cnt = 0
    pbar = PBar(reduce(lambda x, y: x * y, range(1, n + 1))).start()
    for p in permutations(range(n)):
        cnt += 1
        pbar.update(cnt)
        t = rearrange(list(p[:]))
        if t > maxN:
            maxA = [''.join(map(lambda x: chr(ord('A')+x), p))]
            maxN = t
        elif t == maxN:
            maxA += [''.join(map(lambda x: chr(ord('A')+x), p))]
    pbar.finish()
    maxA.sort()
    return maxA[s-1]

def run():
    return pr336(11, 2011)

if __name__ == "__main__":
    print(run())

