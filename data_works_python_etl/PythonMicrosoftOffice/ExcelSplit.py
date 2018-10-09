import xlrd
import xlwt
def open_excel_and_return_table(file= 'file.xls',sheet = 0):
    try:
        data = xlrd.open_workbook(file)
        return data.sheets()[sheet]
    except Exception as e:
        print(str(e))
def get_excel_columns_info(table):
    excel_columns = table.row_values(0)
    return excel_columns
def get_column_data(table,columnIndex,titlecolumname=''):
    excel_column_data = list(set(table.col_values(columnIndex)))
    if titlecolumname in excel_column_data:
        excel_column_data.remove(titlecolumname)
    return excel_column_data
def partition_by_column(outputpath,table,columndata,columnindex):
    outExcelPath = outputpath + "\\" + columndata + ".xlsx"
    filename = xlwt.Workbook()
    sheet = filename.add_sheet("sheet1")
    nrows = table.nrows
    partitionList = [0]
    outline = 0
    for i in range(nrows):
        if table.cell(i,int(columnindex)).value == columndata:
            partitionList.append(i)
    for line in partitionList:
        print(line)
        excleInfo = table.row_values(line)
        for c in range(len(excleInfo)):
            sheet.write(outline,c,excleInfo[c])
        outline += 1
    filename.save(outExcelPath)

def main(filepath,partitioncolumn):
    filePathList = filepath.split("\\")
    outputpath = '\\'.join(filePathList[0:-1])
    excelTable = open_excel_and_return_table(filepath,0)
    columnsList = get_excel_columns_info(excelTable)
    for column in columnsList:
        if column == partitioncolumn:
            columnIndex = columnsList.index(column)
            partColumnsList = get_column_data(excelTable,columnIndex,column)
            print(partColumnsList)
            for columndata in partColumnsList:
                partition_by_column(outputpath, excelTable, columndata, columnIndex)
        else:
            pass

if __name__ == '__main__':
    filepath = 'C:\\Users\\Administrator\\Desktop\\TOP5000·17年至今·收银宝-线上.xlsx' ##目标文件路径
    partitioncolumn = '所属分公司'  ##待拆分列名
    main(filepath,partitioncolumn)