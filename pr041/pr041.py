from PBar import PBar

"""
1+2+...+9 = 45 = 3 * 15
1+2+...+8 = 36 = 3 * 12
"""

def pr041():
    def isPandigital(x):
        t = str(x)
        for c in s[:len(t)]:
            if not c in t:
                return False
        return True
    def isPrime(x):
        if x % 2 == 0:
            return False
        for y in xrange(3, int(x ** 0.5 + 1), 2):
            if x % y == 0:
                return False
        return True
    s = '1234567'
    pbar = PBar(9999999).start()
    for i in xrange(9999999, 2, -1):
        pbar.update(9999999 - i)
        if isPandigital(i) and isPrime(i):
            pbar.finish()
            return i

def run():
    return pr041()

if __name__ == "__main__":
    print(run())

