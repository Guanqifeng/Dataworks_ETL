def addInterest(balance,rate):
    newBalance = balance*(1+rate)
    return newBalance

if __name__=='__main__':
    amount = 10000
    rite = 0.05
    amount = addInterest(amount,rite)
    print(amount)