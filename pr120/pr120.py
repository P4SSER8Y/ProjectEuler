#coding:utf8

def pr120():
    ret = 0
    for a in xrange(3, 1001):
        ret += 2*a*((a-1)/2)
    return ret

def run():
    return pr120()

if __name__ == "__main__":
    print run()

