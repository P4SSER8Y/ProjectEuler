#coding: utf8
from ctypes import *
import os

usr = CDLL(os.path.split(os.path.realpath(__file__))[0] + r'\usr.dll') 

def getPrimes(n):
    usr.getPrimes.argtypes = [c_long]
    usr.getPrimes.restype = POINTER(c_long)
    tmp = usr.getPrimes(n)
    return [tmp[x] for x in xrange(1, tmp[0]+1)]

usr.isPrime.argtypes = [c_long]
usr.isPrime.restype = c_bool
isPrime = usr.isPrime

def getFactors(n):
    usr.getFactors.argtypes = [c_long]
    usr.getFactors.restype = POINTER(c_long)
    tmp = usr.getFactors(n)
    return [tmp[x] for x in xrange(1, tmp[0] + 1)]

def getPrimeFactors(n):
    usr.getPrimeFactors.argtypes = [c_long]
    usr.getPrimeFactors.restype = POINTER(c_long)
    tmp = usr.getPrimeFactors(n)
    return [tmp[x] for x in xrange(1, tmp[0] + 1)]
