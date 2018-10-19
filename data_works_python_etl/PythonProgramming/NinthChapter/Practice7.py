# 花旗骰是在许多赌场玩的骰子游戏。一个玩家掷一双普通的六面骰子。如果初始点
# 数是2、3 或12，则玩家失败。如果是7 或11，则玩家获胜。任何其他初始点数将导致玩家
# “再掷点”。也就是说，玩家持续掷骰子直到掷出7 或重新掷出初始点。如果选手在掷出7
# 之前重新掷出初始点，就获胜。先掷出7 则失败。
# 编程模拟多次掷骰子游戏，并估计玩家获胜的可能性。例如，如果玩家在500 场比赛
# 中赢了249 场，那么估计的获胜概率是249/500 = 0.498。

import random
def dice_game(n):
    winGameNum = 0
    for i in range(n):
        if one_dice_game():
            winGameNum += 1
    print("The Number Of Games is :{0},Win Of The Game is :{1},And The Accounting Of The Game is:{2:0.1%}".format(n,winGameNum,winGameNum/n))
def one_dice_game():
    theFirstResultOfGame = dice()
    firstLoseList = [2,3,12]
    firstWinList = [7,11]
    riceNumOfGame = 1
    getResultOfGame = False
    if theFirstResultOfGame in firstLoseList:
        getResultOfGame = False
    elif theFirstResultOfGame in firstWinList:
        getResultOfGame = True
    else:
        while True:
            riceNumOfGame += 1
            if theFirstResultOfGame == dice() and dice() != 7:
                getResultOfGame = True
                break
            elif dice() == 7:
                getResultOfGame = False
                break
    print('The Number Of Rice In Rice Game Is :' + str(riceNumOfGame))
    return getResultOfGame
def dice():
    diceA = random.randrange(6) + 1
    diceB = random.randrange(6) + 1
    return diceA+diceB



if __name__ == '__main__':
    n = eval(input("Please Input Number Of Games:"))
    dice_game(n)