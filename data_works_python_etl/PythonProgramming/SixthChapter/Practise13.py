# 编写并测试一个函数，满足以下规格说明。
# toNumbers(strList) strList 是一个字符串列表，每个字符串表示一个数字。修
# 改列表，将每一项转换为数字。
import math

def toNumbers(nums):
    print("Transformation String To Number！")
    resultTrans = []
    for i in nums:
        resultTrans.append(eval(i.replace('\'','').replace('\"','')))
    print("The Sum Of nums is :"+str(resultTrans))

if __name__ == '__main__':
    nums = input("Enter a nums list(split by comma): ").split(',')
    toNumbers(nums)