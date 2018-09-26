# 编程计算用户输入的一系列数字的平均值。与前面的问题一样，程序会首先询问
# 用户有多少个数字。注意：平均值应该始终为float，即使用户输入都是int。
import math
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
    print("AVG of all number is :"+str(sum/get_r))