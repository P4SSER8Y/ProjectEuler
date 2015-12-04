from .pr073 import run as pyRun
from ctypes import CDLL, c_long
from os.path import split, realpath
from platform import architecture

try:
    if architecture()[0] == "64bit":
        cRun = CDLL(split(realpath(__file__))[0] + r'\pr073.dll').run
    else:
        cRun = CDLL(split(realpath(__file__))[0] + r'\pr073_32.dll').run
    cRun.argtypes = None
    cRun.restype = c_long
except:
    pass

#run = pyRun
run = cRun
