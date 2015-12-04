def run():
    n = 100
    grid = [[0]*n]*n 
    for i in range(n):
        grid[0][i] = 1
        grid[i][0] = 1
    cnt = 0
    for i in range(1, n):
        for j in range(1, n - i + 1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
            if grid[i][j] > int(1e6):
                cnt += 1
    return cnt

if __name__ == "__main__":
    print(run())
