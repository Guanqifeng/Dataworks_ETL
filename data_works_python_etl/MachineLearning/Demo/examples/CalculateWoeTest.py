# C:\\Users\\Administrator\\Desktop\\all\\cs-training.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

def load_data():
    df_train=pd.read_csv('C:\\Users\\Administrator\\Desktop\\all\\cs-training.csv',sep=',',header='infer')
    df_train.drop(['Unnamed: 0'],inplace=True,axis=1)
    return df_train

def outlier_check(df,c_name):
    p = df[[c_name]].boxplot(return_type='dict')
    df = df[df['RevolvingUtilizationOfUnsecuredLines'] < 10000] #只取信用额度小于10000的记录，客户群集中
    df = df[np.logical_and(df['age'] > 0, df['age'] < 90)]#只取年龄在0-90之间的客户群
    df = df[df['NumberOfTime30-59DaysPastDueNotWorse'] < 20] #只取 35-59天逾期但不糟糕次数 小于20次的客户群
    df = df[df['DebtRatio'] < 50000] #只取负债比率在50000以下的客户群
    df = df[df['MonthlyIncome'] < 500000]#只取月收入在500000以下的客户群
    df = df[df['NumberOfTimes90DaysLate'] < 20]#只取 90天逾期次数 在 20次以内的客户群
    df = df[df['NumberRealEstateLoansOrLines'] < 6]#只取不动产贷款的数量在6个以下的客户群
    df = df[df['NumberOfTime60-89DaysPastDueNotWorse'] < 20]# 只取 60-89天逾期次数 在 20次以内的客户群
    df = df[df['NumberOfDependents'] < 3]#只取 不包含本人的家属数量小于3 的客户群
    return df
    # x_outliers=p['fliers'][0].get_xdata()
    # y_outliers = p['fliers'][0].get_ydata()
    # for j in range(1):
    #     plt.annotate(y_outliers[j], xy=(x_outliers[j], y_outliers[j]), xytext=(x_outliers[j] + 0.02, y_outliers[j]))
    # plt.show()
def check_na(df):
    print(df.count(axis=0))

def SMOTE_sample(inputX,index,test_Ratio=0.2):
    from random import sample
    data_array=np.atleast_1d(inputX)
    class_array=np.unique(data_array)
    test_list=[]
    #train_list=[]
    for c in class_array:
        temp=[]
        for i,value in enumerate(data_array):
            if value==c:
                temp.append(index[i])
        test_list.extend(sample(temp,int(len(temp)*test_Ratio)))
    return list(set(index) - set(test_list)), test_list

def split_sample(df_train):
    train_list,test_list=SMOTE_sample(df_train['SeriousDlqin2yrs'].tolist(),df_train.index.tolist())
    df_train_section=df_train.loc[train_list,:]
    df_test_section=df_train.loc[test_list,:]
    # print(df_train_section)
    return df_train_section,df_test_section

def WOE_Convert(input,sp,rank):
    result=[]
    for v in input:
        for i in range(len(sp)):
            if i<len(sp)-1:
                if v>=sp[i] and v<sp[i+1]:
                    result.append(rank[i])
                    break
            else:
                if v>=sp[i]:
                    result.append(rank[i])
                else:
                    result.append(np.NaN)
    return result

