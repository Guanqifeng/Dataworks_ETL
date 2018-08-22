import shelve

def storePerson(db):
    pid = input("Enter your ID number:")
    person = {}
    person['name'] = input("Enter your name:")
    person['age'] = input("Enter your age:")
    person['phone'] = input("Enter your phone:")
    db[pid] = person

def lookupPerson(db):

    pid = input("Please enter ID number that you want:")

    getinfo = input("What would you want to konw?(name,age,phone):")
    getinfo = getinfo.strip().lower()

    print(str(getinfo.capitalize()) + ":" + str(db[pid][getinfo]))

def printHelp():
    print("The help info:")
    print("Enter store to store person info.")
    print("Enter lookup to select person info.")
    print("Enter ? for help.")
    print("Enter quit to exit database.")

def getInputInfo():
    cmd = input("Enter you (?/help):")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('./database/database.dat')
    try:
        while True:
            cmd = getInputInfo()
            if cmd == '?':
                printHelp()
            elif cmd == 'store':
                storePerson(database)
            elif cmd == 'lookup':
                lookupPerson(database)
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == "__main__":  main()