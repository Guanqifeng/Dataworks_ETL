import re


def re_match_practice():
    """
      Match(pattern,string,flags = 0),practice
      Conclusion:
          1.The pattern equal string => match true
          2.The string is begin with  pattern => match true
          3.The string contain pattern,but not begin with pattern => match false
    """
    # m = re.match('foo','this foo is good')
    # if m is not None:
    #     print(m.group())
    # else:
    #     print("This String Is Not Regex The Model!")

    print(re.match('foo','foo is good').group())

def re_search_practice():
    """
       Match(pattern,string,flags = 0),practice
       Conclusion:
          1.The pattern equal string => search true
          2.The string is begin with  pattern => search true
          3.The string contain pattern,but not begin with pattern => search false
    """
    m = re.search('foo','this foo is good')
    if m is not None:
        print(m.group())
    else:
        print("This String Is Not Regex The Model!")

def match_more_pattern():
    bt = 'bit|bat|bft'
    m = re.match(bt,'bat')  #Match One
    if m is not None: print("Match One:"+m.group())
    m = re.match(bt, 'blt')  # No Match
    if m is not None: print("No Match:"+m.group())
    m = re.search(bt, 'The bat is good')  # Search
    if m is not None: print("Search:"+m.group())
    m = re.match(bt, 'the bft')  # Match ,but not begin with
    if m is not None: print("Match ,but not begin with:"+m.group())

def math_any_char():
    anyend  = ".end"
    m = re.match(anyend,'bend')
    if m is not None: print("Match Any Char:" + m.group())

def math_char_set():
    charSet = "[cr][01][ab][x5]"
    m = re.match(charSet,'c0ax')
    if m is not None: print("Match Char Set:" + m.group())
    ##Personal Test
    mTest = re.match("[1l23]|[uate]","1a")
    sTest = re.search("[1l23][uate]", "1a")
    if mTest is not None: print("Match Char Set MTest:" + mTest.group())
    if sTest is not None: print("Match Char Set STest:" + sTest.group())

def special_pattern_regex():
    pat = '\w+@(\w+\.)?\w+\.com'
    patMore = '\w+@(\w+\.)*\w+\.com'
    reMail = re.match(pat,'www@xxx.com')
    print("pat:"+reMail.group())
    reOtherMail = re.match(pat, 'www@mmm.xxx.com')
    print("pat:"+reOtherMail.group())

    reMail = re.match(patMore, 'www@xxx.com')
    print("patMore:"+reMail.group())
    reOtherMail = re.match(patMore, 'www@sss.yyy.mmm.xxx.com')
    print("patMore:"+reOtherMail.group())

    print(re.match('\w\w\w-\d\d\d','abc-123').group())
    print(re.match('\w\w\w-\D\D\D', 'abc-ABC').group())

def more_group_macth():
    moreGroup = re.match("(\w\w\w)-(\d\d\d)",'abc-123')
    print(moreGroup.group())
    print(moreGroup.group(0))
    print(moreGroup.group(1))
    print(moreGroup.group(2))
    print(str(moreGroup.groups()))

def special_group_match():
    sGroup = re.match("(a(b))","ab")
    print("group():"+sGroup.group())
    print("group(0):"+sGroup.group(0))
    print("group(1):"+sGroup.group(1))
    print("group(2):"+sGroup.group(2))
    print("groups():"+str(sGroup.groups()))

    sBegin = re.search("^The","this The")
    if sBegin is not None:print("sBegin:"+sBegin.group())
    sBegin = re.search(r"\bThe", "this The")
    if sBegin is not None: print("bsBegin:" + sBegin.group())
    sBegin = re.search("\BThe", "this aTheb good")
    if sBegin is not None: print("BsBegin:" + sBegin.group())

def findall_and_finditer():
    s = "This and ther"
    rf = re.findall("(th\w+) and (th\w+)",s,re.I)
    rfi = re.finditer("(th\w+) and (th\w+)",s,re.I)
    print(rf)
    print(str(rfi.__next__().groups()))
    print([g.group(1) for g in re.finditer("(th\w+)",s,re.I)])

def sub_and_subn():
    sr = re.sub('x','Mr,G','Hello,x\n!')
    print(sr)
    sr  =re.sub("[ab]","X","abcdase")
    srn = re.subn("[ab]", "X", "abcdase")
    print(sr)
    print(srn)
    sr = re.sub("(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})",r"\2/\1/\3","20/2/1991")
    print(sr)
    sr = re.subn("(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", r"\2/\1/\3", "20/2/91")
    print(sr)

def split_regex():
    spr = re.split(":",'a:b:c')
    print(spr)
    spr = re.split(":", 'a:b:c')
    print(spr)

    DATA = (
        'Mountain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA',
    )
    for dataline in DATA:
        print(re.split(", |(?= (?:\d{5}|[A-Z]{2})) ",dataline))

def spread_punctuation_regex():

    spr = re.findall(r"(?i)yes","Yes,yes,YES")
    print(spr)
    #(800) 555-1212
    spf = re.search(r'\((?P<test1>\d{3})\) (?P<test2>\d{3})-(?:\d{4})',"(800) 555-1212").groupdict()
    print(spf)
    #try to regex the usefullstring from emails ,and connect "@aw.com"#
    sl = ['%s@aw.com' % e.group(1) for e in re.finditer(r"(?m)^\s+(?!noreply|postmaster)(\w+)",
                                                   '''
                                                        sales@phptr.com
                                                        postmaster@phptr.com
                                                        eng@phptr.com
                                                        noreply@phptr.com
                                                     admin@phptr.com
                                                    ''')]
    print(sl)

def bool_regex_practice():

    b = bool(re.search(r"(?:(x)|y)(?(1)y|x)","xy"))
    print(b)
    b = bool(re.search(r"(?:(x)|y)(?(1)y|x)", "xx"))
    print(b)
if __name__ == "__main__":
    bool_regex_practice()
    #spread_punctuation_regex()
    #split_regex()
    #sub_and_subn()
    #findall_and_finditer()
    #special_group_match()
    #more_group_macth()
    #special_pattern_regex()
    #math_char_set()
    #math_any_char()
    #re_match_practice()
    #re_search_practice()
    #match_more_pattern()