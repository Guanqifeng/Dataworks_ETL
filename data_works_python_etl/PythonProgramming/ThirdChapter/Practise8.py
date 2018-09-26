# 格里高利闰余是从1 月1 日到前一个新月的天数。此值用于确定复活节的日期。它
# 由下列公式计算（使用整型算术）：
# C = year//100
# epact = (8 + (C//4) - C + ((8C + 13)//25) + 11(year%19))%30

def main(year):
    print("Calculate Year is Epact !")
    C = year // 100
    Epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11*(1999%19))%30
    print("Two Points's  Slope is :"+str(Epact))
if __name__ == '__main__':
    year = eval(input("Please enter Four-digit of Year: "))
    main(year)