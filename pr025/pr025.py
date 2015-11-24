from PBar import PBar

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
    pbar = PBar(maxval=n).start()
    fib = fibIter()
    cnt = 1
    f = fib.next()
    while len(str(f)) < n:
        pbar.update(len(str(f))) 
        cnt += 1
        f = fib.next()
    pbar.finish()
    return cnt

def run():
    return pr025(1000)

if __name__ == "__main__":
    print run()

