#spam = ['apples', 'bananas', 'tofu', 'cats']
from data_works_python_etl.AutoMateWithPython.ChapterFive.PractiseFiles.practise5_6_1 import displayInventory

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i,1)
    return  inventory
if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = addToInventory(inv, dragonLoot)
    displayInventory(inv)