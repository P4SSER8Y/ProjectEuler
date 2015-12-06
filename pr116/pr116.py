#coding:utf8

def foo(group):
    n = 50
    f = [0] * (n + max(group))
    f[0] = 1
    for i in range(n): 
        for j in group:
            f[i+j] += f[i]
    return f[n]

def pr116():
    return foo([1, 2]) + foo([1, 3]) + foo([1, 4]) - 3

def run():
    return pr116()

if __name__ == "__main__":
    print(run())
