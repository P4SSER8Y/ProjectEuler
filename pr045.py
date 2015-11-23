def pr045():
    H = lambda n: n * (2 * n - 1)
    P = lambda n: n * (3 * n - 1) / 2
    T = lambda n: n * (n + 1) / 2
    c = 143 # n(2n-1)
    b = 165 # n(3n-1)/2
    a = 286 # n(n+1)/2
    while (H(c) != P(b)) or (H(c) != T(a)):
        c += 1
        while (P(b) < H(c)): b += 1
        if P(b) > H(c): continue
        while (T(a) < P(b)): a += 1
    return T(a)

def run():
    return pr045()

if __name__ == "__main__":
    print run()

