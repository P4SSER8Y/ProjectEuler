def pr036(n):
    def isPalindromic(s):
        for k in range(len(s) // 2):
            if s[k] != s[len(s) - k - 1]:
                return False
        return True
    def dec2bin(x):
        ret = ''
        while x > 0:
            if (x % 2 == 0):
                ret = '0' + ret
            else:
                ret = '1' + ret
            x //= 2
        return ret
    ret = []
    for x in range(n + 1):
        if isPalindromic(str(x)) and isPalindromic(dec2bin(x)):
            ret.append(x)
    return sum(ret)

def run():
    return pr036(1000000)

if __name__ == "__main__":
    print(run())

