from itertools import count
def run():
    def isBounce(x):
        def isIncreased(s):
            for k in range(len(s)-1):
                if s[k] > s[k+1]:
                    return False
            return True
        def isDecreased(s):
            for k in range(len(s)-1):
                if s[k] < s[k+1]:
                    return False
            return True
        return not(isIncreased(str(x)) or isDecreased(str(x)))
    cnt = 0
    for x in count(100):
        if isBounce(x):
            cnt += 1
        if float(cnt)/x >= 0.99:
            return x

if __name__ == "__main__":
    print(run())
