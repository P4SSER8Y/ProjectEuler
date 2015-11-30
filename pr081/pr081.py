#coding:utf8
from os import path
import re

def pr081():
    f = open(path.split(path.realpath(__file__))[0] + '\\data081.txt', 'r')
    d = [x for x in f.readlines() if x]
    f.close()

    n = len(d)
    data = []
    for i in xrange(n):
        data.append([int(x) for x in d[i].split(',') if re.match(r'\d+', x)])

    grid = []
    last = []
    for i in xrange(n):
        grid.append([0]*n)
        last.append([0]*n)
    grid[0][0] = data[0][0]
    for i in xrange(1, n):
        grid[i][0] = data[i][0] + grid[i-1][0]
        grid[0][i] = data[0][i] + grid[0][i-1]
        last[i][0] = 'u'
        last[0][i] = 'l'
    for i in xrange(1, n):
        for j in xrange(1, n):
            if grid[i-1][j] < grid[i][j-1]:
                grid[i][j] = grid[i-1][j] + data[i][j]
                last[i][j] = 'u'
            else:
                grid[i][j] = grid[i][j-1] + data[i][j]
                last[i][j] = 'l'
    return grid[-1][-1]

def run():
    return pr081()

if __name__ == "__main__":
    print run()

