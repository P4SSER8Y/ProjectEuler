#coding:utf8
from itertools import permutations

def pr068():
    ret = 0
    for p in permutations(range(1, 11)):
        if min(p[0], p[3], p[5], p[7], p[9]) != p[0]:
            continue
        s = "".join(map(str, [p[0], p[1], p[2],\
                              p[3], p[2], p[4],\
                              p[5], p[4], p[6],\
                              p[7], p[6], p[8],\
                              p[9], p[8], p[1]]))
        if len(s) == 17:
            continue
        t = p[0] + p[1] + p[2]
        if (t == p[2] + p[3] + p[4]) and\
           (t == p[4] + p[5] + p[6]) and\
           (t == p[6] + p[7] + p[8]) and\
           (t == p[1] + p[8] + p[9]):
            if int(s) > ret:
                ret = int(s)
    return ret

def run():
    return pr068()

if __name__ == "__main__":
    print(run())
