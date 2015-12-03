from usr import isPrime as cIsPrime
def pr046():
    def isPrime(n):
        if primeDict.get(n, False):
            return True
        if cIsPrime(n):
            primeDict[n] = True
            return True
        return False
    def isValid(x):
        if isPrime(x): return False
        for y in xrange(1, int((x/2)**0.5)+1):
            if isPrime(x - 2 * y * y):
                return False
        return True
    primeLst = [2, 3, 5, 7]
    primeDict = dict.fromkeys(primeLst, True)
    k = 9
    while not isValid(k):
        k += 2 
    return k

def run():
    return pr046()

if __name__ == "__main__":
    print(run())

