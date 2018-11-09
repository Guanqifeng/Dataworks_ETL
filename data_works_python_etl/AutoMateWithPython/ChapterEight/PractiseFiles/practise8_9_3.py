#匹配每 3 位就有一个逗号的数字？
import re
import os
def get_files_from_folder(folderpath):
    getRe = re.compile('^([a-zA-Z_]+?)([a-zA-Z0-9]*?)(\\.txt$)')
    getFiles = []
    if os.path.isdir(folderpath):
        for filepath in os.listdir(folderpath):
            if getRe.search(filepath):
                getFiles.append(getRe.search(filepath).group(0))
        for file in getFiles:
            with open(folderpath+"\\"+file) as fileobj:
                print(fileobj.read())
if __name__ == '__main__':
    folderpath = '..\\resource'
    get_files_from_folder(folderpath)
