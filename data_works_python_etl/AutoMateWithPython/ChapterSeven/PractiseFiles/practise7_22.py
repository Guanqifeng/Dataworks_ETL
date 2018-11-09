#匹配每 3 位就有一个逗号的数字？
import re
import pprint
def regex_special_sentence():
    get_re_special_sentence_list = []
    special_sentence_list = ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.'
                            ,'RoboCop eats apples.','ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']
    getRe = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$',re.I)
    for i in special_sentence_list:
        get_re_special_sentence_list.append(getRe.search(i))
    pprint.pprint(get_re_special_sentence_list)
if __name__ == '__main__':
    regex_special_sentence()