def Discrete_Value(df):
    df['RevolvingUtilizationOfUnsecuredLines']=WOE_Convert(df['RevolvingUtilizationOfUnsecuredLines'],[0,0.03,0.12,0.4,0.8],[1,0,2,3,4])
    df['age'] = WOE_Convert(df['age'],[0,40,50,60,70] ,[4,3,2,1,0])
    df['NumberOfTime30-59DaysPastDueNotWorse'] = WOE_Convert(df['NumberOfTime30-59DaysPastDueNotWorse'],[0,1,2] ,[0,1,2])
    df['DebtRatio'] = WOE_Convert(df['DebtRatio'],[0,1,2] ,[0,1,2])
    df['MonthlyIncome'] = WOE_Convert(df['MonthlyIncome'],[0,1000,5000,10000] ,[2,0,1,3])
    df['NumberOfOpenCreditLinesAndLoans'] = WOE_Convert(df['NumberOfOpenCreditLinesAndLoans'],[0,5,8,13],[3,1,0,2])
    df['NumberOfTimes90DaysLate'] = WOE_Convert(df['NumberOfTimes90DaysLate'], [0,1],[0,1])
    df['NumberRealEstateLoansOrLines'] = WOE_Convert(df['NumberRealEstateLoansOrLines'], [0,1,2],[2,0,1])
    df['NumberOfTime60-89DaysPastDueNotWorse'] = WOE_Convert(df['NumberOfTime60-89DaysPastDueNotWorse'],[0,1],[0,1])
    df['NumberOfDependents'] = WOE_Convert(df['NumberOfDependents'],[0,1,2],[0,1,2])
def cal_woe(df):
    groups = df.shape[0] #分箱字段
    all_0 = df['bad'].sum()
    all_1 = df['good'].sum()
    for i in range(groups):
        tmpWOE = np.log((df.loc[i, 'good'] * 1.0 / all_1) / (df.loc[i, 'bad'] * 1.0 / all_0))
        tmpIV = ((df.loc[i, 'good'] * 1.0 / all_1) - (df.loc[i, 'bad'] * 1.0 / all_0)) * tmpWOE
        df.loc[i, 'woe'] = tmpWOE
        df.loc[i, 'iv'] = tmpIV
    return df

def split_feature_box(df):
    RevolvingUtilizationOfUnsecuredLines_Bins = [0, 0.03, 0.12, 0.40, 0.80]
    df['categories'] = pd.cut(df['RevolvingUtilizationOfUnsecuredLines'], RevolvingUtilizationOfUnsecuredLines_Bins,labels=['low','ok','good','great'])
    #getDistinctCategories = list(df.drop_duplicates('categories')['categories'])
    getDistinctCategories = ['good', 'great', 'low', 'ok']
    df_Statistics = []
    for i in getDistinctCategories:
        good,bad = list(df[df['categories'].isin([i])].groupby(['categories','SeriousDlqin2yrs']).size())
        tmp = [i,good,bad]
        df_Statistics.append(tmp)
    return pd.DataFrame(df_Statistics,columns=['Sep_Point','good','bad'])
    #print(getDistinctCategories)
    #for i in df['categories']:
if __name__ == '__main__':
    df_train = load_data()
    # print(df_train)
    df_train = outlier_check(df_train,'NumberOfDependents')#数据预处理
    #check_na(df_train)  #查看数据预处理后的数量
    #df_train, df_test = split_sample(df_train) # 数据拆分 拆分成“检验数据”和“测试数据”
    #print(df_train)
    df_train_statistics = split_feature_box(df_train)
    df_train_statistics = cal_woe(df_train_statistics)
    print(df_train_statistics)
    # print(df_train_statistics.loc[0, 'bad'])
    # print(df_train_statistics['bad'].sum())
    #print(cal_woe(df_train_statistics))
    #WOE数据离散化 检验数分箱
    #print(df_train)
    #print(df_train)
    # writer = pd.ExcelWriter('C:\\Users\\Administrator\\Desktop\\Split_Result.xlsx')
    # df_train.to_excel(writer, 'Train', index=False)
    # writer.save()
    # Y_Train = df_train['SeriousDlqin2yrs'].values.tolist()
    # df_train = df_train.drop(['SeriousDlqin2yrs'], axis=1)
    # x = np.array(df_train.values.tolist()).T
    # Mcov = np.corrcoef(x)
    # df_exl = pd.DataFrame(data=Mcov)
    # writer = pd.ExcelWriter('C:\\Users\\Administrator\\Desktop\\Split_Result.xlsx')
    # df_exl.to_excel(writer, 'cov', index=False)
    # writer.save()


