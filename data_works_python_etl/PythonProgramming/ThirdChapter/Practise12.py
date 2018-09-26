# 编程计算前n 个自然数的立方和，其中n 的值由用户提供。
import math

def main(n):
    print("Sum of N!")
    sum = 0
    for i in range(n):
        sum = sum + math.pow(i+1,3)
    print("Sum of N is :"+str(sum))
if __name__ == '__main__':
    n = eval(input("Please enter n: "))
    main(n)