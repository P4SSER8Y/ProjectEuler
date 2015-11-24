def pr029():
    d = {}
    for a in range(2, 101):
        for b in range(2, 101):
            d[a**b] = None
    return len(d.keys())

def run():
    return pr029()

if __name__ == "__main__":
    print run()

