import string
import random

def getRandomChar():
    '''
       Create Random Char
    :return: string
    '''
    allchar = string.digits + string.ascii_letters
    randomresult = random.sample(allchar,1)
    return ''.join(randomresult)
def concatRandomChar(num):
    '''
        Input a Int Type Parameter To Get A String  of  Concat Random Char
    :parameter:int
    :return: string
    '''
    if isinstance(num,int):
        getRandomList = ''.join([getRandomChar() for i in range(num)])
    else:
        print("Please enter a int type parameters")
    return str(getRandomList)
def getSeriaNumber(num,partnum):
    try:
        getNum = int(num)
        getPartnum = int(partnum)
        getSeriaNum = '-'.join([concatRandomChar(getNum) for i in range(getPartnum)])
        print(getSeriaNum)
        return getSeriaNum
    except TypeError as e:
        print(e)
def getAllSeriaNumber(num,partnum,allnum):
    try:
        getallserianum = [getSeriaNumber(num,partnum) for i in range(allnum)]
        print(getallserianum)
    except:
        print("Paramater's type is not int")

if __name__ == "__main__":
    #getSeriaNumber(4,4)
    getAllSeriaNumber(5,4,10)