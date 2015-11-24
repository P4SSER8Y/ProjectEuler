from PBar import PBar

def pr024(n):
    pbar = PBar(maxval=n).start()
    curr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for _ in xrange(1, n):
        pbar.update(_)
        k = len(curr) - 2
        while (k > 0) and (curr[k] > curr[k + 1]):
            k -= 1
        m = k + 1
        for c in range(m + 1, len(curr)):
            if (curr[c] < curr[m]) and (curr[c] > curr[k]):
                m = c
        a, b = curr[m], curr[k]
        a, b = b, a
        curr[m], curr[k] = a, b
        curr = curr[:(k + 1)] + sorted(curr[(k+1):])
    pbar.finish()
    return reduce(lambda x, y: x + y, curr, '')

def run():
    return pr024(1000000)

if __name__ == "__main__":
    print run()

