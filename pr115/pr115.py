#coding:utf8
from itertools import count

def F(m, n):
    fr = [0] * (n + 1)
    fb = [0] * (n + m + 1)
    fb[0] = 1
    for i in range(1, n+1):
        fr[i] = fr[i-1] + fb[i-m]
        fb[i] = fr[i-1] + fb[i-1]
    return fr[n] + fb[n]

def pr115(): 
    for n in count(1):
        if F(50, n) > 1000000:
            return n

def run():
    return pr115()

if __name__ == "__main__":
    print(run())
