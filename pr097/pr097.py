def powerMod(a, n, m):
    if n == 0: 
        return 1
    if n == 1:
        return a % m
    if n & 1 == 1:
        return (powerMod((a * a) % m, n >> 1, m) * a) % m
    else:
        return powerMod((a * a) % m, n >> 1, m) % m

def run():
    return (28433 * powerMod(2, 7830457, int(1e10)) + 1) % int(1e10)

if __name__ == "__main__":
    print(run())
