def happy():
    return "Happy Birthday to you! \n"
def sing(person):
    lyrics = happy()*2 + "Happy Birthday , dear {0}".format(person) + ". \n" +happy()
    return lyrics
def main():
    for i in ['Susan','Lucy','Fred']:
        print(sing(i))
if __name__ == '__main__':
    main()