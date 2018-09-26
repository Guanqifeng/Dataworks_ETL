# 给定圆形比萨饼的直径和价格，编写一个程序，计算每平方英寸的成本。
# 面积公式为 A = πr2。
import math

def main(d,price):
    print("Calculate Round Area from diameter !")
    r = d/2
    A = round(math.pi,2)*r**2
    avg_rice = price/A
    print("Avg Price is :"+str(avg_rice)+" of diameter : "+str(d))
if __name__ == '__main__':
    d = eval(input("Please enter your Diameter: "))
    price = eval(input("Please enter your Price: "))
    main(d,price)