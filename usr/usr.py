#coding:utf8
from ctypes import *

if __name__ == "__main__":
    usr = CDLL('usr.dll')
    usr.getFactors.argtypes = [c_long]
    usr.getFactors.restype = POINTER(c_long)
    test = usr.getFactors(100000000)
    print(test[0])
