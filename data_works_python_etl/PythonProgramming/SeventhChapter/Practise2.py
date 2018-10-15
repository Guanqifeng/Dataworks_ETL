#某位CS 教授给出了5 分的小测验，评分等级为5-A，4-B，3-C，2-D，1-E，0-F。
# 编写一个程序，接受测验得分作为输入，并使用判断结构来计算相应的等级。

def calculateGrade(score):
    dictGrade = {5:'A',4:'B',3:'C',2:'D',1:'E',0:'F'}
    if score in dictGrade:
        print("You Input The Parameter is :{0} In The Statistics Range!".format(score))
        return dictGrade.get(score)
    else:
        print("You Input The Parameter is :%s Not In The Statistics Range!"%score)
        return None
if __name__ == '__main__':
    score = eval(input("Please Input The Parameter (score):"))
    print("You should Get The Grade Is :"+str(calculateGrade(score)))