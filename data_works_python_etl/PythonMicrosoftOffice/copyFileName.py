import os,sys
import xlsxwriter as xlsxwriter
from progressbar import *
def getFileName(rootPath):
    if os.path.exists(rootPath):
        # for root, dirs, files in os.walk(rootPath, topdown=False):
        #     print(dirs)
        #     # dirs=str(dirs).replace('\\',r'\\')
        #     # rPath,folderName=os.path.split(dirs)
        #     # print(str(folderName))
        #     # for name in files:
        #     #     print(os.path.join(root, name))
        #     # for name in dirs:
        #     #     print( name)
        if 'data.xls' in os.listdir(rootPath):
            get_filename_list = os.listdir(rootPath)
            get_filename_list.remove('data.xls')
        else:
            get_filename_list = os.listdir(rootPath)
        return get_filename_list
def copyNameToExcel(FileNameList,rootPath):
    n = 0
    progress = ProgressBar()
    workbook = xlsxwriter.Workbook(rootPath+"\\"+'data.xls')
    worksheet = workbook.add_worksheet('文件名')
    if FileNameList:
        for FileName in progress(FileNameList):
            worksheet.write(n, 0, FileName)
            n += 1
    workbook.close()

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(len(sys.argv))
    print(str(sys.argv))
    print("传入参数有问题，需要两条参数（根路径）！")
    sys.exit()
else:
    root_path = sys.argv[1]
    fileNameList = getFileName(root_path)
    copyNameToExcel(fileNameList, root_path)

# if __name__=='__main__':
#     rootPath = 'C:\\Users\\Administrator\\Desktop\\test'
#     fileNameList = getFileName(rootPath)
#     copyNameToExcel(fileNameList,rootPath)