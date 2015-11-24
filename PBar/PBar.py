#encoding:utf8
import progressbar

class PBarCMD(object):
    def __init__(self, maxval=100):
        self.maxval = maxval
        widgets = [progressbar.Percentage(), progressbar.widgets.Bar(),' ' , progressbar.widgets.Counter()]
        self.p = progressbar.ProgressBar(maxval = self.maxval, widgets= widgets)

    def start(self):
        self.p.start()
        return self

    def update(self, val):
        self.p.update(val)
        return None

    def finish(self):
        self.p.finish()
        return None

PBar = PBarCMD
