# 斐波那契序列开始是1,1,2,3,5,8，……前两个数字之后，序列中的每个数字都是前
# 两个数之和。编写一个程序，计算并输出第n 个斐波纳契数，其中n 是用户输入的值
def getFBNQ(n):
    a,b = 0,1
    while n > 0:
        a,b = b,a+b
        n -=1
    return b

if __name__ == '__main__':
    n = eval(input("Please input n that you want to Calculate!:"))
    print(getFBNQ(n))