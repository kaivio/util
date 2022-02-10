# 持久化进度记录器

import dbm
import atexit
import sys

db = dbm.open('.progressing.catch','c')
atexit.register(db.close)

class Progressing():
    def __init__(self,key=sys.argv[0],total=0):
        i = db.get(key,0)
        self.now = int(i)
        self.total = total
        self.key = key

    def update(self,i):
        self.now = i
        db[self.key] = str(i)
    
    def tick(self):
        self.update(self.now+1)
    
    def clear(self):
        del db[self.key]


def task_queue(func,iterable,key=None,once=False):
    key = key or sys.argv[0]+func.__name__
    p = Progressing(key)
    i = 0
    for args in iterable:
        if  p.now == i: 
            func(*args)
            p.tick()
        i = i+1
    if not once:
        p.clear()
