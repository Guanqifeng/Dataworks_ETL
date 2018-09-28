# 某个CS 教授给出100 分的考试，分数等级为90～100：A、80～89：B、70～79：
# C、60～69：D、<60：F。编写一个程序，接受考试成绩作为输入，并打印出相应的等级。
def main():
    # months is a list used as a lookup table
    grade = ['A','B','C','D','F']
    n = int(input("Enter a score number (0-100): "))
    if n>=90 and n <= 100:
        i = 0
    elif n>=80 and n <= 89:
        i = 1
    elif n>=70 and n <= 79:
        i = 2
    elif n>=60 and n <= 69:
        i = 3
    else:
        i = 4
    print("The month abbreviation is", grade[i] + ".")
if __name__ == '__main__':
    main()