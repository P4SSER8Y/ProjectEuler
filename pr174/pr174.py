#coding:utf8
from itertools import count

def pr174():
    foo = dict.fromkeys(range(1000000 + 1), 0)
    for i in range(1, (1000000 + 8) // 4 + 1):
        for j in count(i+2, 2):
            if (j ** 2 - i ** 2) <= 1000000:
                foo[j ** 2 - i ** 2] += 1
            else:
                break 
    ret = 0
    for x in foo.keys():
        if (1 <= foo[x]) and (foo[x] <= 10):
            ret += 1
    return ret

def run():
    return pr174()

if __name__ == "__main__":
    print(run())
