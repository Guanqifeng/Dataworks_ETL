def addInterest(balance,rate):
    newBalance = balance*(1+rate)
    balance = newBalance
    return balance

if __name__=='__main__':
    amount = 10000
    rite = 0.05
    addInterest(amount,rite)
    print(amount)