import random

def getRandomInt():
    return random.randint(1,20)
def getGuessNumber():
    getRandomNum = getRandomInt()
    Times = 0
    print("I Will Give You 5 Times To Guess The Number!")
    for i in range(5):
        num = eval(input("Please input your guess:"))
        Times += 1
        if getRandomNum > num :
           print("Your Guess is too Low!")
        elif getRandomNum < num :
           print("Your Guess is too High!")
        else:
           print("Good Job,You Guess It By {0} Times!".format(Times))
           break
    if Times == 5:
        print("You have used 5 times to guess the number,you could try again!")
if __name__ == '__main__':
    getGuessNumber()