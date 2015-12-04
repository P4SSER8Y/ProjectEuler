#encoding:utf8

class PBarCMD(object):
    def __init__(self, maxval=100, minval=0):
        self.maxval = maxval - minval
        self.minval = minval
        self.curr = minval
        self.percent = 0

    def start(self):
        self.next = 0.01 * self.maxval + self.minval
        print("%3d%%\t\t%s\r" % (0, self.curr), end = "")
        return self

    def update(self, val):
        if val < self.next:
            return
        self.percent = (val - self.minval) / self.maxval
        self.next = (self.percent + 0.01) * self.maxval + self.minval
        self.curr = val
        print("%3d%%\t\t%s\r" % (int(self.percent * 100), self.curr), end = "")
        return None

    def finish(self):
        print()
        return None

PBar = PBarCMD
