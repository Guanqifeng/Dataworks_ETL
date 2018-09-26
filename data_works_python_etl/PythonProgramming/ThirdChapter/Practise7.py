# 编写一个程序，接受两点（见上一个问题），并确定它们之间的距离。
import math

def main(x1=0,y1=0,x2=0,y2=0):
    print("Calculate Two Points's  distance !")
    if y2 != y1 and x2 != x1:
        distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    elif y2 != y1 and x2 == x1:
        distance = abs(y2 - y1)
    else:
        distance = abs(x2 - x1)
    print("Two Points's  distance is :"+str(distance))
if __name__ == '__main__':
    x1,y1,x2,y2 = eval(input("Please enter Coordinate of two points (x1,y1,x2,y2): "))
    main(x1,y1,x2,y2)