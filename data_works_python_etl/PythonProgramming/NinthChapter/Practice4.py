# 大多数排球分站赛现在采用回合计分制。在这个系统中，赢得一个回合的球队得1
# 分，即使不是发球的球队。一方得25 分时比赛结束。设计并实现使用回合计分制的排球
# 模拟。

import random

def printInfo():
    print("This is a RBall Game!")
def getInputInfo():
    a = eval(input("Please Enter The Wins Of A:"))
    b = eval(input("Please Enter The Wins Of B:"))
    n = eval(input("Please Enter You Want To Try Number Of Games:"))
    return a,b,n
def resultOfNGame(winsA,winsB,GameN):
    winOfA = 0
    winOfB = 0
    for i in range(GameN):
        getscoreA,getscoreB = resultOfOneGame(winsA,winsB)
        print("The PlayerA And PlayerB's Score of Game is (scoreA,scoreB):{0},{1}".format(getscoreA,getscoreB))
        if getscoreA > getscoreB:
            winOfA += 1
        else:
            winOfB += 1
    return winOfA,winOfB
def resultOfOneGame(winsA,winsB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA,scoreB):
      if  serving == 'A':
          if random.random() < winsA:
              scoreA += 1
          else:
              serving = 'B'
      else:
          if random.random() < winsB:
              scoreB += 1
          else:
              serving = 'A'
    return  scoreA,scoreB
def gameOver(a,b):
    return (a >= 15 and a - b >= 2) or (b >= 15 and b - a >= 2) or a == 25 or b ==25


def main():
    #明确比赛内容
    printInfo()
    winsA,winsB,GameN = getInputInfo()
    getWinOfA,getWinOfB = resultOfNGame(winsA,winsB,GameN)
    print("Player A Win {0} Games That Accounting Of Game is {1:0.1%}:".format(getWinOfA,getWinOfA/GameN))
    print("Player B Win {0} Games That Accounting Of Game is {1:0.1%}:".format(getWinOfB, getWinOfB/GameN))
if __name__ == '__main__':
    main()