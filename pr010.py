def pr010(n):
    lst = [True] * (n + 1)
    lst[0] = False
    lst[1] = False
    ret = 0
    k = 0
    while k <= n:
        while (k <= n) and (lst[k] is False):
            k += 1
        if k > n:
            break
        ret += k
        t = k + k
        while (t <= n):
            lst[t] = False
            t += k
        k += 1
    return ret

def pr010_2(n):
    from usr import getPrimes
    return sum(getPrimes(n))

def run():
    return pr010_2(2000000)

if __name__ == "__main__":
    print run()

