from itertools import count
from usr import isPrime

def run():
    totalCnt = 1
    primeCnt = 0
    for k in count(2):
        totalCnt += 4
        primeCnt += len(filter(isPrime,
                               [(2*k-1)**2-2*(k-1),
                                (2*k-1)**2-4*(k-1),
                                (2*k-1)**2-6*(k-1)]))
        if primeCnt / float(totalCnt) <= 0.1:
            break
    return 2*k-1

if __name__ == "__main__":
    print run()

