# convert2.py
# A program to convert Fahrenheit temps to Celsius
# by: Guan Computewell
def main():
    print("This program is transforming Celsius to Fahrenheit !")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("The temperature is", celsius, "degrees Celsius.")
    input("Press the <Enter> key to quit.")
if __name__ == '__main__':
    main()