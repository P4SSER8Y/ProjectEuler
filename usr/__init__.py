#coding: utf8
from ctypes import *
import os

usr = CDLL(os.path.split(os.path.realpath(__file__))[0] + r'\usr.dll') 

usr.isPrime.argtypes = [c_long]
usr.isPrime.restype = c_bool

usr.getPrimes.argtypes = [c_long]
usr.getPrimes.restype = POINTER(c_long)

usr.getFactors.argtypes = [c_long]
usr.getFactors.restype = POINTER(c_long)

usr.getPrimeFactors.argtypes = [c_long]
usr.getPrimeFactors.restype = POINTER(c_long)

usr.isPrimeMR.argtypes = [c_longlong]
usr.isPrimeMR.restype = c_bool

def getPrimes(n):
    tmp = usr.getPrimes(n)
    return [tmp[x] for x in range(1, tmp[0]+1)]

def isPrime(n):
    return usr.isPrime(n)

def isPrimeMR(n):
    return usr.isPrimeMR(n)

def getFactors(n):
    tmp = usr.getFactors(n)
    return [tmp[x] for x in range(1, tmp[0] + 1)]

def getPrimeFactors(n):
    tmp = usr.getPrimeFactors(n)
    return [tmp[x] for x in range(1, tmp[0] + 1)]
