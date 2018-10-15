# 2．写一个程序来打印“The Ants Go Marching.”十段的歌词。下面给出几个例句。你
# 可以为每一节中的“little one”选择你自己的活动，但一定要选择一些押韵（或几乎押韵）
# 的内容。
# The ants go marching one by one, hurrah! hurrah!
# The ants go marching one by one, hurrah! hurrah!
# The ants go marching one by one,
# The little one stops to suck his thumb,
# And they all go marching down...
# In the ground...
# To get out....
# Of the rain.
# Boom! Boom! Boom!
# The ants go marching two by two, hurrah! hurrah!
# The ants go marching two by two, hurrah! hurrah!
# The ants go marching two by two,
# The little one stops to tie his shoe,
# And they all go marching down...
# In the ground...
# To get out...
# Of the rain.
# Boom! Boom! Boom!

def startword(num,end = ''):
    return  'The ants go marching {0} by {1}, {2}\n'.format(num,num,end)
def endword():
    return  'And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!'
def songoftheantsgomarching(num,actionname):
    getStart = startword(num,'hurrah! hurrah!') * 2 + startword(num)
    getMiddle = "The little one stops to %s,\n"%actionname
    getEnd = endword()
    return getStart + getMiddle + getEnd
def main():
    for num,actionname in [('one','suck his thumb'),('two','tie his shoe')]:
        print(actionname)
        print(songoftheantsgomarching(num,actionname))

if __name__=='__main__':
    main()