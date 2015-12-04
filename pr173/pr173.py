#coding:utf8
from math import sqrt
from itertools import count

def pr173(N):
    ret = 0
    for i in range(1, (N + 8) // 4 + 1):
        for j in count(i+2, 2):
            if (j ** 2 - i ** 2) <= N:
                ret += 1
            else:
                break
    return ret

def run():
    return pr173(1000000)

if __name__ == "__main__":
    print(run())
