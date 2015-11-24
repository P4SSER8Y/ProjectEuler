def run():
    f = open('data067.txt', 'r')
    lines = f.readlines()
    f.close()
    f = []
    for l in lines:
        f.append([0] + map(int, l.split(' ')) + [0])
    for i in range(1, len(f)):
        for j in range(1, len(f[i])-1):
            f[i][j] += max(f[i-1][j-1], f[i-1][j])
    return max(f[-1])

if __name__ == "__main__":
    print run()
