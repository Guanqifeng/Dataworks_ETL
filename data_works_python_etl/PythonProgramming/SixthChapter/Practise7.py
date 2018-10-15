#编写一个函数来计算第n 个斐波纳契数。
import math
def sumFBNQ(n):
    a,b = 0,1
    while n > 0:
        a,b = b,a+b
        n -= 1
    return b
if __name__ == '__main__':
    n = eval(input("Please input Num Of FBNQ:"))
    print(sumFBNQ(n))