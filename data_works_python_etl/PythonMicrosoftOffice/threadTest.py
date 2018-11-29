import threading
import time
class myThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        starTime = time.time()
        print(str(self.name)+'StartTime:'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        test(self.counter[0],self.counter[1])
        print('EndTime:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("共耗时："+str(time.time()-starTime))
def test(name1,name2):
    print(str(name1)+" AND "+str(name2))

def getThreadRecursion(num,realnum,listobj):
    if num == 1 or realnum - num == 3:
        myThread(num-1, 'Thread'+str(num-1), listobj[num-1]).start()
        return True
    else:
        num -= 1
        myThread(num,'Thread'+str(num),listobj[num]).start()
        getThreadRecursion(num, realnum, listobj)
if __name__ == '__main__':
    listObj = [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e'),(6,'f'),(7,'g'),(8,'h'),(9,'i'),(10,'j'),(11,'l')]
    getLengthAll = len(listObj)
    while getLengthAll >= 0:
        getThreadRecursion(getLengthAll,getLengthAll,listObj)
        getLengthAll -= 4