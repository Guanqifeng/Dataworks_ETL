# Syracuse（也称为“Collatz”或“Hailstone”）序列的生成从一个自然数开始，重复
# 应用以下函数，直到达到1
def Syracuse(num):
    if num:
        while num != 1:
            print(num)
            if num % 2 == 0:
                num = num // 2
            elif num % 2 == 1:
                num = 3 * num + 1


if __name__ == '__main__':
    num = eval(input("Please input n that you want to Calculate!(bum):"))
    Syracuse(num)