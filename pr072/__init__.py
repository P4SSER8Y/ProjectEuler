from .pr072 import run as pyRun
from ctypes import CDLL, c_longlong
from os.path import split, realpath
from platform import architecture

try:
    if architecture()[0] == "64bit":
        cRun = CDLL(split(realpath(__file__))[0] + r'\pr072.dll').run
    else:
        cRun = CDLL(split(realpath(__file__))[0] + r'\pr072_32.dll').run
    cRun.argtypes = None
    cRun.restype = c_longlong
except:
    pass

#run = pyRun
run = cRun
