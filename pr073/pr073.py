#coding:utf8
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def pr073():
    ret = 0
    for x in range(4, 12001):
        for y in range(x//3 + 1, x//2 + (x & 1)):
            if gcd(x, y) == 1:
                ret += 1
    return ret

def run():
    return pr073()

if __name__ == "__main__":
    print(run())

