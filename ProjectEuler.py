#encoding:utf8
from pedb import PEDB
from time import time
from importlib import import_module
from sys import version
import re
import os
import sys

def run(problem):
    print()
    print("Problem", problem)
    db = PEDB()
    data = db.getProblem(problem)
    for x in data:
        print(x, ': ', data[x], sep = '')
    print()
    print("===Calculating===")
    moduleName = 'pr' + str(1000 + problem)[1:]
    #try:
    m = import_module(moduleName)
    #except ImportError as e:
    #    print("the Problem is not done")
    #    return None, None

    t1 = time() * 1000
    answer = None
    try:
        answer = m.run()
        print("The answer is", answer)
        print("Finished in ", end = "")
    except KeyboardInterrupt:
        print("Interruped at ", end = "")
    t2 = time() * 1000
    print(int(t2 - t1), 'ms')
    print("===The End===\n")
    return answer, int(t2 - t1)

if __name__ == "__main__":
    print(version)
    print()
    print("Please Enter the Problem Number: ", end = "")
    t = input()
    if re.match(r'^\s*\d+\s*$', t):
        pn = int(t)
        if pn == 0:
            db = PEDB()
            solved = sorted([int(x) for x in db.db.keys() if db.getProblem(x)['solved']])
            print("There are " + str(len(solved)) + " problems solved")
            t1 = time()
            for m in solved:
                ans, t = run(m)
                db.record(m, solved=True, time=t)
            t2 = time()
            db.writeFile()
            print("Finished all in " + str(int(t2-t1)) + 's')
        else:
            ans, t = run(pn)
            print("Is it correct?(y/[n])", end = " ")
            if (input()+' ')[0] in 'yY':
                db = PEDB()
                db.record(pn, solved=True, time=t, answer=ans)
    else:
        pbs = [f for f in os.listdir('.') if re.match(r'^pr\d{3}\.py$', f)]
        pbs += [f for f in os.listdir('.') if re.match(r'^pr\d{3}$', f)]
        pbs.sort(key=lambda x: os.stat(x).st_mtime, reverse=True)
        problem = int(re.findall(r'[1-9]\d*', pbs[0])[0])
        print("Select the latest one: Problem", problem)
        ans, t = run(problem)
        print("Is it correct?(y/[n])", end = " ")
        if (input()+' ')[0] in 'yY':
            db = PEDB()
            db.record(problem, solved=True, time=t, answer=ans)
            db.writeFile()
