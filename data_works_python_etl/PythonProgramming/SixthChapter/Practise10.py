# 用函数acronym(phrase)完成第5 章的编程练习4，该函数返回字符串短语的
# 首字母缩略词。
import re

def getAbbreviation(phrase):
    print("Convert phrase to abbreviation ！")
    abbreviation_list = []
    get_list = re.split('\s+', phrase)
    print(str(get_list))
    for i in get_list:
        abbreviation_list.append(i[0].upper())
    print("The phrase " + phrase + " is transformed to " + ''.join(abbreviation_list))
if __name__ == '__main__':
    phrase = input("Enter a phrase: ")
    getAbbreviation(phrase)