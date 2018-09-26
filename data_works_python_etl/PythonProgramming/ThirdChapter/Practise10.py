# 编写程序，确定梯子斜靠在房子上时，达到给定高度所需的长度。梯子的高度和
# 角度作为输入。计算长度使用公式为：
import math

def main(height,angle):
    print("Calculate Length of Ladder !")
    #角度必须以弧度表示
    radians = (math.pi/180)*angle
    length = height/math.sin(radians)
    print("Ladder's Length is :"+str(length))
if __name__ == '__main__':
    height,angle = eval(input("Please enter Height and Angle of Ladder(height,angle): "))
    main(height,angle)