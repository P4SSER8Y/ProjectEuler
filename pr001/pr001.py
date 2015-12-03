def pr001(n):
    return sum([x for x in range(2, n) if (x % 3 == 0) or (x % 5 == 0)])

def run():
    return pr001(1000)

if __name__ == "__main__":
    print(run())
