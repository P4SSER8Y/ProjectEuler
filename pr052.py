from itertools import count

def run():
    for x in count(1):
        if len(str(6*x)) > len(str(x)): continue
        s = str(x)
        flag = True
        for y in str(2*x)+str(3*x)+str(4*x)+str(5*x)+str(6*x):
            if not y in s:
                flag = False
                break
        if flag:
            break
    print
    return x

if __name__ == "__main__":
    print run()

