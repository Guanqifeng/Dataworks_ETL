#许多公司对每周超出40 小时以上的工作时间支付150%的工资。编写程序输入工作
#小时数和小时工资，并计算一周的总工资。

def calculateSalary(hours,salaryofhour):
    print("You Input The Parameter is （hours，salaryofhour）：{0}，{1}".format(hours,salaryofhour))
    if hours > 40:
        getSalary = (hours - 40) * salaryofhour * 1.5 + 40 * salaryofhour
    else:
        getSalary = hours * salaryofhour
    return getSalary

if __name__ == '__main__':
    hours,salaryofhour = eval(input("Please Input The Parameter （hours，salaryofhour）:"))
    print("You should Get The Salary Is :"+str(calculateSalary(hours,salaryofhour)))