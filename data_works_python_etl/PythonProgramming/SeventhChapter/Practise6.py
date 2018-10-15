# Podunksville 的超速罚单政策是50 美元加上超速部分每mph（一英里每小时）5 美
# 元，如果超过90mph 再追加罚款200 美元。编写一个程序，接受度速限制和计时速度，并
# 打印一条消息，表明速度合法，或者在速度非法时，打印罚款。
import math

def isIllegalOrNot(speedlimit,timingspeed):
    print("Legitimate Speed Is :{0}".format(speedlimit))
    overSpeed = timingspeed - speedlimit
    if overSpeed and overSpeed < 90:
       return overSpeed * 5
    elif overSpeed and overSpeed >= 90:
       return 90 * 5+200
    else:
        return None
if __name__ == '__main__':
    speedlimit,timingspeed = eval(input("Please Input The Parameter (speedlimit(mph),timingspeed(mph)):"))
    print("The Fine Is :"+str(isIllegalOrNot(speedlimit,timingspeed)))