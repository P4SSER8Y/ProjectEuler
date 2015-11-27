#coding:utf8
from PBar import PBar

def pr145(n):
    def isValid(n):
        while n:
            if ((n % 10) & 1) == 0:
                return False
            n /= 10
        return True
    def revNum(n):
        s = 0
        while n:
            s = s * 10 + n % 10
            n /= 10
        return s
    pbar = PBar(n).start()
    ret = 0
    for x in xrange(1, min(int(9e7), n)):
        if x % 10:
            if isValid(x + revNum(x)):
                pbar.update(x)
                ret += 1
                t = x
    pbar.finish()
    return ret, t

def run():
    return pr145(int(1e9))

if __name__ == "__main__":
    print run()

