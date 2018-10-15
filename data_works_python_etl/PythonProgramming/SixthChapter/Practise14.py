# 使用前面三个问题中的函数来实现计算从文件读取的数字的平方和的程序。你的
# 程序应提示输入文件名，并打印出文件中值的平方和。（提示：使用readlines()。）
import math

def toNumbers(filePath):
    try:
        sumSquareNumList = 0
        with open(filePath,encoding='utf-8') as fileInfo:
            if fileInfo:
                for line in fileInfo.readlines():
                    for i in line.split(','):
                        sumSquareNumList += math.pow(eval(i),2)
            return sumSquareNumList
    except IOError as er:
        print("Error Of Open File!\n"+str(er))
    except Exception as ex:
        print("Exception Of Open File!\n"+str(ex))


if __name__ == '__main__':
    filePath = './SourceFileResource/NumFile1'
    print(toNumbers(filePath))