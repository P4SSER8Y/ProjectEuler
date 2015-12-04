def run():
    fac = [0] * 10
    fac[0] = 1
    for x in range(1, 10):
        fac[x] = x * fac[x-1]
    ret = 0
    for x in range(10, 3000000):
        if x == sum([fac[int(c)] for c in str(x)]):
            ret += x
    return ret

if __name__ == "__main__":
    print(run()) 
