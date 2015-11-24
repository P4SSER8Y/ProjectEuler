#encoding:utf8
from time import time
import re
import os

def run(problem):
    print "Solving Problem", problem
    print "===Calculating==="
    moduleName = 'pr' + str(1000 + problem)[1:]
    try:
        m = __import__(moduleName)
    except ImportError:
        print "the Problem is not done"
        return None, None

    t1 = time() * 1000
    try:
        answer = m.run()
        print "The answer is", answer
        print "Finished in",
    except KeyboardInterrupt:
        print "Interruped at",
    t2 = time() * 1000
    print int(t2 - t1), 'ms'
    print "===The End===\n"
    return answer, int(t2 - t1)

if __name__ == "__main__":
    print "Please Enter the Problem Number:",
    t = raw_input()
    if re.match(r'^\s*\d+\s*$', t):
        pn = int(t)
        if pn == 0:
            from pedb import PEDB
            db = PEDB()
            solved = sorted([int(x) for x in db.db.keys() if db.getProblem(x)['solved']])
            print "There are " + str(len(solved)) + " problems solved"
            t1 = time()
            for m in solved:
                ans, t = run(m)
                db.record(m, solved=True, time=t, answer=ans)
            t2 = time()
            db.writeFile()
            print "Finished all in " + str(int(t2-t1)) + 's'
        else:
            ans, t = run(pn)
            print "Is it correct?(y/[n])",
            if (raw_input()+' ')[0] in 'yY':
                from pedb import PEDB
                db = PEDB()
                db.record(pn, solved=True, time=t, answer=ans)
    else:
        pbs = [f for f in os.listdir('.') if re.match(r'^pr\d{3}\.py$', f)]
        pbs += [f for f in os.listdir('.') if re.match(r'^pr\d{3}$', f)]
        pbs.sort(cmp=lambda a, b: cmp(os.stat(a).st_mtime, os.stat(b).st_mtime), reverse=True)
        problem = int(re.findall(r'[1-9]\d*', pbs[0])[0])
        print "Select the latest one: Problem", problem
        ans, t = run(problem)
        print "Is it correct?(y/[n])",
        if (raw_input()+' ')[0] in 'yY':
            from pedb import PEDB
            db = PEDB()
            db.record(problem, solved=True, time=t, answer=ans)
            db.writeFile()
