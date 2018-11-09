import sys,xlrd,os
def rename_filename(file= 'file.xls',sheet = 0):
    getdict_rename = {}
    try:
        data = xlrd.open_workbook(file)
        table = data.sheets()[sheet]
        nrows = table.nrows
        for rownum in range(1,nrows):
            getdict_rename[table.row_values(rownum)[0]] = table.row_values(rownum)[1]
        root_path = file[:file.rfind('\\')]
        for i in getdict_rename:
            if os.path.exists(root_path.replace('\\',r'\\')+r"\\"+i):
                os.rename(root_path.replace('\\',r'\\')+r"\\"+i,root_path.replace('\\',r'\\')+r"\\"+getdict_rename.get(i))
            else:
                pass
    except Exception as e:
        print(str(e))

print("请输入Excel文件的路径，且Excel文件与待替换文件夹在同一根路径下！")
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(len(sys.argv))
    print(str(sys.argv))
    print("传入参数有问题！")
    sys.exit()
else:
    excel_path = sys.argv[1]
    try:
        rename_filename(excel_path)
    except Exception as e:
        print("程序处理有误：" + str(e))