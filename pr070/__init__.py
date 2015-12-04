from .pr070 import run as pyRun
from ctypes import CDLL
from os.path import split, realpath

try:
    cRun = CDLL(split(realpath(__file__))[0] + r'\pr070.dll').run
    cRun.argtypes = c_long
    cRun.restype = c_long
except:
    pass

#run = pyRun
run = cRun
