# 某位CS 教授给出了100 分的考试，分级为90～100：A，80～89：B，70～79：C，
# 60～69：D，<60：F。编写一个程序，将考试分数作为输入，并使用判断结构来计算相应的
# 等级。

def calculateGrade(score):

    if score and 90 <= score <= 100:
        return "A"
    elif score and 80 <= score <= 89:
        return "B"
    elif score and 70 <= score <= 79:
        return "C"
    elif score and 60 <= score <= 69:
        return "D"
    elif score:
        return "F"
    else:
        return None
if __name__ == '__main__':
    score = eval(input("Please Input The Parameter (score:0~100):"))
    print("You should Get The Grade Is :"+str(calculateGrade(score)))