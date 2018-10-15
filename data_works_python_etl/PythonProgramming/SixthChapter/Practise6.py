# 使用两个函数：一个计算比萨饼的面积，一个计算每平
# 方英寸的成本。
import math
def sumAreaOfTriangle(a,b,c):
    if a and b and c:
        s = (a+b+c)/2
        areaOfTriangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
    else:
        areaOfTriangle = 0
    return areaOfTriangle
if __name__ == '__main__':
    a,b,c = eval(input("Please input Trilateral Of Triangle:"))
    print(sumAreaOfTriangle(a,b,c))