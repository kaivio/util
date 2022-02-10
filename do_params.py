
from progressing import Progressing,task_queue
import time
def task(param):
    print('task: ',param)
    time.sleep(0.1)

with open('params.txt') as f: 
    params = []
    for line in f.read().split('\n'):
        params.append([line])

    task_queue(task,params)

