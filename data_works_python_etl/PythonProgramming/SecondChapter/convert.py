# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
def main():
    #for i in range(5):
    print("This program is transforming Celsius to Fahrenheit !")
    print("------------output-------------")
    print("Celsius---------transto----------Fahrenheit")
    for celsius in [a for a in range(0,101,10)]:
        #print("This program is transforming Celsius to Fahrenheit !")
        #celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        #print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        print(str(celsius)+"                              "+str(fahrenheit))
    input("Press the <Enter> key to quit.")

if __name__ == '__main__':
    main()