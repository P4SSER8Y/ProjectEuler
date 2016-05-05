#coding: utf8
from ctypes import *
import platform
import os

if platform.system() == 'Windows':
    if platform.architecture()[0] == "64bit":
        usr = CDLL(os.path.split(os.path.realpath(__file__))[0] + r'\usr.dll') 
    else:
        usr = CDLL(os.path.split(os.path.realpath(__file__))[0] + r'\usr_32.dll') 
elif platform.system() == 'Linux':
    usr = CDLL(os.path.split(os.path.realpath(__file__))[0] + r'/usr.so')


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

usr.gcd.argtypes = [c_long, c_long]
usr.gcd.restype = c_long

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

def gcd(a, b):
    return usr.gcd(a, b)
