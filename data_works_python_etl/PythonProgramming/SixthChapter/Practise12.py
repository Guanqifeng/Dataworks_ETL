# 编写并测试一个函数，满足以下规格说明。
# sumList(nums) nums 是一个数字列表。返回列表中数字的和。
import math

def sumList(nums):
    print("Calculate Sum Of nums ！")
    resultSum = 0
    if nums:
        for i in nums:
            resultSum += i
    print("The Sum Of nums is :"+str(resultSum))

if __name__ == '__main__':
    nums = eval(input("Enter a nums list(split by comma): "))
    sumList(nums)