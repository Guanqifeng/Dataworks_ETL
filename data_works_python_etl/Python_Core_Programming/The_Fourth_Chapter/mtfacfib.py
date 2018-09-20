from myThread import MyThread
from time import ctime,sleep

def fib(x):
    sleep(0.005)
    if x< 2: return 1
    return fib(x-2)+fib(x-1)
def fac(x):
    sleep(0.1)
    if x < 2 : return 1
    return x*fac(x-1)
def sum(x):
    sleep(0.02)
    if x < 2 : return 1
    return x+sum(x-1)

funcs = [fib,fac,sum]
n = 12

def main():
    nfuncs = range(len(funcs))
    print("****Single Thread Starting at:"+ctime())
    for i in nfuncs:
        print("Function "+str(funcs[i].__name__)+"is Starting at :"+ctime())
        print(funcs[i](n))
        print("Function " + str(funcs[i].__name__) + "is Done at :" + ctime())
    print("****Single Thread Done at:"+ctime())

    print("\n****Multiple Threads Starting at:"+ctime())
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
    print("All Done")

if __name__ == '__main__':
    main()

