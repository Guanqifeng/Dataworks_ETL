# 斐波那契序列是数字序列，其中每个连续数字是前两个数字的和。经典的斐波那
# 契序列开始于1，1，2，3，5，8，13，……。编写计算第n 个斐波纳契数的程序，其中n
# 是用户输入的值。例如，如果n = 6，则结果为8。
import math

def main(n):
    print("Your enter the number is :"+str(n))
    a,b = 0,1
    while n>0:
        a,b = b,a+b
        n -= 1
    print(str(n)+" Fibonacci is : "+str(b))
if __name__ == '__main__':
    n = eval(input("Please Enter you want to calculate nums: "))
    main(n)