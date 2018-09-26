# 编程对用户输入的一系列数字求和。 程序应该首先提示用户有多少数字要求和，
# 然后依次提示用户输入每个数字，并在输入所有数字后打印出总和。（提示：在循环体中使
# 用输入语句。）
import random

def main(n):
    print("Your enter the number is :"+str(n))
    global  sum
    sum = sum + n
if __name__ == '__main__':
    sum = 0
    get_r = round(random.random()*10)
    print("you should input "+str(get_r)+" numbers to sum them!")
    for i in range(get_r):
        get_num = eval(input("Please Enter a number now:"))
        main(get_num)
    print("Sum of all number is :"+str(sum))