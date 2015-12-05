#coding:utf8
from math import sqrt

def pr125(N):
    def isPalindrome(n):
        s = str(n)
        for i in range(len(s) >> 1):
            if s[i] != s[- i - 1]:
                return False
        return True
    sumSqr = [0] * int(sqrt(N) + 1)
    for i in range(1, len(sumSqr)):
        sumSqr[i] = sumSqr[i - 1] + i * i

    ret = set()
    for i in range(len(sumSqr)):
        for j in range(i + 2, len(sumSqr)):
            s = sumSqr[j] - sumSqr[i]
            if (s < N) and isPalindrome(s):
                ret.add(s)
    return sum(ret) 

def run():
    return pr125(10 ** 8)

if __name__ == "__main__":
    print(run())
