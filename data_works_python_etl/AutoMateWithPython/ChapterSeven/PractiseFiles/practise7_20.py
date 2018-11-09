#匹配每 3 位就有一个逗号的数字？
import re

def regex_3_num():
    getRe = re.compile(r'^\d{1,3}(,\d{3})+|^\d{1,2}$')
    numList = ['42','1,234','6,368,745','12,34,567','1234']
    result = []
    for i in numList:
        print(getRe.search(i))
        #result.append(getRe.match(i))
if __name__ == '__main__':
    regex_3_num()