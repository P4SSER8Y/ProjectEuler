def pr015(n):
    grid = [[1] * (n + 1)] + [[1] + [0] * n] * n
    for i in range(1, n+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i-1][j]+grid[i][j-1]
    return grid[n][n]

def run():
    return pr015(20)

if __name__ == "__main__":
    print(run())

