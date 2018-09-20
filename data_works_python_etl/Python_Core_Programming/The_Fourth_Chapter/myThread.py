import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args= args
    def run(self):
        print(self.name+" is Starting at:"+ctime())
        self.res = self.func(*self.args)
        print(self.name+" is Finished at:"+ctime())
    def getResult(self):
        return self.res