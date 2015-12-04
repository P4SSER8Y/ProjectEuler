from os.path import split, realpath

def pr042():
    def value(word):
        return sum(map(lambda c: ord(c) - ord('A') + 1, word))
    f = open(split(realpath(__file__))[0]+'\\data042.txt', 'r')
    words = eval('[' + f.readline() + ']')
    f.close()
    triNum = [0]
    for x in range(1, 100):
        triNum.append(triNum[-1] + x)
    ret = 0
    for word in words:
        if value(word) in triNum:
            ret += 1
    return ret

def run():
    return pr042()

if __name__ == "__main__":
    print(run())

