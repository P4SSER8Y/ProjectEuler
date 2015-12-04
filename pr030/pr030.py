def pr030():
    def fn(x):
        y = x
        t = 0
        while x > 0:
            t += (x % 10) ** 5
            x //= 10
        return y == t
    return sum([x for x in range(2, 1000000) if fn(x)])

def run():
    return pr030()

if __name__ == "__main__":
    print(run())

