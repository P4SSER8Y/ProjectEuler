def pr004():
    def isPalindrome(n):
        t = n
        r = 0
        while (t > 0):
            r = r * 10 + t % 10
            t /= 10
        return n == r
    maxProd = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            if isPalindrome(i * j):
                maxProd = max(maxProd, i*j)
    return maxProd

def run():
    return pr004()

if __name__ == "__main__":
    print run()

