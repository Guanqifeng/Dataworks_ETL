# 数字命理学家声称能够基于名字的“数值”来确定一个人的性格特征。名字的值的
# 确定方法是名字中字母的值之和，其中“a”为1、“b”为2、“c”为3，直到“z”为26。
# 例如，名字“Zelle”具有的值为26 + 5 + 12 + 12 + 5 = 60（顺便说一下，这恰好是一个非常
# 吉利的数字）。编写一个程序，计算输入的单个名字的数值。
import re
def main():
    print("Calculate name_value of name!")
    sum = 0
    base_name = input("Please enter your name:")
    name = ''.join(re.findall('[a-zA-Z]+',base_name))
    for i in name:
        sum = sum + (ord(i.lower())-96)
    print("Your name :"+str(base_name)+" taht name_value is "+str(sum))
if __name__ == '__main__':
    main()