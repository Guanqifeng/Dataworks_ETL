# 某所大学根据学生拿到的学分对学生分年级。小于7 学分的学生是大一新生。至少
# 有7 个学分才是大二，16 分以上是大三，26 分以上是大四。编写一个程序，根据获得的学
# 分数计算年级。

def calculateGrade(credit):

    if credit and credit >= 26:
        return "大四"
    elif score and credit >= 16:
        return "大三"
    elif score and credit >= 7:
        return "大二"
    elif score:
        return "大一新生"
    else:
        return None
if __name__ == '__main__':
    score = eval(input("Please Input The Parameter (credit:0~100):"))
    print("You should Get The Grade Is :"+str(calculateGrade(score)))