#创建一个疯狂填词（Mad Libs）程序
import shelve,re
def update_file(inputpath):
    try:
        updateDict = {}
        outputpath = inputpath[:-5] + "_output"
        getRe = re.compile('(ADJECTIVE|NOUN|ADVERB|VERB)')
        with open(inputpath) as getFile:
            getFileInfo = getFile.read()
            getUpdateInfoList = getRe.findall(getFileInfo)
            for word in getUpdateInfoList:
                if word.startswith(('a','e','i','o','u')):
                    print("Enter An {0}".format(word))
                else:
                    print("Enter A {0}".format(word))
                getWillUpdate = input(":")
                updateDict[word] = getWillUpdate
            for i in updateDict:
                getFileInfo = getFileInfo.replace(i,updateDict[i])
            with open(outputpath,'w',encoding='utf-8') as outputFile:
                outputFile.write(getFileInfo)
    except Exception as e:
        print("Get File From Path Error Is:"+e)
if __name__ == '__main__':
    inputpath = '..\\resource\\8_9_2_input'
    #inputpath = 'C:\\Users\\Administrator\\GuanTest\\Dataworks_ETL\\data_works_python_etl\\AutoMateWithPython\\ChapterEight\\resource\\8_9_2_input'
    update_file(inputpath)