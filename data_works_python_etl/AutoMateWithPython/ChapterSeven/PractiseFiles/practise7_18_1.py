#匹配每 3 位就有一个逗号的数字？
import re
import pprint
def verificationUsername():
    getUsername = input("Please input Your UserName:")
    username_of_re = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
    if username_of_re.search(getUsername):
        print("Your UserName is Compliance!")
    else:
        print("Your UserName is Not Compliance!")

if __name__ == '__main__':
    verificationUsername()