#coding:utf8

def F(m, n):
    fr = [0] * (n + 1)
    fb = [0] * (n + m + 1)
    fb[0] = 1
    for i in range(1, n+1):
        fr[i] = fr[i-1] + fb[i-m]
        fb[i] = fr[i-1] + fb[i-1]
    return fr[n] + fb[n]

def pr114():
    return F(3, 50)

def run():
    return pr114()

if __name__ == "__main__":
    print(run())
