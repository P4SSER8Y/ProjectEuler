def pr006(n):
    return sum(range(n+1))**2 - sum(map(lambda x: x * x, range(n+1)))

def run():
    return pr006(100)

if __name__ == "__main__":
    print(run())

