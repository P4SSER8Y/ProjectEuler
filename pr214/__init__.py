from .pr214 import run as pyRun
from ctypes import CDLL
from os.path import split, realpath

try:
    cRun = CDLL(split(realpath(__file__))[0] + r'\pr214.dll').run
    cRun.argtypes = None
    cRun.restype = None
except:
    pass

run = pyRun
#run = cRun
