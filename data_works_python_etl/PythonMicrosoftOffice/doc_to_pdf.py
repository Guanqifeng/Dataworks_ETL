# -*- encoding: utf-8 -*-
import  os
from win32com import client
from progressbar import *
import time
def pathExists(doc_path, pdf_path):
    if os.path.exists(doc_path) and os.path.exists(pdf_path):
        return True
    if os.path.exists(doc_path) and not os.path.exists(pdf_path):
        os.mkdir(pdf_path)
        return True
    if not os.path.exists(doc_path):
        return False

def doc2pdf(doc_path, pdf_path):
    """
    :word文件转pdf
    :param doc_name word文件名称
    :param pdf_name 转换后pdf文件名称
    """
    try:
        progress = ProgressBar()
        fileList = set(os.listdir(doc_path))
        word = client.DispatchEx("Word.Application")
        for filename in progress(fileList):
            if filename.endswith('.doc') or filename.endswith('.docx'):
                worddoc = word.Documents.Open(doc_path + r"\\" + filename, ReadOnly=1)
                if filename.endswith('.doc'):
                    pdfFileName = filename.replace('.doc', '.pdf')
                else:
                    pdfFileName = filename.replace('.docx', '.pdf')
                if os.path.exists(pdf_path + r"\\" + pdfFileName):
                    os.remove(pdf_path + r"\\" + pdfFileName)
                worddoc.SaveAs(pdf_path + r"\\" + pdfFileName, FileFormat=17)
                worddoc.Close()
                del worddoc
            else:
                print(filename + "is not a word file!")
    except Exception as e:
        print("Doc To Pdf Error"+str(e))

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
    starTime = time.time()
    doc_path = "C:\\Users\\Administrator\\Desktop\\test_file\\协议"
    ftp_path = "C:\\Users\\Administrator\\Desktop\\test_file\\协议PDF"
    if pathExists(doc_path, ftp_path):
        print('StartTime:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        doc2pdf(doc_path, ftp_path)
        print('EndTime:' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("共耗时：" + str(time.time() - starTime))
    else:
        print("Word存储路径："+doc_path+" 不存在，文件不进行转换！")