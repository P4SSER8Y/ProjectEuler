def pr014(n):
    def collatzIter(n):
        if record.get(n, 0) > 0:
            return record[n]
        else:
            if n % 2 == 0:
                t = collatzIter(n / 2) + 1
            else:
                t = collatzIter(3 * n + 1) + 1
            record[n] = t
            return t
    record = {1: 1}
    maxN = 1
    for k in range(1, n+1):
        cnt = collatzIter(k)
        if cnt > record[maxN]:
            maxN = k
    return maxN

def run():
    return pr014(1000000)

if __name__ == "__main__":
    print(run())

