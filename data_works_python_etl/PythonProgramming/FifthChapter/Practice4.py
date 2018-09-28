# 首字母缩略词是一个单词，是从短语中的单词取第一个字母形成的。例如，RAM
# 是“random access memory”的缩写。编写一个程序，允许用户键入一个短语，然后输出
# 该短语的首字母缩略词。注意：首字母缩略词应该全部为大写，即使短语中的单词没有
# 大写
import re
def main():
    # months is a list used as a lookup table
    print("Convert phrase to abbreviation ！")
    abbreviation_list = []
    phrase = input("Enter a phrase: ")
    get_list = re.split('\s+',phrase)
    print(str(get_list))
    for i in get_list:
        abbreviation_list.append(i[0].upper())
    print("The phrase "+phrase+" is transformed to "+''.join(abbreviation_list))
if __name__ == '__main__':
    main()