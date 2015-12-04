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
        for y in range(3, int(x ** 0.5 + 1), 2):
            if x % y == 0:
                return False
        return True
    s = '1234567'
    for i in range(9999999, 2, -1):
        if isPandigital(i) and isPrime(i):
            return i

def run():
    return pr041()

if __name__ == "__main__":
    print(run())

