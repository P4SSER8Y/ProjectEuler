#coding:utf8

def pr179(n):
    f = [0] * n
    for i in range(1, n):
        j = i
        while j < n:
            f[j] += 1
            j += i
    cnt = 0
    for i in range(1, n):
        if f[i] == f[i-1]:
            cnt += 1
    return cnt 

def run():
    return pr179(int(1e7))

if __name__ == "__main__":
    print(run())
