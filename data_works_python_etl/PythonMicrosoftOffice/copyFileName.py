import os
import xlwt
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
        return os.listdir(rootPath)
def copyNameToExcel(FileNameList,rootPath):
    file = xlwt.Workbook(encoding='utf-8')
    # 指定file以utf-8的格式打开
    table = file.add_sheet('data')
    if FileNameList:
        for FileName in FileNameList:
            table.write(FileName,'123')
    file.save(rootPath+r"\\"+'data.xls')

if __name__=='__main__':
    rootPath = 'C:\\Users\\lenovo\\Desktop\\test'
    fileNameList = getFileName(rootPath)
    copyNameToExcel(fileNameList,rootPath)