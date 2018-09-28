# 扩展前一个问题的解决方案，允许计算完整的名字，如“John Marvin Zelle”或“John
# Jacob Jingleheimer Smith”。总值就是所有名字的数值之和。
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