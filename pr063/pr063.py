from itertools import count
from math import pow

def run():
    cnt = 0
    for n in count(1):
        t = int(round(pow(pow(10, n - 1) - 1, 1.0 / n)))
        cnt += 10 - t
        if pow(t, n) < pow(10, n - 1):
            cnt -= 1
        if t == 10:
            return cnt

if __name__ == "__main__":
    print run()