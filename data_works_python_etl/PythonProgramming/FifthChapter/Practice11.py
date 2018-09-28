# 编写第1 章中的chaos.py 程序的改进版本，允许用户输入两个初始值和迭代次数，
# 然后打印一个格式很好的表格，显示这些值随时间的变化情况。例如，如果初始值为0.25
# 和0.26（10 次迭代），表格可能如下所示：

def main(a,b,n):
    print("This program illustrates a chaotic function")
    #x = eval(input("Enter a number between 0 and 1:"))
    #n = eval(input("How many numbers should I print? "))
    xa = a
    xb = b
    num = 0
    print("{0:10}{1:10}{2:10}".format("index",str(a),str(b)))
    print("--------------------------------")
    for i in range(n):
        #x = 3.9 * x * (1 - x)
        #x = 3.9 * (x - x * x)

        xa = 3.9 * xa - 3.9 * xa * xa
        xb = 3.9 * xb - 3.9 * xb * xb
        #x = 2.0 * x * (1 - x)
        num += 1
        print("{0:10.8}{1:10.8}{2:10.8}".format(str(num),str(xa),str(xb)))

if __name__ == '__main__':
    a = eval(input("Enter a number between 0 and 1:"))
    b = eval(input("Enter a number between 0 and 1:"))
    n = eval(input("How many numbers should I print? "))
    main(a,b,n);