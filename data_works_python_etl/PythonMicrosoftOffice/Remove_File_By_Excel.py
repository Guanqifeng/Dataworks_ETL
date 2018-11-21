import os,sys,xlrd
import shutil
def read_excel(excel_path,sheet = 0):
    try:
        data = xlrd.open_workbook(excel_path)
        excel_table_obj = data.sheets()[sheet]
        excel_column_data = []
        nrows = excel_table_obj.nrows
        for i in range(1, nrows):
            excel_column_data.append(excel_table_obj.row_values(i)[0])
        return excel_column_data
    except Exception as e:
        print(str(e))
def remove_file(excel_list,folder_path):
    removeFolder = folder_path+r'\\'+"被移动文件"
    if os.path.exists(removeFolder):
        pass
    else:
        os.mkdir(removeFolder)
    for foldername in excel_list:
        shutil.move(folder_path+'\\'+foldername, removeFolder+'\\'+foldername)

if len(sys.argv) < 3 or len(sys.argv) > 3:
    print(len(sys.argv))
    print(str(sys.argv))
    print("传入参数有问题，需要两条参数（Excel文件路径 与 根目录）！")
    sys.exit()
else:
    excel_path,root_path = sys.argv[1],sys.argv[2]
    getExcelList = read_excel(excel_path)
    remove_file(getExcelList, root_path)
# if __name__ == '__main__':
#    excel_path = 'C:\\Users\\Administrator\\Desktop\\1119公司资料拆分需求-gqf\\公司列表.xlsx'
#    folder_path = 'C:\\Users\\Administrator\\Desktop\\1119公司资料拆分需求-gqf\\'
#    getExcelList = read_excel(excel_path)
#    remove_file(getExcelList,folder_path)