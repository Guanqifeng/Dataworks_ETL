import os
import sys
import shutil

def create_folder(path):
    fileList = []
    compnyFolder = []
    personFolder = []
    if os.path.exists(path):
        # 创建目录
        if os.path.exists(path + r"\\" + "公司-无excel"):
            for foldername in os.listdir(path + r"\\" + "公司-无excel"):
                for filename in os.listdir(path + r"\\" + "公司-无excel"+r"\\"+foldername):
                    os.remove(os.path.join(path + "\\" + "公司-无excel"+"\\"+foldername+"\\",filename))
                os.rmdir(path + "\\" + "公司-无excel"+"\\"+foldername)
            os.rmdir(path + "\\" + "公司-无excel")
            os.mkdir(path + r"\\" + "公司-无excel")
            companypath = path + "\\" + "公司-无excel"
        else:
            os.mkdir(path + r"\\" + "公司-无excel")
            companypath = path + "\\" + "公司-无excel"

        if os.path.exists(path + r"\\" + "个人-无excel"):
            for foldername in os.listdir(path + r"\\" + "个人-无excel"):
                for filename in os.listdir(path + r"\\" + "个人-无excel"+r"\\"+foldername):
                    os.remove(os.path.join(path + "\\" + "个人-无excel"+"\\"+foldername+"\\",filename))
                os.rmdir(path + "\\" + "个人-无excel"+"\\"+foldername)
            os.rmdir(path + "\\" + "个人-无excel")
            os.mkdir(path + r"\\" + "个人-无excel")
            personpath = path + "\\" + "个人-无excel"
        else:
            os.mkdir(path + r"\\" + "个人-无excel")
            personpath = path + "\\" + "个人-无excel"
        #移动文件
        getFolderList = os.listdir(path)
        getFolderList.remove('个人-无excel')
        getFolderList.remove('公司-无excel')
        for folderName in getFolderList:
            for filename in os.listdir(path+r"\\"+folderName):
                fileList.append(path+"\\"+folderName+"\\"+filename)
        for rfilename in fileList:
            rpath,rname = os.path.split(rfilename)
            if str(rname).__contains__("公司"):
                compnyFolder.append(rpath)
            else:
                personFolder.append(rpath)
        for folder in set(compnyFolder):
            fpath, fname = os.path.split(folder)
            shutil.copytree(folder, companypath + "\\" + fname)
        for folder in set(personFolder)-set(compnyFolder):
            fpath, fname = os.path.split(folder)
            shutil.copytree(folder, personpath + "\\" + fname)
    else:
        print("目录不存在："+str(path))

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(len(sys.argv))
    print(str(sys.argv))
    print("传入参数有问题，需要两条参数（Excel文件路径 与 Word文件路径）！")
    sys.exit()
else:
    root_path = sys.argv[1]
    create_folder(root_path)
# if __name__ == '__main__':
#     root_path = 'C:\\Users\\Administrator\\Desktop\\1119公司资料拆分需求-gqf'
#     create_folder(root_path)

