# 修改短柄壁球模拟，以便计算最佳n 场比赛结果。先发球是交替的，所以选手A 在
# 奇数局比赛中是先发球，选手B 在偶数局比赛中是先发球。


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
        getscoreA,getscoreB = resultOfOneGame(winsA,winsB,i+1)
        if getscoreA > getscoreB:
            winOfA += 1
        else:
            winOfB += 1
    return winOfA,winOfB
def resultOfOneGame(winsA,winsB,n):
    if n%2 ==0 :
        serving = "B"
    else:
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
    return a ==15 or b == 15


def main():
    #明确比赛内容
    printInfo()
    winsA,winsB,GameN = getInputInfo()
    getWinOfA,getWinOfB = resultOfNGame(winsA,winsB,GameN)
    print("Player A Win {0} Games That Accounting Of Game is {1:0.1%}:".format(getWinOfA,getWinOfA/GameN))
    print("Player B Win {0} Games That Accounting Of Game is {1:0.1%}:".format(getWinOfB, getWinOfB/GameN))
if __name__ == '__main__':
    main()