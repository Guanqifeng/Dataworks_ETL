def collatz(number):
    if number and number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
if __name__ == '__main__':
    number = eval(input("Please enter a number:"))
    getNumber = collatz(number)
    while getNumber != 1:
        print("The result of function is :" + str(getNumber))
        number = eval(input("Please enter a number:"))
        getNumber = collatz(number)