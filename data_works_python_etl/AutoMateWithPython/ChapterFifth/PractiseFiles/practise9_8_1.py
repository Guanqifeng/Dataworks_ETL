#编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg）。
#不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中。
import  shutil,re,os
def find_all_file(inputpath):
    getRe = re.compile(r'(.*?)(.txt$)')
    getAllFilePath = []
    getSpecialFilePath = []
    for foldername,subfoldername,filenames in os.walk(inputpath):
        for filename in filenames:
            if foldername.endswith('\\'):
                getAllFilePath.append(foldername.replace('\\',r'\\')+filename)
            else:
                getAllFilePath.append((foldername+"\\").replace('\\',r'\\')+filename)
    for i in getAllFilePath:
        if getRe.match(i):
            getSpecialFilePath.append(getRe.match(i).group(0))
    return getSpecialFilePath
def remove_file_to_new_folder(inputpath,filepathlist):
    newOutputPath = inputpath + "NewFolder"
    os.mkdir(newOutputPath)
    if isinstance(filepathlist,list):
        for filepath in filepathlist:
            try:
                shutil.copy(filepath,newOutputPath+filepath[filepath.rfind(r'\\')+1:])
            except Exception as e:
                print("Move File Error Is :" + str(e))
if __name__ == '__main__':
    inputpath = '..\\resource\\'
    getfilepathlist = find_all_file(inputpath)
    remove_file_to_new_folder(inputpath,getfilepathlist)