# 使用坐标（x1，y1）和（x2，y2）指定平面中的两个点。编写一个程序，计算通过
# 用户输入的两个（非垂直）点的直线的斜率。


def main(x1=0,y1=0,x2=0,y2=0):
    print("Calculate Two Points's  Slope !")
    if y2 != y1 and x2 != x1:
        Slope = (y2-y1)/(x2-x1)
    else:
        Slope = 0
    print("Two Points's  Slope is :"+str(Slope))
if __name__ == '__main__':
    x1,y1,x2,y2 = eval(input("Please enter Coordinate of two points (x1,y1,x2,y2): "))
    main(x1,y1,x2,y2)