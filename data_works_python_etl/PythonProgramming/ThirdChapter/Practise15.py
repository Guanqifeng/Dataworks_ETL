# 编写程序，通过对这个级数的项进行求和来求近似的π 值：4/1 – 4/3 + 4/5 – 4/7 + 4/9
# − 4/11 +……程序应该提示用户输入n，要求和的项数，然后输出该级数的前n 个项的和。
# 让你的程序从math.pi 的值中减去近似值，看看它的准确性。
import math

def main(n):
    print("Your enter the number is :"+str(n))
    print("Constant π is : "+str(math.pi))
    get_sum = 0
    for i in range(0,n,2):
       if ((i+1)//2)%2 == 0:
           get_sum = get_sum+4/(i+1)
       else:
           get_sum = get_sum-4/(i+1)
    print("Get sum value is ："+str(get_sum))
    print("Get Sum value Difference from Pi : "+str(math.pi-get_sum))
if __name__ == '__main__':
    n = eval(input("Please Enter you want to calculate nums: "))
    main(n)