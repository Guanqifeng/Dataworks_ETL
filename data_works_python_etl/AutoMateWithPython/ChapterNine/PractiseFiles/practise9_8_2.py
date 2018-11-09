#匹配每 3 位就有一个逗号的数字？
import re
import os
import send2trash
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

def delete_big_file(filelist):
    for filepath in filelist:
        if os.path.getsize(filepath) > 10000:
            send2trash.send2trash(filepath)
if __name__ == '__main__':
    folderpath = '..\\resource'
    getAllFileList = find_all_file(folderpath)
    delete_big_file(getAllFileList)