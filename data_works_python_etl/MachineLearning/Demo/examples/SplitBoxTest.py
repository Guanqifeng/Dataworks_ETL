import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 随机生成一段成绩
if __name__ == '__main__':
    score_list = np.random.randint(25, 100, size=20)
    print(score_list)
    bins = [0, 59, 70, 80, 100]
    getresult1 = pd.cut(score_list, bins)
    print(getresult1)
    score_cat = pd.cut(score_list, bins)
    getresult2 = pd.value_counts(score_cat)
    print(getresult2)
    df = DataFrame()
    df['score'] = score_list
    print(df)
    df['student'] = [pd.util.testing.rands(3) for i in range(20)]
    print(df)
    print(pd.cut(df['score'], bins))
    df['categories'] = pd.cut(df['score'], bins, labels=['low','ok','good','great'])
    print(df)