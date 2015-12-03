def run():
    f = [0] * 101
    f[0] = 1
    for i in range(1, 101):
        for j in range(i, 101):
            f[j] = f[j] + f[j-i]
    return f[100] - 1

if __name__ == "__main__":
    print(run())
