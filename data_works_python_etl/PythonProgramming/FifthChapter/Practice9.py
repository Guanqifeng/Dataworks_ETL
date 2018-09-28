# 编写一个程序，计算用户输入的句子中的单词数。
import re
def main():
    print("Count Words from Phrase！")
    Phrase = input("Please Enter the Phrase: ")
    Phrase_words = re.split('\s+',Phrase.strip())
    print(str(Phrase_words))
    for word in set(Phrase_words):
        print("The Word :"+str(word)+" of the Phrase that count is:"+str(Phrase_words.count(word)))
if __name__ == '__main__':
    main()