# -*- encoding: utf-8 -*-
import  os
from win32com import client
from progressbar import *
import time
import threading

word = client.DispatchEx("Word.Application")

class myThread(threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        doc2pdf(self.counter[0],self.counter[1])

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
    try:
        worddoc = word.Documents.Open(doc_file_path, ReadOnly=1)
        worddoc.SaveAs(pdf_file_path, FileFormat=17)
        worddoc.Close()
        del worddoc
    except Exception as e:
        print("Doc To Pdf Error" + str(e))

def isDocFile(doc_name):
    if doc_name.endswith('.doc') or doc_name.endswith('.docx'):
        return True
    else:
        return False

def main(doc_path, pdf_path):
    starTime = time.time()
    if pathExists(doc_path, ftp_path):
        getFileSet = getDocPathOfFileName(doc_path)
        file_path_list = [(doc_path+"\\"+str(filename),pdf_path+"\\"+str(filename.split(".")[0])+".pdf") for filename in getFileSet if isDocFile(filename)]
        #pdf_file_path_list = [pdf_path+"\\"+str(filename).split('.')[0]+'.pdf' for filename in getFileSet if isDocFile(filename)]
        try:
            fileNames = len(file_path_list)
            while fileNames>=6:
                myThread((fileNames - 1) % 6,"Thread"+str((fileNames - 1) % 6),file_path_list[fileNames - 1]).start()
                myThread((fileNames - 2) % 6,"Thread"+str((fileNames - 2) % 6),file_path_list[fileNames - 2]).start()
                myThread((fileNames - 3) % 6,"Thread"+str((fileNames - 3) % 6),file_path_list[fileNames - 3]).start()
                myThread((fileNames - 4) % 6,"Thread"+str((fileNames - 4) % 6),file_path_list[fileNames - 4]).start()
                myThread((fileNames - 5) % 6,"Thread"+str((fileNames - 5) % 6),file_path_list[fileNames - 5]).start()
                myThread((fileNames - 6) % 6,"Thread"+str((fileNames - 6) % 6),file_path_list[fileNames - 6]).start()
                fileNames -= 6
            while fileNames >= 0 & fileNames< 6:
                myThread(fileNames,"Thread"+str(fileNames),file_path_list[fileNames]).start()
                fileNames -= 1
        except:
            print("Error: unable to start thread")
    else:
        print("Word存储路径："+doc_path+" 不存在，文件不进行转换！")

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
