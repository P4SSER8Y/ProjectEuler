from os.path import split, realpath
def pr022():

    def calc(name):
        return sum(map(lambda x: ord(x) - ord('A') + 1, name))
    import re
    f = open(split(realpath(__file__))[0]+'\\data022.txt', 'r')
    raw = f.read()
    f.close()
    raw = re.sub(r'[^A-Z]', ' ', raw)
    raw = re.sub(r' +', '|', raw)
    name = [x for x in raw.split('|') if len(x) > 0]
    name.sort()
    ret = 0
    for k in range(len(name)):
        ret += (k + 1) * calc(name[k])
    return ret

def run():
    return pr022()

if __name__ == "__main__":
    print run()

