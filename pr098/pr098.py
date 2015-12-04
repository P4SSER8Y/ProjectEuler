#coding:utf8

def pr098():
    def counter(n):
        ret = [0] * 10
        while n:
            ret[n % 10] += 1
            n //= 10
        return tuple(ret)
    tmp = {}
    for i in range(10**5):
        t = counter(i * i)
        tmp[t] = tmp.get(t, []) + [i * i]
    t = []
    for x in tmp.keys():
        if len(tmp[x]) < 2:
            t.append(x)
    for x in t:
        tmp.pop(x)
    print(len(tmp.keys()))

def run():
    return pr098()

if __name__ == "__main__":
    print(run())

