#coding:utf8
from os import path

def crossProduct(A, B, C, D):
    x1 = B[0]-A[0]
    y1 = B[1]-A[1]
    x2 = D[0]-C[0]
    y2 = D[1]-C[1]
    return x1*y2-x2*y1

def pr102():
    f = open(path.split(path.realpath(__file__))[0]+'\\data102.txt', 'r')
    data = f.readlines()
    f.close()

    cnt = 0
    for i in xrange(len(data)):
        t = [int(x) for x in data[i].split(',')]
        P = (0, 0)
        A = (t[0], t[1])
        B = (t[2], t[3])
        C = (t[4], t[5])
        ABxAP = crossProduct(A, B, A, P)
        BCxBP = crossProduct(B, C, B, P)
        CAxCP = crossProduct(C, A, C, P)
        if ((ABxAP >= 0) and (BCxBP >= 0) and (CAxCP >= 0)) or \
           ((ABxAP <= 0) and (BCxBP <= 0) and (CAxCP <= 0)):
               cnt += 1
    return cnt

def run():
    return pr102()

if __name__ == "__main__":
    print run()

