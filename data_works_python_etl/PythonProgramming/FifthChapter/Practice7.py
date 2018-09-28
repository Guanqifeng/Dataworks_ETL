# 凯撒密码是一种简单的替换密码，其思路是将明文消息的每个字母在字母表中移
# 动固定数字（称为密钥）。例如，如果键值为2，则单词“Sourpuss”将被编码为“Uqwtrwuu”。
# 原始消息可以通过使用密钥的负值“重新编码”来恢复。编写一个可以编码和解码凯撒
# 密码的程序。对程序的输入将是明文的字符串和密钥的值。输出将是一个编码消息，其
# 中原始消息中的每个字符都将被替换为Unicode 字符集中后移密钥个字符。例如，如果
# ch 是字符串中的字符，key 是要移位的量，则替换ch 的字符可以计算为chr（ord（ch）
# + key）。
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