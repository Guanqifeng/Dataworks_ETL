#匹配每 3 位就有一个逗号的数字？
import re
import pprint
def strip_of_person(getstring ,special = ' '):
    strip_re = re.compile(r'^([' + str(special) + r']*)(.*?)([' + str(special) + ']*)$')
    if getstring:
        get_result = strip_re.search(getstring).group(2)
        return get_result
    else:
        print("Your Input Is None!")
if __name__ == '__main__':
    getstring = str(input("Please Input Your Input That You Want To Strip:"))
    special = str(input("Please Input Your Input Special Strip(Default Blank):"))
    if special :
         print(strip_of_person(getstring,special))
    else:
         print(strip_of_person(getstring))
