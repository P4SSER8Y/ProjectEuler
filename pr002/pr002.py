def pr002(n):
    def fibIter():
        a = 0
        b = 1
        while True:
            c = a + b
            a = b
            b = c
            yield c
    even = lambda x : x % 2 == 0
    ret = 0
    fib = fibIter()
    for x in fib:
        if x <= n :
            if even (x):
                ret += x
        else:
            break
    return ret

def run():
    return pr002(4000000)

if __name__ == "__main__":
    print(run())

