# 用while 循环编程，来确定投资在特定利率下翻倍需要多长时间。输入是年利率，
# 输出是投资增加一倍的年数。注：初始投资金额无关紧要，你可以用1 元。
def getYearsToDouble(principal,rate):
    years = 0
    income = principal
    if principal and rate:
       while income < principal*2:
           income = income+principal*rate
           years += 1
    return years

if __name__ == '__main__':
    principal, rate = eval(input("Please input n that you want to Calculate!(principal,rate):"))
    print(getYearsToDouble(principal, rate))