from usr import getPrimes

def pr050(n):
    prime = getPrimes(n)
    primeSet = set(prime)
    maxCnt = 0
    maxSum = 0
    for i in range(len(prime)):
        cnt = 0
        sum = 0
        for j in range(i, len(prime)):
            cnt += 1
            sum += prime[j]
            if sum in primeSet:
                if cnt > maxCnt:
                    maxCnt = cnt
                    maxSum = sum
            if sum > n:
                break
    return maxSum

def run():
    return pr050(1000000)

if __name__ == "__main__":
    print(run())

