# Konditorei 咖啡店售卖咖啡，每磅10.50 美元加上运费。每份订单的运费为每磅0.86
# 美元 +固定成本1.50 美元。编写计算订单费用的程序。

def main(n=0,f=0):
    print("Calculate Business income !")
    nic = (10.50 + f - (1.50 + 0.86) )*n
    ic = (10.50 + f)*n
    print("Business income is :"+str(ic)+" and Business Net income is "+str(nic)+" of "+str(n)+" cups of Coffee!")
if __name__ == '__main__':
    t = eval(input("Please enter Cups of coffees that you need: "))
    main(t)