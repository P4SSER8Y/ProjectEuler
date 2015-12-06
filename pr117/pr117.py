#coding:utf8

def foo(group):
    n = 50
    f = [0] * (n + max(group))
    f[0] = 1
    for i in range(n): 
        for j in group:
            f[i+j] += f[i]
    return f[n]

def pr117():
    return foo([1, 2, 3, 4])

def run():
    return pr117()

if __name__ == "__main__":
    print(run())
