import os
from pr206 import run as pyRun
from ctypes import CDLL, c_longlong

cRun = CDLL(os.path.split(os.path.realpath(__file__))[0] + r'\pr206.dll').run
cRun.argtypes = None
cRun.restype = c_longlong

run = cRun


