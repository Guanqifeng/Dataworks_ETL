#  Game OF #
import sys

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def  printBoard(board):
     print(board['top-L']+"|"+board['top-M']+"|"+board['top-R'])
     print('-+-+-')
     print(board['mid-L'] + "|" + board['mid-M'] + "|" + board['mid-R'])
     print('-+-+-')
     print(board['low-L'] + "|" + board['low-M'] + "|" + board['low-R'])
def getPieceCoordinate():
    player = 'X'
    for i in range(9):
        print("Coordinate Of Piece Is :{0}".format(str(theBoard.keys())))
        coordinate = input("Please Input Your Coordinate:")
        while True:
            if coordinate in theBoard and theBoard[coordinate] == ' ':
                theBoard[coordinate] = player
                break
            elif coordinate in theBoard and theBoard[coordinate] != ' ':
                coordinate = input("The Coordinate Is Used By Other Player,Please Input again!(Input Exit If You Want to End of Game)")
            else:
                coordinate = input("The Coordinate Is Not In Piece,Please Input again!(Input Exit If You Want to End of Game)")
            if coordinate == 'Exit':
                sys.exit()
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        printBoard(theBoard)
if __name__ == '__main__':
    getPieceCoordinate()