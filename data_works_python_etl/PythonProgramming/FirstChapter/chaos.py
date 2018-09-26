# File: chaos.py
# A simple program illustrating chaotic behavior.
def main(a,b,n):
    print("This program illustrates a chaotic function")
    #x = eval(input("Enter a number between 0 and 1:"))
    #n = eval(input("How many numbers should I print? "))
    xa = a
    xb = b
    print("          input    " + str(a) + "     " + str(b))
    print("--------------------------------")
    for i in range(n):
        #x = 3.9 * x * (1 - x)
        #x = 3.9 * (x - x * x)

        xa = 3.9 * xa - 3.9 * xa * xa
        xb = 3.9 * xb - 3.9 * xb * xb
        #x = 2.0 * x * (1 - x)
        print("                   "+str(xa)+"     "+str(xb))

if __name__ == '__main__':
    a = eval(input("Enter a number between 0 and 1:"))
    b = eval(input("Enter a number between 0 and 1:"))
    n = eval(input("How many numbers should I print? "))
    main(a,b,n);

