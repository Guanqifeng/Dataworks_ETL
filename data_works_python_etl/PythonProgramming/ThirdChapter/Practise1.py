#编写一个程序，利用球体的半径作为输入，计算体积和表面积。以下是一些可能有
#用的公式：
#V = 4/3πr3
#A = 4πr2
import math

def main(r):
    print("Calculate volume and surface area from r !")

    V = (4/3)*round(math.pi,2)*r*r*r
    A = 4*round(math.pi,2)*r**2
    print("Volume is :"+str(V)+" Area is :"+str(A)+" of Radius : "+str(r))
if __name__ == '__main__':
    r = eval(input("Please enter your R: "))
    main(r);