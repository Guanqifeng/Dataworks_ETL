#spam = ['apples', 'bananas', 'tofu', 'cats']

def printTable():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print(tableData[0][0].rjust(8, ' ') + " " + tableData[1][0].ljust(5, ' ') + " " + tableData[2][0].ljust(5, ' '))
    print(tableData[0][1].rjust(8, ' ') + " " + tableData[1][1].ljust(5, ' ') + " " + tableData[2][1].ljust(5, ' '))
    print(tableData[0][2].rjust(8, ' ') + " " + tableData[1][2].ljust(5, ' ') + " " + tableData[2][2].ljust(5, ' '))
    print(tableData[0][3].rjust(8, ' ') + " " + tableData[1][3].ljust(5, ' ') + " " + tableData[2][3].ljust(5, ' '))
if __name__ == '__main__':
    printTable()