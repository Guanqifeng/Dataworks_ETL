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
    loop0()
    loop1()
    print("All Done at:" + ctime())

if __name__ == "__main__":
    main();