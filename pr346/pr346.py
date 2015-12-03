#coding:utf8

def pr346(N):
    collection = set([1])
    available = set([1])
    for b in xrange(2, 1e10)):
        t = b + 1
        if len(collection) > int(1e7):
            newcollection = set()
            for i in collection:
                if i >= t:
                    newcollection.add(i)
            collection = newcollection
        while t <= N:
            if not t in collection:
                collection.add(t)
            else:
                available.add(t)
            t = t * b + 1
    return sum(available)

def run():
    return pr346(int(1e12))

if __name__ == "__main__":
    print run()

