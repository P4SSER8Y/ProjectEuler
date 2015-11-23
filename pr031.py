def pr031():
    coin = [1, 2, 5, 10, 20, 50, 100, 200]
    total = [1] + [0] * 200
    for c in coin:
        for k in range(1, len(total)):
            if (k - c) >= 0:
                total[k] += total[k - c]
    return total[200]
                

def run():
    return pr031()
if __name__ == "__main__":
    print run()

