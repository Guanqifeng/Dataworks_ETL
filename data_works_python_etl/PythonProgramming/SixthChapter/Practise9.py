# 用返回分数的字母等级的函数grade(score)完成第5 章的编程练习3。
def calculateGrade(n):
    grade = ['A', 'B', 'C', 'D', 'F']
    if n >= 90 and n <= 100:
        i = 0
    elif n >= 80 and n <= 89:
        i = 1
    elif n >= 70 and n <= 79:
        i = 2
    elif n >= 60 and n <= 69:
        i = 3
    else:
        i = 4
    print("The month abbreviation is", grade[i] + ".")
if __name__ == '__main__':
    n = int(input("Enter a score number (0-100): "))
    calculateGrade(n)