#coding:utf8
from math import sqrt
from usr import gcd

def pr075(N):
    f = [0] * (N + 1)
    for m in range(1, int(sqrt(N))):
        for n in range(1, m):
            if ((n + m) & 1) and (gcd(n, m) == 1):
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                p = a + b + c
                s = p
                while (s <= N):
                    f[s] += 1
                    s += p
    ret = 0
    for x in f:
        if x == 1:
            ret += 1
    return ret

def run():
    return pr075(1500000)

if __name__ == "__main__":
    print(run())
