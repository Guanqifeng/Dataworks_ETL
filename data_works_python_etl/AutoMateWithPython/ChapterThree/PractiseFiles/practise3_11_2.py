def intTest(number):
    try:
        return int(number)
    except ValueError as e:
        print("Unavailable Parameter,You Should Input A Number Of Int! Error:"+str(e))
if __name__ == '__main__':
    number = input("Please enter a number:")
    print(intTest(number))