def run():
    ans = []
    def iter(ret):
        def check():
            for c in forward.keys():
                if len(forward[c]) > 0:
                    return False
                if len(backward[c]) > 0:
                    return False
            return True
        if check():
            ans.append(ret)
            return 
        t1 = list(backward[ret[-1]])
        for c1 in t1:
            fLst = ''
            for c2 in forward.keys():
                if c1 in forward[c2]:
                    fLst += c2
                    forward[c2].remove(c1)
            bLst = ''
            for c2 in backward.keys():
                if c1 in backward[c2]:
                    bLst += c2
                    backward[c2].remove(c1)
            iter(ret + c1)
            for c2 in fLst:
                forward[c2].add(c1)
            for c2 in bLst:
                backward[c2].add(c1)

    f = open('data079.txt', 'r')
    data = [s[:3] for s in f.readlines()]
    f.close()
    forward = {}
    backward = {}
    for c in '1234567890':
        forward[c] = set()
        backward[c] = set()
    for x in data:
        backward[x[0]].add(x[1])
        backward[x[0]].add(x[2])
        forward[x[1]].add(x[0])
        backward[x[1]].add(x[2])
        forward[x[2]].add(x[0])
        forward[x[2]].add(x[1])
    for c in '0123456789':
        fLst = ''
        for t in forward.keys():
            if c in forward[t]:
                fLst += c
                forward[t].remove(c)
        iter(c)
        for t in fLst:
            forward[t].add(c)
    return ans

if __name__ == "__main__":
    print run()