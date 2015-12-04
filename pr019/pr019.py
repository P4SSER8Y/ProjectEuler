from datetime import date

def pr019():
    cnt = 0
    for i in range(1901, 2001):
        for j in range(1, 13):
            if date(i, j, 1).weekday() == 6:
                cnt += 1
    return cnt

def run():
    return pr019()

if __name__ == "__main__":
    print(run())

