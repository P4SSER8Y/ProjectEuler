#coding:utf8

def pr095(N):
    def foo(chain, n):
        if n > N:
            return []
        if n in chain:
            return chain[chain.index(n):]
        if flag[n]:
            return []
        flag[n] = True
        return foo(chain + [n], sumOfDiv[n]) 
    sumOfDiv = [0] * (N + 1)
    for i in range(1, 1 + (N >> 1)):
        j = 2 * i
        while j <= N: 
            sumOfDiv[j] += i
            j += i
    flag = [False] * (N + 1)
    longest = []
    for i in range(2, N + 1): 
        temp = foo([], i)
        if len(temp) > len(longest):
            longest = temp
    return min(longest)

def run():
    return pr095(int(1e6))

if __name__ == "__main__":
    print(run())
