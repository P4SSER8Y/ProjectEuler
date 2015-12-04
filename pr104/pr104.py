#coding:utf8

def pr104():
    def isValid(n):
        s = str(n)
        a = s[:9]
        b = s[-9:]
        for c in '123456789':
            if (not c in a) or (not c in b):
                return False
        return True
    def fibGen():
        yield 1
        a = 1
        b = 1
        while True:
            a, b = b, a + b
            yield a
    fib = fibGen()
    t = next(fib)
    k = 1
    while t < 100000000:
        k += 1
        t = next(fib) 
    while not isValid(t):
        k += 1
        t = next(fib)
    return k
        
def run():
    return pr104()

if __name__ == "__main__":
    print(run())

