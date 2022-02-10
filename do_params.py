
from progressing import Progressing
import time
def task(param):
    print('task: ',param)
    time.sleep(0.1)

with open('params.txt') as f: 
    p = Progressing()
    i = 0
    for line in f:
        if  p.now == i:
            if line[-1] == '\n':
                param = line[:-1]
            else:
                param = line
            
            task(param)
            p.tick()
        i = i+1
    p.done()
