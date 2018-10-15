# sumN(n)返回前n 个自然数的和。
# sumNCubes(n)返回前n 个自然数的立方的总和。
# 然后在提示用户输入n 的程序中使用这些函数，并打印出前n 个自然数的和与前n 个
# 自然数的立方之和。
import math

# def sumN(n):
#     sum = 0
#     if n and n >0:
#         for i in range(n):
#             sum = sum + i + 1
#     return sum
# def sumNCubes(n):
#     sumN = 0
#     if n and n > 0:
#         for i in range(n):
#             sumN = sumN +pow((i + 1),3)
#     return sumN
##########递归思路
def sumN(n):
    if n == 1:
        return 1
    else:
        sum = n + sumN(n - 1)
    return sum
def sumNCubes(n):
    if n == 1:
        return 1
    else:
        sumN = math.pow(n,3)+sumNCubes(n-1)
    return sumN
if __name__ == '__main__':
    radius = eval(input("Please input a Number To Calculate:"))
    print("Radius is :{0} And sumNCubes is :{1}".format(radius,sumNCubes(radius)))
    print("Radius is :{0} And sumN is :{1}".format(radius,sumN(radius)))