import os
import sys
def batch_of_replace_name(rootpath):
    #give me a root path
    if os.path.exists(rootpath):
        getFolderList = os.listdir(rootpath)
        getFileList = [rootpath+"\\"+foldername+"\\"+''.join(os.listdir(rootpath+"\\"+foldername)) for foldername in getFolderList]
        for filepath in getFileList:
            getrpath,replacename = os.path.split(filepath)
            os.rename(filepath,getrpath+r'\\'+'1.jpg')

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(len(sys.argv))
    print(str(sys.argv))
    print("传入参数有问题，需要两条参数（Excel文件路径 与 Word文件路径）！")
    sys.exit()
else:
    root_path = sys.argv[1]
    batch_of_replace_name(root_path)
# if __name__ == '__main__':
#     rootpath = 'C:\\Users\\Administrator\\Desktop\\资料'
#     batch_of_replace_name(rootpath)