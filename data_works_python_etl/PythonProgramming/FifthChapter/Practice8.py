# 上一个练习有一个问题，它不处理“超出字母表末端”的情况。真正的凯撒密码以
# 循环方式移动，其中“z”之后的下一个字符是“a”。修改上一个问题的解决方案，让它循
# 环。你可以假定输入只包含字母和空格。（提示：创建一个包含字母表所有字符的字符串，
# 并使用此字符串中的位置作为代码。你不必将“z”转换成“a”，只需确保在字母表字符串
# 中对整个字符序列中使用循环移位。）
def main():
    print("Enter the Public_Password that you want to change Private_Password!")
    Public_Password = input("Please enter your password:")
    num  = input("Please Enter you want key of Private_Password(1-10):")
    pp_list = []
    for i in Public_Password:
        pp_list.append(chr(ord(i)+int(num)))
    Private_Password = ''.join(pp_list)
    print("PublicPassword: "+Public_Password+" will be Changed to PrivatePassword: "+ Private_Password)
if __name__ == '__main__':
    main()