def pr016(n):
    t = 2 ** n
    cnt = 0
    while t > 0:
        cnt += t % 10
        t //= 10
    return cnt

def run():
    return pr016(1000)

if __name__ == "__main__":
    print(run())

