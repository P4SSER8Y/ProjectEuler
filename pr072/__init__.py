from .pr072 import run as pyRun
from ctypes import CDLL, c_longlong
from os.path import split, realpath

try:
    cRun = CDLL(split(realpath(__file__))[0] + r'\pr072.dll').run
    cRun.argtypes = None
    cRun.restype = c_longlong
except:
    pass

#run = pyRun
run = cRun
