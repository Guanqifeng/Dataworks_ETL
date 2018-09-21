def main():
    print("This is a Calculator!")
    exp = input("Please Enter Your Expression:")
    result = eval(exp)
    print("The Expression '",exp,"' result is :",result)

if __name__ == '__main__':
    main()