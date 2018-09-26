# 使用以下公式编写程序以计算三角形的面积，其三边的长度为a、b 和c：
import math

def main(a,b,c):
    print("Calculate Area of Triangle !")
    S = (a + b + c)/2
    A = math.sqrt(S*(S-a)*(S-b)*(S-c))
    print("Triangle's Area is :"+str(A))
if __name__ == '__main__':
    a,b,c = eval(input("Please enter Trilateral of Triangle(a,b,c): "))
    main(a,b,c)