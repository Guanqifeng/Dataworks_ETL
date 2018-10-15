import os
import shutil

def readAllFileName(sourcefolderpath):
    '''
    Return All Of Filename That In The Path
    :param sourcefolderpath: SourceFolderPath
    :return: A List Of Filename
    '''
    AllFileNameList = os.listdir(sourcefolderpath)#得到文件夹下的所有文件名称
    return AllFileNameList
def ruleOfSamePrefix(sourcefolderpath,filenamelist,prefix,iscasesensitive):
    '''
    Designation Prefix to Classify The Files
    :param sourcefolderpath:SourceFolderPath
    :param filenamelist:A List Of Filename From SourceFolderPath
    :param prefix:Classify Prefix
    :param iscasesensitive: Is Case Sensitive Or Not （True or False）
    :return:Classify Folder Path and File Path That Will Be Moved
    '''
    outPutFolderPath = sourcefolderpath+"\\"+prefix
    moveFileList = []
    if filenamelist:
        for filename in filenamelist:
            if iscasesensitive:
                if str(prefix) and filename.replace(' ', '')[0:len(prefix)] == str(prefix):
                    moveFileList.append(sourcefolderpath + "\\" + filename)
            else:
                if str(prefix).lower() and str(filename).replace(' ', '').lower()[0:len(prefix)] == str(prefix).lower():
                    moveFileList.append(sourcefolderpath + "\\" + filename)
    else:
        print("Input Parameter Filename List Is None!(FileNameList:{0}) ".format(filenamelist))
    return outPutFolderPath,moveFileList
def ruleOfContain(sourcefolderpath,filenamelist,containinfo,iscasesensitive):
    '''
    Designation Contain to Classify The Files
    :param sourcefolderpath:SourceFolderPath
    :param filenamelist:A List Of Filename From SourceFolderPath
    :param containinfo:Classify Contain
    :param iscasesensitive: Is Case Sensitive Or Not （True or False）
    :return:Classify Folder Path and File Path That Will Be Moved
    '''
    outPutFolderPath = sourcefolderpath + "\\" + containinfo
    moveFileList = []
    if filenamelist:
        for filename in filenamelist:
            if iscasesensitive:
                if str(containinfo) and str(containinfo) in str(filename).replace(' ', ''):
                    moveFileList.append(sourcefolderpath + "\\" + filename)
            else:
                if str(containinfo).lower() and str(containinfo).lower() in str(filename).replace(' ', '').lower():
                    moveFileList.append(sourcefolderpath + "\\" + filename)
    else:
        print("Input Parameter Filename List Is None!(FileNameList:{0}) ".format(filenamelist))
    return outPutFolderPath, moveFileList
def moveFileToFolder(newfolderpath,movefilepathlist):
    '''
    Save The File That Will Be Moved In To Classify Folder Path
    :param newfolderpath: Classify Folder Path
    :param movefilepathlist: A List Of File Paths That Will Be Moved
    :return: Move Successful
    '''
    if newfolderpath and movefilepathlist:
        getNewFolderPath,getMoveFilePathList = newfolderpath,movefilepathlist
        if os.path.exists(getNewFolderPath):
            pass
        else:
            os.mkdir(getNewFolderPath)  # 创建文件夹
        for filenamepath in getMoveFilePathList:
            try:
                shutil.move(filenamepath,getNewFolderPath)  #移动文件到指定目录下
            except IOError as e:
                print(e)
    else:
        print("Input Parameter NewFolderPath or MoveFileList Is None!(NewFolderPath:{0} ,MoveFileList:{1} )".format(newfolderpath,movefilelist))
def main(sourcefolderpath,rule = 1,containinfolist = [],prefixlist = [],iscasesensitive=False):
    '''
    Main Function
    :param sourcefolderpath: SourceFolderPath
    :param rule: Rule Of Classify (Default Is 1 =>"Prefix Classify")
    :param containinfolist:A List Of Contain Classify (Default Is [])
    :param prefixlist:A List Of Prefix Classify (Default Is [])
    :param iscasesensitive:Is Case Sensitive Or Not (Default Is False =>Not Case Sensitive)
    :return:Execute Successful
    '''
    try:
        if os.path.exists(sourcefolderpath):
            filesList = readAllFileName(sourcefolderpath)
            if rule != 1 and containinfolist:
                for containinfo in containinfolist:
                    pass
                    getOutPutFolderPath, getMoveFileList = ruleOfContain(sourcefolderpath,filesList,containinfo,iscasesensitive)
                    moveFileToFolder(getOutPutFolderPath, getMoveFileList)
            elif rule == 1 and prefixlist:
                for prefix in prefixlist:
                    getOutPutFolderPath,getMoveFileList = ruleOfSamePrefix(sourcefolderpath,filesList,prefix,iscasesensitive)
                    moveFileToFolder(getOutPutFolderPath, getMoveFileList)
            else:
                print("Input Parameter Rule is : {0} and ClassifyList is :{1} or {2} \nThe Input Info Is Not Compliance!".format(rule,containinfolist,prefixlist))
        else:
            raise Exception("路径不存在，请查证："+str(sourcefolderpath))
    except Exception as e:
        print("异常信息："+e)

if __name__ == '__main__':
    sourcefolderpath = 'C:\\Users\\Administrator\\Desktop\\ExcelTest2' #指定待处理的文件存放路径
    ######前缀匹配归类
    # rule = 1 #归类规则 ，1：前缀归类 ，2：包含归类
    # prefixlist = ['ssj','gqf','in'] #文件名中前缀为数组中的内容，将被归为一类
    # #iscasesensitive = True #默认不区分大小写，如果要区分大小写，需要释放注释
    # main(sourcefolderpath, rule,prefixlist = prefixlist)
    ######包含匹配归类
    rule = 2  # 归类规则 ，1：前缀归类 ，2：包含归类
    containinfolist = ['ssj','gqf','in','上海','out'] #文件名中包含数组中的内容，将被归为一类
    # #iscasesensitive = True #默认不区分大小写，如果要区分大小写，需要释放注释
    main(sourcefolderpath,rule,containinfolist = containinfolist)