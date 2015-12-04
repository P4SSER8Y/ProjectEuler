def run(): 
    maxSum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            t = a ** b
            s = 0
            while (t > 0):
                s += t % 10
                t //= 10
            if s > maxSum:
                maxSum = s
    return maxSum

if __name__ == "__main__":
    print(run())

