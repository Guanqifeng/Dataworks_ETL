def addInterest(balance,rate):
    for i in range(len(balance)):
        balance[i] = balance[i]*(1+rate)
    return balance

if __name__=='__main__':
    amounts = [10000,20000,30000]
    rite = 0.05
    addInterest(amounts,rite)
    print(amounts)