# 某个CS 教授给出了5 分测验，等级为5-A、4-B、3-C、2-D、1-F、0-F。编写一个
# 程序，接受测验分数作为输入，并打印出相应的等级。
def main():
    # months is a list used as a lookup table
    grade = ['A','B','C','D','E','F']
    n = int(input("Enter a score number (1-5): "))
    print("The month abbreviation is", grade[n-1] + ".")
if __name__ == '__main__':
    main()