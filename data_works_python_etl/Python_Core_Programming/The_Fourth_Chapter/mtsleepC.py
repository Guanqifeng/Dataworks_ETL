import threading
from time import ctime,sleep

loops = [4,2]

def loop(nloop,nsec):
    print("Starting loop "+str(nloop)+" at: "+ctime())
    sleep(nsec)
    print("loop " + str(nloop) + "Done at: " + ctime())

def main():
    print("Starting at "+ctime())
    threads = []
    nloops = range(len(loops)) # 0,1

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print("All thread Done at :"+ctime())

if __name__ == '__main__':
    main();