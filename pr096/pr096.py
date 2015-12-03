#coding:utf8
from os import path
import copy

def sudokuShow(grid):
    for x in grid:
        print x
    print

def sudokuSolver(grid):
    def isFailed(grid):
        for i in xrange(9):
            for j in xrange(9):
                if (grid[i][j] == 0) and (len(candidates[i][j]) == 0):
                    return True
        return False
    def isSolved(grid):
        for x in grid:
            for y in x:
                if y == 0:
                    return False
        return True
    def clear(x, y): 
        m = grid[x][y]
        candidates[x][y].clear()
        for i in xrange(9):
            candidates[i][y] -= {m}
            candidates[x][i] -= {m}
        for i in xrange(x/3*3, (x/3+1)*3):
            for j in xrange(y/3*3, (y/3+1)*3): 
                candidates[i][j] -= {m}
    def count():
        row = []
        col = []
        for _ in xrange(9):
            row.append([0] * 11)
            col.append([0] * 11) 
        for i in xrange(9):
            for j in xrange(9):
                for x in candidates[i][j]:
                    row[i][x] += 1
                    col[j][x] += 1 
        return row, col 
    def fuckit():
        for i in xrange(9):
            for j in xrange(9):
                if len(candidates[i][j]) == 1:
                    grid[i][j] = candidates[i][j].pop()
                    clear(i, j)
                    return True
        row, col = count()
        for x in xrange(1, 10):
            for i in xrange(9):
                if row[i][x] == 1:
                    for j in xrange(9):
                        if x in candidates[i][j]:
                            break
                    grid[i][j] = x
                    clear(i, j)
                    return True
                if col[i][x] == 1:
                    for j in xrange(9):
                        if x in candidates[j][i]:
                            break
                    grid[j][i] = x
                    clear(j, i)
                    return True
        return False

    candidates = []
    for i in xrange(9):
        candidates.append([])
        for j in xrange(9):
            candidates[i].append(set(xrange(1, 10)))
    for i in xrange(9):
        for j in xrange(9):
            if grid[i][j] > 0:
                clear(i, j)
    while not isSolved(grid):
        if isFailed(grid):
            return False
        if not fuckit():
            for i in xrange(9):
                for j in xrange(9):
                    if grid[i][j] == 0:
                        break
                if grid[i][j] == 0:
                    break
            for x in candidates[i][j]:
                tmp = copy.deepcopy(grid)
                tmp[i][j] = x
                sudokuSolver(tmp)
                if isSolved(tmp):
                    grid = tmp
                    return True
            break
    return isSolved(grid)

def pr096():
    f = open(path.split(path.realpath(__file__))[0]+"\\data096.txt", 'r')
    ret = 0
    for _ in xrange(50):
        f.readline()
        grid = []
        for __ in xrange(9):
            grid.append([int(c) for c in f.readline() if ('0' <= c) and (c <= '9')]) 
        print _+1,sudokuSolver(grid)
        ret += grid[0][0]*100+grid[0][1]*10+grid[0][2]
    f.close()
    return ret

def run():
    return pr096()

if __name__ == "__main__":
    print run()

