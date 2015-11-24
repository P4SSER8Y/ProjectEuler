from pr071 import run as pyRun
from ctypes import CDLL, c_long
from os.path import split, realpath

try:
    cRun = CDLL(split(realpath(__file__))[0] + r'\pr071.dll').run
    cRun.argtypes = None
    cRun.restype = c_long
except:
    pass

#run = pyRun
run = cRun
