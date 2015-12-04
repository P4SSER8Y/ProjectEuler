from .pr071 import run as pyRun
from ctypes import *
from os.path import split, realpath

cRun = CDLL(split(realpath(__file__))[0] + '\\pr071.dll').run
cRun.argtypes = None
cRun.restype = c_long

#run = pyRun
run = cRun
