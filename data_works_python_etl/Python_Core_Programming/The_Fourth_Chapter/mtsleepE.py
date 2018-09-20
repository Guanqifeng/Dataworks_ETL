import threading
from time import sleep,ctime


loops = [4,2]

class ThreadFunc(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)
def loop(nloop,nsec):
    print("Starting loop "+str(nloop)+" at:"+ctime())
    sleep(nsec)
    print("Loop "+str(nloop)+"Done at:"+ctime())

def main():
    print("Starting all loops at:"+ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = ThreadFunc(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print("All loops Done at:"+ctime())
if __name__ == '__main__':
    main()