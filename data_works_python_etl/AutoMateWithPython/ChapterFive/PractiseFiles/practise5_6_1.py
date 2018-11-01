#spam = ['apples', 'bananas', 'tofu', 'cats']

def displayInventory(goodsdict):
    countOfGoods = 0
    if goodsdict and isinstance(goodsdict,dict):
        print("Inventory:")
        for key,val in goodsdict.items():
            countOfGoods += val
            print(str(val)+" "+key)
        print("Total number of items: "+str(countOfGoods))
    else:
        print("Your Dict Is None Or Your Input Is Not Dict!")
if __name__ == '__main__':
    dictOfGoods = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(dictOfGoods)