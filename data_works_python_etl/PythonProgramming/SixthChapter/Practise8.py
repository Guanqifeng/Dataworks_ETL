# 用返回下一个猜测的函数nextGuess(guess,x)解决第3 章中的编程练习17。
import math

def calculateApproximation(guess,x):
    print("Your enter the number is :" + str(x) + "And The Sqrt Of Number is :" + str(math.sqrt(x)))
    print("Your guess number is :" + str(guess))
    approximation = (guess + x / guess) / 2
    print("The approximation is : " + str(approximation))
if __name__ == '__main__':
    guess, x = eval(input("Please Enter you want to calculate nums(guess,x): "))
    calculateApproximation(guess, x)