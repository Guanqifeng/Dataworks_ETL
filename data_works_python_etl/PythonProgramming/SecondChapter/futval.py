# futval.py
# A program to compute the value of an investment
# carried 10 years into the future

def main():
    # print("This program calculates the future value")
    # print("of a 10-year investment.")
    # principal = eval(input("Enter the initial principal: "))
    # apr = eval(input("Enter the annual interest rate: "))
    # years = eval(input("Enter the saving of years: "))
    # for i in range(years):
    #     principal = principal*(1+apr)
    # print("The value in "+str(years)+" years is:", principal)
    ###########固定投入  收益###############
    # principal = eval(input("Enter the initial principal: "))
    # apr = eval(input("Enter the annual interest rate: "))
    # years = eval(input("Enter the saving of years: "))
    # income = 0
    # for i in range(years):
    #     income = (income+principal)*(1+apr)
    # print("Fixed investment is :"+str(principal),end="  ")
    # print("Investment years is :" + str(years), end="  ")
    # print("Income of  :"+str(years)+"Years is :"+str(income))
    ##############复利频度为：季度 计算收益###################
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the saving of years: "))
    for i in range(years*10):
        principal = principal*(apr/10+1)
    print("The value in " + str(years) + " years is:", str(principal))


if __name__ == '__main__':
    main()
