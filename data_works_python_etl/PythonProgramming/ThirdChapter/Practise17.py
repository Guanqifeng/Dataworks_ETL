# 编程实现牛顿方法。程序应提示用户找到值的平方根（x）和改进猜测的次数。从猜测
# 值x / 2 开始，你的程序应该循环指定的次数，应用牛顿的方法，并报告猜测的最终值。你
# 还应该从math.sqrt(x)的值中减去你的估计值，以显示它的接近程度。
import math

def main(guess,x):
    print("Your enter the number is :"+str(x)+"And The Sqrt Of Number is :"+str(math.sqrt(x)))
    print("Your guess number is :" + str(guess))
    approximation  = (guess+x/guess)/2
    print("The approximation is : "+str(approximation))
if __name__ == '__main__':
    guess,x = eval(input("Please Enter you want to calculate nums(guess,x): "))
    main(guess,x)