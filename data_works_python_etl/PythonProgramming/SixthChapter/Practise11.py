# 编写并测试一个函数，满足以下规格说明。
# squareEach(nums) nums 是一个数字列表。修改列表，对每一项平方。
import math

def squareEach(nums):
    print("Calculate Square Of nums ！")
    resultList = []
    if nums:
        for i in nums:
            resultList.append(math.sqrt(i))
    print("The Square Of nums is :"+str(resultList))

if __name__ == '__main__':
    nums = eval(input("Enter a nums list(split by comma): "))
    print(nums)
    squareEach(nums)