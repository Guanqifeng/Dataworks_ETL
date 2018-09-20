from atexit import register
from random import randrange
from threading import Thread,currentThread,Lock
from time import ctime,sleep

class CleanOutPutSet(set):
    def __str__(self):
        return ','.join(x for x in self)

loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutPutSet()
lock = Lock()
def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print("%s Started %s"%(ctime(),myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    print("%s Completed %s (%d secs)"%(ctime(),myname,nsec))
    remaining.remove(myname)
    print("\n  (remaining:%s)"%(remaining or 'NONE'))
    lock.release()
def main():
    for pause in loops:
        Thread(target=loop,args=(pause,)).start()
@register
def _atexit():
    print("all Done at : "+ctime())

if __name__ == '__main__':
    main()

