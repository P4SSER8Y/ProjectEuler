import itertools
from usr import getPrimes

def run():
    primes = set(x for x in getPrimes(10000) if x > 1000)
    valid_a = []
    for p in primes:
        tmp = [int(''.join(y)) for y in itertools.permutations(str(p)) if int(''.join(y)) in primes]
        tmp = list(dict.fromkeys(tmp).keys())
        if len(tmp) >= 3:
            tmp.sort()
            if not tmp in valid_a:
                valid_a.append(tmp)
    valid_a.sort()
    ret = []
    for x in valid_a:
        for y in itertools.combinations(x, 3):
            if y[0] + y[2] == 2*y[1]:
                ret.append(y)
    return ret

if __name__ == "__main__":
    print(run())
