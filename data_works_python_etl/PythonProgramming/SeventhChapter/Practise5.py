# 身体质量指数（BMI）的计算公式是人的体重（以磅计）乘以720，再除以人的身
# 高（以英寸计）的平方。BMI 在19～25 范围内（包括边界值）被认为是健康的。编写一个
# 程序，计算人的BMI，并打印一条消息，告诉他们是在健康范围之上、之中还是之下。
import math

def isHealthyOrNot(Height,Weight):
    #一英尺 = 30.48 厘米
    #一磅 =0.45359237 kg
    if Height and Weight:
        indexOfHealthy =  (Weight/0.45359237) * 720/math.pow(Height/30.48,2)
        if indexOfHealthy and 19 <= indexOfHealthy <= 25:
            return "In the healthy range"
        elif indexOfHealthy and indexOfHealthy > 25:
            return "Above the healthy range"
        elif indexOfHealthy:
            return "Below the healthy range"
        else:
            return None
    else:
        return None
if __name__ == '__main__':
    Height,Weight = eval(input("Please Input The Parameter (Height(cm),Weight(kg)):"))
    print("The Index Of Your Body Is :"+str(isHealthyOrNot(Height,Weight)))