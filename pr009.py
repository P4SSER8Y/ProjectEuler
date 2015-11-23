def pr009():
    for x in range(1, 1001):
        for y in range(x, 1001):
            if (x + y <= 1000) and (x*x + y*y == (1000 - x - y)**2):
                return x * y * (1000 - x - y)

def run():
    return pr009()

if __name__ == "__main__":
    print run()

