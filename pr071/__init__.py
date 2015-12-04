from .pr071 import run as pyRun
from ctypes import *
from os.path import split, realpath
from platform import architecture

if architecture()[0] == "64bit": 
    cRun = CDLL(split(realpath(__file__))[0] + '\\pr071.dll').run
else:
    cRun = CDLL(split(realpath(__file__))[0] + '\\pr071_32.dll').run
cRun.argtypes = None
cRun.restype = c_long

#run = pyRun
run = cRun
