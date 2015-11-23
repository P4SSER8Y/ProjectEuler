from usr import getPrimes 
from PBar import PBar   

def pr047(factors, maxNum):
    prime = getPrimes(maxNum)
    factor = dict.fromkeys(range(maxNum + 1), 0)

    pbar = PBar(maxNum).start()
    for x in prime:
        pbar.update(x)
        y = x
        while y <= maxNum:
            factor[y] = factor[y] + 1
            y += x
    pbar.finish()

    pbar.start()
    for t in xrange(2, maxNum - factors):
        pbar.update(t)
        flag = True
        for y in xrange(factors):
            if factor[t + y] != factors:
                flag = False
                break
        if flag:
            break
    pbar.finish()
    return [t + x for x in range(factors)]

def run():
    return pr047(4, 1000000)
    #return pr047(3, 1000)

