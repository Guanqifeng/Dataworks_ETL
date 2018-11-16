import pandas as pd
import numpy as np

def read_csv_test(filepath):
    #读取csv文件（filepath），保留字段内容（header = 'infer'），以逗号分隔（sep=','）
    getData = pd.read_csv(filepath,sep=',',header = 'infer')
    return getData
def pandas_drop_test(pddata):
    # 删除默认列（'Unnamed: 0'），axis = 1代表列，axis = 0 代表 索引 inplace 默认是False 如果为True 将 空设为 None
    pddata.drop(['Unnamed: 0'],inplace =True,axis = 1)
    return pddata
def pandas_loc_test(pddata):
    return pddata.loc[0]
def pandas_isin_test(pddata):
    return pddata[pddata.age>45.0]
def get_pandase():
    result = pd.DataFrame([[1,2,3],[4,5,6]],columns=list('abc'))
    print(result)
if __name__ == '__main__':
   #csvpath = 'C:\\Users\\Administrator\\Desktop\\pandas_test.csv'
   #getPdData = read_csv_test(csvpath)
   #print(pandas_drop_test(getPdData))
   #print(pandas_loc_test(getPdData))
   #print(pandas_isin_test(getPdData))
   get_pandase()