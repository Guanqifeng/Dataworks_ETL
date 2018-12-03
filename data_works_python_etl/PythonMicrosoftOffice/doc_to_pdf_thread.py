# -*- encoding: utf-8 -*-
import  os

import pythoncom
from win32com import client
from progressbar import *
import time
import threading



def pathExists(doc_path, pdf_path):
    if os.path.exists(doc_path) and os.path.exists(pdf_path):
        return True
    if os.path.exists(doc_path) and not os.path.exists(pdf_path):
        os.mkdir(pdf_path)
        return True
    if not os.path.exists(doc_path):
        return False

def getDocPathOfFileName(doc_path):
    return set(os.listdir(doc_path))

def doc2pdf(doc_file_path, pdf_file_path):
    """
    :word文件转pdf
    :param doc_file_path word文件路径
    :param pdf_file_path pdf文件路径
    """
    pythoncom.CoInitialize()
    try:
        word = client.DispatchEx("Word.Application")
        worddoc = word.documents.Open(doc_file_path, ReadOnly=1)
        worddoc.SaveAs(pdf_file_path, FileFormat=17)
        # 关闭
        worddoc.Close()
        del worddoc
    except Exception as e:
        print(str(e))
    finally:
        # 对com操作，一定要确保退出word应用
        if word:
            word.Quit()
        # 释放资源
        pythoncom.CoUninitialize()

def isDocFile(doc_name):
    if doc_name.endswith('.doc') or doc_name.endswith('.docx'):
        return True
    else:
        return False

class myThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        #doc2pdf(self.counter[0],self.counter[1])
        doc2pdf(self.counter[0],self.counter[1])



def getThreadRecursion(num,realnum,listobj,threads):

    if num == 1 or realnum - num == 100:
        thread_o = myThread(num-1, 'Thread'+str(num-1), listobj[num-1])
        threads.append(thread_o)
        thread_o.start()
        return True
    else:
        num -= 1
        thread_o = myThread(num,'Thread'+str(num),listobj[num])
        threads.append(thread_o)
        thread_o.start()
        getThreadRecursion(num, realnum, listobj,threads)
    return  threads

def wait_for_complete(threads):
    for item in threads:
        if item.isAlive():
            item.join()

def main(doc_path, pdf_path):
    starTime = time.time()
    print('StartTime:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    if pathExists(doc_path, ftp_path):
        getFileSet = getDocPathOfFileName(doc_path)
        file_path_list = [(doc_path+"\\"+str(filename),pdf_path+"\\"+str(filename.split(".")[0])+".pdf") for filename in getFileSet if isDocFile(filename)]
        #pdf_file_path_list = [pdf_path+"\\"+str(filename).split('.')[0]+'.pdf' for filename in getFileSet if isDocFile(filename)]
        # try:
        #     fileNums = len(file_path_list)
        #     while fileNums >= 0:
        #         threads = []
        #         get_threads = getThreadRecursion(fileNums, fileNums, file_path_list,threads)
        #         wait_for_complete(get_threads)
        #         fileNums -= 21
        # except:
        #     print("Error: unable to start thread")
        fileNums = len(file_path_list)
        while fileNums >= 0:
            threads = []
            get_threads = getThreadRecursion(fileNums, fileNums, file_path_list, threads)
            wait_for_complete(get_threads)
            fileNums -= 101
    else:
        print("Word存储路径："+doc_path+" 不存在，文件不进行转换！")
    print('EndTime:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    print('共耗时:' + str(time.time() - starTime))
# if len(sys.argv) < 3 or len(sys.argv) > 3:
#     print(len(sys.argv))
#     print(str(sys.argv))
#     print("传入参数有问题，需要两条参数（Excel文件路径 与 根目录）！")
#     sys.exit()
# else:
#     doc_path,ftp_path = sys.argv[1],sys.argv[2]
#     if pathExists(doc_path, ftp_path):
#         doc2pdf(doc_path, ftp_path)
if __name__=='__main__':
    doc_path = "C:\\Users\\Administrator\\Desktop\\test_file\\协议"
    ftp_path = "C:\\Users\\Administrator\\Desktop\\test_file\\协议PDF"
    main(doc_path, ftp_path)
