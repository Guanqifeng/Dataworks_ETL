# 使用两个函数：一个计算比萨饼的面积，一个计算每平
# 方英寸的成本。
import math
def sumArea(d):
    print("Calculate Round Area from diameter !")
    r = d/2
    A = round(math.pi,2)*r**2
    print("A diameter Of Pizza is :{0} And Area is :{1}".format(d,A))
    return A
def avgPrice(area,price):
    avg_rice = price/area
    print("Avg Price is :"+str(avg_rice))
if __name__ == '__main__':
    d = eval(input("Please input a diameter Of Pizza:"))
    price = eval(input("Please input Price Of Pizza:"))
    getArea = sumArea(d)
    avgPrice(getArea,price)