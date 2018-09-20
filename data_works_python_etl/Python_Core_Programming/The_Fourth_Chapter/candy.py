from atexit import register
from threading import BoundedSemaphore,Thread,Lock
from time import ctime,sleep
from random import randrange

lock = Lock()
MAX = 5
candy = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print("Refilling Candy....")
    try:
        candy.release()
    except ValueError :
        print("Full Skipping!")
    else:
        print("OK")
    lock.release()
def buy():
    lock.acquire()
    print("Buying Candy...")
    if candy.acquire(False):
        print("OK")
    else:
        print("Empty Skipping!")
    lock.release()
def product(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))
def customer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def main():
    print("Starting at:"+ctime())
    nloops = randrange(2,6)
    print("The Candy Mechine (full with %d bars)"%MAX)
    Thread(target=customer,args=(randrange(nloops,nloops+MAX+2),)).start()
    Thread(target=product,args=(nloops,)).start()

@register
def _atexit():
    print("All Done at:"+ctime())

if __name__=="__main__":
    main();
