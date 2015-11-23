from pedb import PEDB

prefix = """\
Project Euler
=============
Solutions to [Project Euler](http://projecteuler.net/)

![my profile](https://projecteuler.net/profile/zqnchn.png)

Language
--------

+ mainly Python
+ C for acceleration

Engines
-------

+ PyPy 4.0.1 (Python 2.7)
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
    f.write('+ [' + str(1000+x)[1:] + ' ' + db.getProblem(x)['title'] + r'](http://projecteuler.net/problem=' + str(x) + ')\n')
    f.write('    - answer: ' + str(db.getProblem(x)['answer']) + ' \n')
    f.write('    - min used time: ' + str(db.getProblem(x)['time']) + ' ms\n\n')
f.flush()
f.close()
