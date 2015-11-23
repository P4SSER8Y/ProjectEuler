import re
import string
from operator import xor
from itertools import cycle

def pr059():
    def decrypt(key, ori):
        ret = ''
        for c in ori:
            ret += chr(xor(ord(key.next()), c))
        return ret
    f = open("data059.txt", 'r')
    data = map(int, f.readline().split(','))
    f.close()
    maxEs = 0
    best = []
    bestText = ''
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                tmp = decrypt(cycle([a, b, c]), data)
                cnt = len(filter(lambda c: c == ' ', tmp))
                if cnt > maxEs:
                    maxEs = cnt
                    best = [a, b, c]
                    bestText = tmp
    print maxEs
    print ''.join(best)
    print bestText
    print
    return sum(map(ord, bestText))


def run():
    return pr059()

if __name__ == "__main__":
    print run()