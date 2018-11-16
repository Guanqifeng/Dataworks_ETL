#利用 Try和except 结构抛出异常并获取异常，最后输出提示！

if __name__ == '__main__':
    try:
        with open('C:\\sdads.txt', 'r') as file: # 一个不存在的路径
            print(file.read())
    except Exception as e:
        print("获取不到来路径，异常信息如下：")
        print(str(e))



