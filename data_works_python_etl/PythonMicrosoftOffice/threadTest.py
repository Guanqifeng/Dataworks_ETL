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
        print('StartTime:'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        test(self.counter[0],self.counter[1])
        print('EndTime:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("共耗时："+str(time.time()-starTime))
def test(name1,name2):
    print(name1+" AND "+name2)

if __name__ == '__main__':
    myThread(1, 'Thread1', ['test1','test2']).start()
    myThread(2, 'Thread2', ['test3', 'test4']).start()