import xlrd
import xlwt
'''
    处理Excel文件，按指定列的内容拆分，并将拆分结果分别放入新的Excel中
'''
def open_excel_and_return_table(file= 'file.xls',sheet = 0):
    '''
    Connect The Excel And Return A Excel Object
    :param file: Excel Path
    :param sheet: The Sheet for Reading
    :return: Excel Reader Object
    '''
    try:
        data = xlrd.open_workbook(file)
        return data.sheets()[sheet]
    except Exception as e:
        print(str(e))
def get_excel_columns_info(table):
    '''
    Read The Title Of The Excel And Return It
    :param table: Excel Reader Object
    :return: List Of Excel Title
    '''
    excel_columns = table.row_values(0)
    return excel_columns
def get_column_data(table,columnIndex,titlecolumname=''):
    '''
    Get the Data of Designation Column That Will Be Grouped And Return A List Of Distinct Results
    :param table:Excel Reader Object
    :param columnIndex:The Index Of Designation Column
    :param titlecolumname:The Excel Title That Will Be Removing
    :return:A List Of Distinct Results
    '''
    excel_column_data = list(set(table.col_values(columnIndex)))
    if titlecolumname in excel_column_data:
        excel_column_data.remove(titlecolumname)
    return excel_column_data
def partition_by_column(outputpath,table,columndata,columnindex):
    '''
    According To Column Data And Get The Index Of Row，Get Row From Excel By Index And Write The Recode to Excel Writer
    Object,Finally Save The Excel Writer Object As A File Of Output Path
    :param outputpath:Output File Root Path
    :param table:Excel Reader Object
    :param columndata:The Column Data That Will Be Grouped
    :param columnindex:The Column Index That Will Be Grouped
    :return: A Output File Of Excel
    '''
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
    '''
    Main Function
    :param filepath: SourceFile Path
    :param partitioncolumn: Designation Column That Will Be Grouped
    :return: All Program Result
    '''
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