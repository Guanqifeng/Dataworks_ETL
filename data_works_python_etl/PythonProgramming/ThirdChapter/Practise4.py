# 编写一个程序，根据闪光和雷声之间的时间差来确定雷击的距离。声速约为1100
# 英尺/秒，1 英里为5280 英尺。

def main(t):
    print("Calculate Thunder distance from me !")
    #1 英里为5280 英尺
    #声速约为1100英尺/秒
    # v = t*s
    v = t*1100/5280
    print("Thunder between with me is :"+str(v)+" mile!")
if __name__ == '__main__':
    t = eval(input("Please enter time(unit:s) interval of Lightning and Thunder: "))
    main(t)