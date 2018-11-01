#spam = ['apples', 'bananas', 'tofu', 'cats']

def transListToString(lista):
    getResultString = ''
    if isinstance(lista,list) and lista:
        for i in range(len(lista)):
            if i == len(lista) - 1:
                getResultString += " and "+str(lista[i])
            else:
                getResultString += ", "+str(lista[i])
        return  getResultString[1:]
    else:
        print("Your Input Is Not A List")
        pass
if __name__ == '__main__':
    lista = ['this','is','a','test','99',10]
    print(transListToString(lista))