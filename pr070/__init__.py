from .pr070 import run as pyRun
from ctypes import CDLL
from os.path import split, realpath
from platform import architecture

try:
    if architecture()[0] == "64bit":
        cRun = CDLL(split(realpath(__file__))[0] + r'\pr070.dll').run
    else:
        cRun = CDLL(split(realpath(__file__))[0] + r'\pr070_32.dll').run 
    cRun.argtypes = c_long
    cRun.restype = c_long
except:
    pass

#run = pyRun
run = cRun
