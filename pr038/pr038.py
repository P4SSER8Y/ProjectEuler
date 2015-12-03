def pr038():
    def push(s):
        if len(s) > 9:
            return None
        if sum(1 for c in '123456789' if c in s) == 9:
            ret.append(int(s))
    ret = []
    for x in xrange(1, 10000):
        s = ''
        i = 1
        while len(s) < 9:
            s += str(x * i)
            i += 1
        push(s)
    return sorted(ret, reverse=True)[0]

def run():
    return pr038()

if __name__ == "__main__":
    print(run())

