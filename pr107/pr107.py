#coding:utf8
from os.path import split, realpath, sep

def readData():
    MAX_INT = 2147483647
    data = []
    f = open(split(realpath(__file__))[0] + sep + "data107.txt", 'r')
    for s in f.readlines():
        data.append([])
        for d in s.split(','): 
            if d[0] == '-':
                data[-1].append(-1)
            else:
                try:
                    data[-1].append(int(d))
                except:
                    pass
    f.close()
    return data

def pr107():
    data = readData()
    ret = 0
    queue = []
    vSet = set()
    for j in range(len(data)):
        if data[0][j] >= 0:
            queue.append((0, j))
    vSet.add(0)
    for _ in range(len(data) - 1): 
        queue.sort(key = lambda x: data[x[0]][x[1]])
        e = queue.pop(0) 
        while (e[0] in vSet) and (e[1] in vSet):
            e = queue.pop(0) 
        vSet.add(e[1])
        for j in range(len(data)):
            if (not j in vSet) and (data[e[1]][j] >= 0):
                queue.append((e[1], j))
        ret += data[e[0]][e[1]]
    total = 0
    for i in data:
        for j in i:
            if j > -1:
                total += j
    return total // 2 - ret

def run():
    return pr107()

if __name__ == "__main__":
    print(run())
