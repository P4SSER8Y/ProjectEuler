import re
import string
from operator import xor
from itertools import cycle
from os.path import split, realpath, sep

def pr059():
    def decrypt(key, ori):
        ret = ''
        for c in ori:
            ret += chr(xor(ord(next(key)), c))
        return ret
    f = open(split(realpath(__file__))[0]+sep+"data059.txt", 'r')
    data = list(map(int, f.readline().split(',')))
    f.close()
    maxEs = 0
    best = []
    bestText = ''
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                tmp = decrypt(cycle([a, b, c]), data)
                cnt = len([c for c in tmp if c == ' '])
                if cnt > maxEs:
                    maxEs = cnt
                    best = [a, b, c]
                    bestText = tmp
    return sum(map(ord, bestText))

def run():
    return pr059()

if __name__ == "__main__":
    print(run())
