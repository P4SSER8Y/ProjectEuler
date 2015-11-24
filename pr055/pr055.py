reverse = lambda s: reduce(lambda a, b: b + a, s)

def isPalindromic(s):
    return s == reverse(s)

def isLychrel(n):
    for _ in range(50):
        n += int(reverse(str(n)))
        if isPalindromic(str(n)):
            return False
    return True

def run():
    cnt = 0
    for n in range(10000):
        if isLychrel(n):
            cnt += 1
    return cnt

if __name__ == "__main__":
    print run()

