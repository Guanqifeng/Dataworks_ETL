import _thread
from time import sleep,ctime

def loop0():
    print("Loop0 start at :"+ctime())
    sleep(4)
    print("Loop0 end at:"+ctime())

def loop1():
    print("Loop1 start at :"+ctime())
    sleep(2)
    print("Loop1 end at :"+ctime())

def main():
    print("Starting at:"+ctime())
    _thread.start_new_thread(loop0,())#start_new_thread第一个参数为函数名，不需要加“（）”
    _thread.start_new_thread(loop1,())
    sleep(6)
    print("All Done at:" + ctime())

if __name__ == "__main__":
    main();