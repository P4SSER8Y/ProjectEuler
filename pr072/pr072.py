from ctypes import *
from platform import architecture
from PBar import PBar

if architecture()[0] == "64bit":
    cLib = CDLL('pr072\pr072.dll')
else:
    cLib = CDLL('pr072\pr072_32.dll')

phi = cLib.phi
phi.argstype = [c_long, POINTER(c_long)]
phi.restype = c_long

getPrimes = cLib.getPrimes
getPrimes.argstype = [c_long]
getPrimes.restype = POINTER(c_long)

def run():
    primes = getPrimes(int(1e6))
    ret = 0
    for x in range(2, int(1e6)+1):
        ret += phi(x, primes)
    return ret

if __name__ == "__main__":
    print(run())
