# 编写一个程序来打印歌曲“Old MacDonald”的歌词。你的程序应该打印五种不同
# 动物的歌词，类似于下面的例子。
# Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
# And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
# With a moo, moo here and a moo, moo there.
# Here a moo, there a moo, everywhere a moo, moo.
# Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!

def eeigh():
    return "Ee-igh, Ee-igh, Oh!\n"
def sing(animal):
    lyrics = "Old MacDonald had a farm, " + eeigh() +"And on that farm he had a {0}".format(animal) + eeigh() \
             +"With a {0},{1} here and a {2},{3} there \n".format(animal,animal,animal,animal) + \
             "Here a {0},there a {1}, everywhere a {2}, {3} .\n".format(animal,animal,animal,animal)+ \
             "Old MacDonald had a farm" + eeigh()
    return lyrics
if __name__=='__main__':
    print(sing("moo"))