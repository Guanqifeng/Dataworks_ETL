#匹配每 3 位就有一个逗号的数字？
import re
import pprint
def regex_name():
    getAvaliblename = []
    name_list = ['Satoshi Nakamoto','Alice Nakamoto','RoboCop Nakamoto','satoshi Nakamoto','Mr.Nakamoto','Nakamoto','Satoshi nakamoto']
    re_of_name = re.compile(r'^[A-Z][a-zA-Z]+ [A-Z][a-z]+')
    for i in name_list:
        getAvaliblename.append(re_of_name.search(i))
    pprint.pprint(getAvaliblename)
if __name__ == '__main__':
    regex_name()