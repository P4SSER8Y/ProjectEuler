import json
import os

class PEDB(object):
    def __init__(self, dbFile = 'db.json'):
        self.dbFile = dbFile
        if os.path.exists(self.dbFile):
            f = open(self.dbFile, 'r')
            self.db = json.load(f)
            f.close()
        else:
            self.db = {}
    def record(self, num, solved=100, time=-1, title=None, answer=None):
        t = self.db.get(str(num), {})
        if solved != 100:
            t['solved'] = solved
        if time >= 0:
            t['time'] = min(time, t.get('time', 2147483647))
        if title:
            t['title'] = title
        if answer:
            t['answer'] = str(answer)
        self.db[str(num)] = t
    def writeFile(self):
        f = open(self.dbFile, 'w')
        f.write(json.dumps(self.db, indent=4, sort_keys=True))
        f.flush()
        f.close()
    def getProblem(self, n):
        return self.db.get(str(n), None)
    def getSolvedProblems(self):
        return sorted([int(x) for x in self.db.keys() if self.db[x]['solved']])
