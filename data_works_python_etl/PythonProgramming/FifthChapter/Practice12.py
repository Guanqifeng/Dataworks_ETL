# 编写第2 章中的futval.py 程序的改进版本。程序将提示用户投资金额、年化利率
# 和投资年数。然后程序将输出一个格式正确的表，以年为单位跟踪投资的价值


def main():
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the saving of years: "))
    print("{0:10},{1:10}".format("Year","Value"))
    print("------------------------------------")
    for i in range(years):
        principal = principal*(apr+1)
        print("{0:10}${1:10.8}".format(str(i+1),str(principal)))


if __name__ == '__main__':
    main()