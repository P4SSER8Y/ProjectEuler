from usr import getPrimes 

def pr047(factors, maxNum):
    prime = getPrimes(maxNum)
    factor = dict.fromkeys(range(maxNum + 1), 0)

    for x in prime:
        y = x
        while y <= maxNum:
            factor[y] = factor[y] + 1
            y += x

    for t in range(2, maxNum - factors):
        flag = True
        for y in range(factors):
            if factor[t + y] != factors:
                flag = False
                break
        if flag:
            break
    return t + factor[0]

def run():
    return pr047(4, 1000000)
    #return pr047(3, 1000)

