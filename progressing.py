import time
import os


class Progressing():
    def __init__(self,file=f'{__file__}.progressing',total=0):
        self.now = 0
        self.total = total
        self.file = file
        try:
            self.fd = open(file,'r+')
            self.now = int(self.fd.read())
        except FileNotFoundError as e:
            self.fd = open(file,'w+')

    
    def update(self,i):
        self.now = i
        self.fd.seek(0)
        self.fd.write(str(i))
        self.fd.flush()

    def tick(self):
        self.update(self.now+1)
    
    def done(self):
        self.fd.close()
        os.remove(self.file)
        
    def __del__(self):
        self.fd.close()

def main():
    p = Progressing()
    for i in range(100):
        if i < p.now:
            continue
        p.tick()
        print(i)
        time.sleep(0.1)

    p.done()


main()
