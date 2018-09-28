# 编写一个程序，计算用户输入的句子中的平均单词长度。
import re
def main():
    print("Count Words from Phrase！")
    Phrase = input("Please Enter the Phrase: ")
    Phrase_words = re.split('\s+',Phrase.strip())
    sum_len = 0
    num = 0
    for word in Phrase_words:
        sum_len = sum_len + len(word)
        num +=1
    print("Avg length of the word from Phrase is :"+str(round(sum_len/num,4)))
if __name__ == '__main__':
    main()