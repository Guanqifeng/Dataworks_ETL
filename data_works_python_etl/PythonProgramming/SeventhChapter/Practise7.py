# 如果一个人至少30 岁，并且成为美国公民至少9 年，就有资格成为美国参议员。
# 作为美国众议员，年限分别是25 岁和7 年。编写一个程序，接受一个人的年龄和公民年数
# 作为输入，并输出他的参议院和众议院资格。
def isUSOfRepresentatives(age,years):
    if age >= 25 and years >= 7:
        return "Is A Representatives"
    else:
        return "Is Not A Representatives"
if __name__ == '__main__':
    age,years = eval(input("Please Input Your Age And Years Of Live In USA (age,years):"))
    print(isUSOfRepresentatives(age,years))