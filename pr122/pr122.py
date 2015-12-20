#coding:utf8

def pr122():
    def iter(i, path, depth):
        if (i > 200) or (depth > m[i]):
            return
        m[i] = depth
        for j in path:
            iter(i + j, [i + j] + path, depth + 1)
    m = [2147483647] * 201
    m[0] = 0
    m[1] = 0
    iter(1, [1], 0)
    return sum(m[:201])

def run():
    return pr122()

if __name__ == "__main__":
    print(run())

