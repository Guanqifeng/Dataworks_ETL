#N场壁球比赛需要：
#1.运动员 2.比赛规则 3.一场比赛
import random
class Player():
    def __init__(self,winrate):
        self.winrate = winrate
    def getPlayerWinRate(self):
        return self.winrate
    def setPlayerWinRate(self,winrate):
        self.winrate = winrate
class GameIsOver():
    def __init__(self,playerAScore,playerBScore):
        self.playerAScore = playerAScore
        self.playerBScore = playerBScore
    def IsOverOrNotOfGame(self):#根据两名运动员的比分，利用比赛规则，返回比赛结果
        return self.playerAScore == 15 or self.playerBScore == 15 or\
               (self.playerAScore == 7 and self.playerBScore == 0) or (self.playerAScore == 0 and self.playerBScore == 7)
class MoreOfGame():
    def __init__(self,PlayerA,PlayerB):
        self.PlayerA = PlayerA
        self.PlayerB = PlayerB
    def getResultOfGame(self,numofGames):
        playerAWin = 0
        playerBWin = 0
        playerAWinByZero = 0
        playerBWinByZero = 0
        for i in range(1,numofGames+1):
            if i % 2 == 0:
                serve = "A"
            else:
                serve = "B"
            getPlayerAScore,getPlayerBScore = self.OneOfGame(serve)
            if getPlayerAScore > getPlayerBScore:
                if getPlayerBScore == 0:
                    playerAWinByZero += 1
                    playerAWin += 1
                else:
                    playerAWin += 1
            else:
                if getPlayerAScore == 0:
                    playerBWinByZero += 1
                    playerBWin += 1
                else:
                    playerBWin += 1
        return playerAWin , playerBWin , playerAWinByZero , playerBWinByZero
    def OneOfGame(self,serve):
        PlayerAScore = 0
        PlayerBScore = 0
        while not GameIsOver(PlayerAScore, PlayerBScore).IsOverOrNotOfGame():
            if serve == "A":
                if random.random() < self.PlayerA.getPlayerWinRate():
                    PlayerAScore += 1
                else:
                    serve = "B"
            if serve == "B":
                if random.random() < self.PlayerB.getPlayerWinRate():
                    PlayerBScore += 1
                else:
                    serve = "A"
        return PlayerAScore , PlayerBScore

def main():
    print("We Will Be Playing A Game Of R_Ball!")
    playARate = float(input("Please Input A Game Rate of Player A Is :"))
    playBRate = float(input("Please Input A Game Rate of Player B Is :"))
    numberOfGames = int(input("Please Input Number Of Games That You Want Is :"))
    playA = Player(playARate)
    playB = Player(playBRate)
    getplayerAWin,getplayerBWin,getplayerAWinByZero,getplayerBWinByZero = MoreOfGame(playA,playB).getResultOfGame(numberOfGames)
    print("The Results Of {0} Games is:\n playA's Win is {1}\n playB's Win is {2}\n playA's Zero_Win is {3}\n playB's Zero_Win is {4}\n"
          " The Rate Of Win By PlayA is {5:0.1%}\n The Rate Of Win By PlayB is {6:0.1%}".format(numberOfGames,getplayerAWin,getplayerBWin,getplayerAWinByZero,getplayerBWinByZero,getplayerAWin/numberOfGames,getplayerBWin/numberOfGames))

if __name__ == '__main__':
    main()