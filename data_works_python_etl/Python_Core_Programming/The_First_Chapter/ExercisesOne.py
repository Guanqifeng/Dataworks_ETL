import re

#1.1
def practice_1_1():
 get_result = re.findall('[hb][aui]t','abatbitbuthathithutc32')
 print("1_1:"+str(get_result))
#1.2
def practice_1_2():
 get_result = re.findall('\w+ \w','Guan QF,Sukie S')
 print("1_2:"+str(get_result))
#1.3
def practice_1_3():
 get_result = re.findall('\w+,\s\w+','Guan, QF,Sukie, S, G')
 print("1_3:"+str(get_result))
#1.4
def practice_1_4():
 get_result = re.findall('[A-Za-z_]+[\w_]+','__name__,if,import')
 print("1_4:"+str(get_result))
#1.5
def practice_1_5():
 get_result = re.search('[0-9]+\s([a-zA-z ])+','3120 De la Cruz Boulevard').group(0)
 print("1_5:"+str(get_result))

#1.6
def practice_1_6():
 get_result = re.search('^www\.\w+\.com$','www.ccc2345234.com').group(0)
 print("1_6:"+get_result)
 get_result_S = re.findall('\w+://\w+\.\w+\.\w{3}\s?', 'http://www.foothill.edu http://www.1232.net')
 print("1_6:"+str(get_result))

#1.7
def practice_1_7():
 get_result = re.search('[\+-]?\d+','-123123').group(0)
 print("1_7:"+str(get_result))

#1.8
def practice_1_8():
 get_result = re.search('[\+-]?\d+[lL]$','-123123L').group(0)
 print("1_8:"+str(get_result))

#1.9
def practice_1_9():
 get_result = re.search('[\+-]?\d*\.\d*','23.1212312').group(0)
 print("1_9:"+str(get_result))

#1.10
def practice_1_10():
 get_result = re.search('[\+-]?\d+\.\d+\+\d+\.\d+[j]$','-1.4+1.5j').group(0)
 print("1_10:"+str(get_result))

#1.11
def practice_1_11():
 get_result = re.search('[a-zA-Z0-9_]+@\w+\.\w+','2018_guan@163.com').group(0)
 print("1_11:"+str(get_result))

#1.12
def practice_1_12():
 get_result = re.search('(https|http)?(://)?\w+.+','https://ide-cn-shanghai.data.aliyun.com/').group(0)
 print("1_12:"+str(get_result))

def practice_1_13():
 s = "<type 'int'>,<type 'float'>,<type 'builtin_function_or_method'>"
 get_result = re.sub('<type|>|\'','',s).split(",")
 print("1_13:"+str(get_result))

def practice_1_13():
 s = "2018-9-10"
 get_result = re.sub('-0?([1-9])-',r"0\1",s)
 print("1_13:"+str(get_result))

def practice_1_14():
 s = "282132231233222 1111-222222-3333 1111-2222-3333-4444 "
 get_result = re.findall('(\d{4}-?\d{4,6}-?\d{4,5}-?\d{0,4})',s)
 print("1_14:"+str(get_result))

if __name__ == '__main__':
    practice_1_1();
    practice_1_2();
    practice_1_3();
    practice_1_4();
    practice_1_5();
    practice_1_6();
    practice_1_7();
    practice_1_8();
    practice_1_9();
    practice_1_10();
    practice_1_11();
    practice_1_12();
    practice_1_13();
    practice_1_14();