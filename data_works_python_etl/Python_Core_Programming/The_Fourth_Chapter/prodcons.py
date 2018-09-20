from myThread import MyThread
from random import randint
from time import sleep
from queue import Queue

def writeQ(queue):
    print("producing object fo Q...")
    queue.put("xxx",1)
    print("Size Now:"+str(queue.qsize()))

def readQ(queue):
    val = queue.get(1)
    print("Consumed object from Q ... Size Now:"+str(queue.qsize()))

def writer(queue,loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))
def reader(queue,loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [reader,writer]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(q,nloops),funcs[1].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print("ALL Done!")

if __name__ == "__main__":
    main()
