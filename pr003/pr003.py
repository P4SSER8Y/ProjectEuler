def pr003(n):
    primes = []
    k = 2
    while (k * k) <= n:
        if all(map(lambda x: k % x != 0, primes)):
            primes.append(k)
            if (n % k == 0):
                maxPrime = k
                while (n % k == 0):
                    n //= k
        k += 1
    return n

def run():
    return pr003(600851475143)

if __name__ == "__main__":
    print(run())

