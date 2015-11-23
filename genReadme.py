from pedb import PEDB

prefix = """\
Project Euler
=============
Solutions to http://projecteuler.net/

Language
--------

+ mainly Python
+ C for acceleration

Engines
-------

+ mainly Pypy 4.0.1 (Python 2.7)
+ gcc (with -O3 enabled)

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
    f.write('+ ' + str(1000+x)[1:] + ' ' + db.getProblem(x)['title'] + '\n')
    f.write('    - min used time: ' + str(db.getProblem(x)['time']) + ' ms\n\n')
f.flush()
f.close()
