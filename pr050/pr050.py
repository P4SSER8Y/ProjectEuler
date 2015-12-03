from usr import getPrimes
from PBar import PBar

def pr050(n):
    prime = getPrimes(n)
    primeSet = set(prime)
    maxCnt = 0
    maxSum = 0
    pbar = PBar(len(prime)).start()
    for i in xrange(len(prime)):
        pbar.update(i)
        cnt = 0
        sum = 0
        for j in xrange(i, len(prime)):
            cnt += 1
            sum += prime[j]
            if sum in primeSet:
                if cnt > maxCnt:
                    maxCnt = cnt
                    maxSum = sum
            if sum > n:
                break
    pbar.finish()
    return maxCnt, maxSum

def run():
    return pr050(1000000)

if __name__ == "__main__":
    print(run())

