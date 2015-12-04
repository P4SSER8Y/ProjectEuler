from functools import reduce

def pr020(n): 
    n = reduce(lambda x, y: x * y, range(1, n + 1))
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

def run():
    return pr020(100)

if __name__ == "__main__":
    print(run())

