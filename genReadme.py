#coding:utf8
from pedb import PEDB

import os, re

prefix = """\
Project Euler
=============
Solutions to [Project Euler](http://projecteuler.net/)

Language
--------

+ mainly Python
+ C for acceleration

Engines
-------

+ PyPy 4.0.1 (Python 2.7)
+ gcc (with -O3 enabled)
+ My Computer
    - Windows 10 64-bit
    - CPU: Intel® Core™ i5-3210M CPU @ 2.5GHz (2 Cores 4 Threads)
    - RAM: 4GB

Requirements
============
- itertools
- progressbar
- ctypes(with gcc, make)
- fractions
- math

Solved Problems
===============
"""

db = PEDB()
f = open('README.md', 'w')
f.write(prefix)
for x in db.getSolvedProblems():
    f.write('+ [' + str(1000+x)[1:] + ' ' + db.getProblem(x)['title'] + r']('+ str(1000+x)[1:]+ ')[:link:](http://projecteuler.net/problem=' + str(x) + ')  ')
    if db.getProblem(x)['time'] > 60000:
        f.write(":warning: ")
    if db.getProblem(x)['time'] < 10:
        f.write(":trollface:")
    if os.path.exists('pr'+str(1000+x)[1:]+'\\algo.md'):
        f.write(":thought_balloon:")
    f.write("\n\n")
    f.write('    - answer: ' + str(db.getProblem(x)['answer']) + ' \n')
    f.write('    - min used time: ' + str(db.getProblem(x)['time']) + ' ms\n\n')

    rm = open('pr'+str(1000+x)[1:]+'\\README.md', 'w')
    rm.write(str(1000+x)[1:] + ' ' + db.getProblem(x)['title'] + r'[:link:](http://projecteuler.net/problem=' + str(x) + ')  ')
    if db.getProblem(x)['time'] > 60000:
        rm.write(":warning:")
    if db.getProblem(x)['time'] < 10:
        rm.write(":trollface:")
    if os.path.exists('pr'+str(1000+x)[1:]+'\\algo.md'):
        rm.write(":thought_balloon:")
    rm.write("\n")
    rm.write('========================\n\n')
    rm.write('- answer: ' + str(db.getProblem(x)['answer']) + ' \n')
    rm.write('- min used time: ' + str(db.getProblem(x)['time']) + ' ms\n\n')

    if os.path.exists('pr'+str(1000+x)[1:]+'\\algo.md'):
        rm.write("Algorithm\n=========\n\n")
        algo = open('pr'+str(1000+x)[1:]+'\\algo.md', 'r')
        rm.write(algo.read())
        algo.close()
    rm.flush()
    rm.close()
f.flush()
f.close()
