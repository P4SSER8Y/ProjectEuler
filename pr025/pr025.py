def pr025(n):
    def fibIter():
        a = 0
        b = 1
        yield b
        while True:
            c = a + b
            yield c
            a = b
            b = c
    fib = fibIter()
    cnt = 1
    f = next(fib)
    while len(str(f)) < n:
        cnt += 1
        f = next(fib)
    return cnt

def run():
    return pr025(1000)

if __name__ == "__main__":
    print(run())

