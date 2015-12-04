def run():
    def iter(used, ans):
        if len(used) == 6:
            if valid(ans[-1], ans[0]):
                print(ans)
                return ans
        for k in polygonalKey:
            if not k in used:
                for x in polygonal[k]:
                    if valid(ans[-1], x):
                        t = iter(used + [k], ans + [x]) 
                        if t:
                            return t
    valid = lambda x, y: x % 100 == y // 100
    polygonal = {3: [n*(n+1)//2 for n in range(45, 141)],
                 4: [n*n for n in range(32, 100)],
                 5: [n*(3*n-1)//2 for n in range(26, 82)],
                 6: [n*(2*n-1) for n in range(23, 71)],
                 7: [n*(5*n-3)//2 for n in range(21, 64)],
                 8: [n*(3*n-2) for n in range(19, 59)]}
    polygonalKey = range(3, 9)
    for k in polygonalKey:
        for x in polygonal[k]:
            ans = iter([k], [x])
            if ans:
                return sum(ans)

if __name__ == "__main__":
    print(run())
