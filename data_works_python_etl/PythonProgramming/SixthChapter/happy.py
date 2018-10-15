def happy():
    print("Happy Birthday to you!")
def sing(person):
    happy()
    happy()
    print("Happy Birthday,dear %s"%(person)+".")
    happy()
def main():
    sing("Fred")
    print()
    sing("Lucy")
if __name__ == '__main__':
    main()