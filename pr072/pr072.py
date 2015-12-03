from ctypes import *
from PBar import PBar

phi = CDLL('pr072\pr072.dll').phi
phi.argstype = [c_long, POINTER(c_long)]
phi.restype = c_long

getPrimes = CDLL('pr072\pr072.dll').getPrimes
getPrimes.argstype = [c_long]
getPrimes.restype = POINTER(c_long)

def run():
    primes = getPrimes(int(1e6))
    pbar = PBar(int(1e6)).start()
    ret = 0
    for x in xrange(2, int(1e6)+1):
        ret += phi(x, primes)
        pbar.update(x)
    pbar.finish()
    return ret

if __name__ == "__main__":
    print(run())

