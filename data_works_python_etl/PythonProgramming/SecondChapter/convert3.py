# convert3.py
# A program to convert KM temps to Mile  （1km = 0.62Mile）
# by: Guan Computewell
def main():
    print("This program is transforming KM to Mile !")
    km = eval(input("What is the KM ? "))
    mile = (0.62/1)*km
    print(str(km)+" Km Trans to Mile is", mile)
    input("Press the <Enter> key to quit.")
if __name__ == '__main__':
    main()