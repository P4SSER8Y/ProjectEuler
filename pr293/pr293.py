#coding:utf8
from usr import getPrimes, isPrimeMR

def pr293(N):
    def getPseudo(n):
        t = n + 3
        while not isPrimeMR(t):
            t += 2
        return t - n
    primes = getPrimes(N >> 1)

    pseudo = set()
    twos = 2
    while twos < N:
        pseudo.add(getPseudo(twos))
        k = 1
        last = [twos]
        while (len(last) > 0):
            curr = []
            p = primes[k]
            for x in last: 
                t = x * p
                while t < N:
                    curr.append(t)
                    t *= p
            for x in curr:
                pseudo.add(getPseudo(x))
            last = curr
            k += 1 
        twos <<= 1        
    return sum(pseudo)

def run():
    return pr293(int(1e9))

if __name__ == "__main__":
    print(run())
