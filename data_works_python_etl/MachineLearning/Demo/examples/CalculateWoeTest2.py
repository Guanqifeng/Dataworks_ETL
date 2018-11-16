# coding = utf-8
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import Imputer

from sklearn.linear_model.logistic import LogisticRegression
from sklearn import tree

# 忽略警告错误的输出
import warnings

warnings.filterwarnings('ignore')


# 用数据集构造随机森林分类器模型
# 加载数据（训练和测试）
# preprocessing
# split training_data into training_new&test_new to verify model
# use mean_value to replace default_value with the method Imputer
# build a RandomForestModel with training_new
# deal with the unbalanced data problem
# perform parameters'ajustment with GridSearchCV in CrossValidation
# export best model and test it with data_test

# 创建字典函数
# input: keys = [] and values = []
# output: dict{}


def create_dict(keys, vals):
    lookup = {}
    if len(keys) == len(vals):
        for i in range(len(keys)):
            key = keys[i]
            val = vals[i]
            lookup[key] = val
    return lookup


# 计算AUC函数
# input: y_true = [] and y_score = []
# output: auc


def compute_auc(y_true, y_score):
    auc = roc_auc_score(y_true, y_score)
    print('auc', auc)
    return auc


def main():
    # 1,加载数据（训练和测试）和预处理数据
    colnames = ['ID', 'label', 'RUUnsecuredL', 'age', 'NOTime30-59',
                'DebtRatio', 'Income', 'NOCredit', 'NOTimes90',
                'NORealEstate', 'NOTime60-89', 'NODependents']
    # 将数据集中没有意义的数值全部指定为‘NA'，比如年龄小于１８，
    col_nas = ['', 'NA', 'NA', 0, [98, 96], 'NA', 'NA', 'NA', [98, 96], 'NA', [98, 96], 'NA']
    col_na_values = create_dict(colnames, col_nas)
    dftrain = pd.read_csv('cs-training.csv', names=colnames,
                          na_values=col_na_values, skiprows=[0])
    # print(dftrain)
    # pop()返回删除的列，并默认本地删除
    train_id = [int(x) for x in dftrain.pop('ID')]
    y_train = np.asarray([int(x) for x in dftrain.pop('label')])
    x_train = dftrain.values

    dftest = pd.read_csv('cs-test.csv', names=colnames,
                         na_values=col_na_values, skiprows=[0])
    test_id = [int(x) for x in dftest.pop('ID')]
    y_test = np.asarray(dftest.pop('label'))
    x_test = dftest.values

    # 2,使用StratifiedShuffleSplit将训练数据分解为trainning_new和test_new(用于验证模型）
    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.33333, random_state=0)
    for train_index, test_index in sss.split(x_train, y_train):
        # print("TRAIN:", train_index, "TEST:", test_index)
        x_train_new, x_test_new = x_train[train_index], x_train[test_index]
        y_train_new, y_test_new = y_train[train_index], y_train[test_index]

    y_train = y_train_new
    x_train = x_train_new

    # 3,使用Imputer将所有NaN替换为平均值
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(x_train)
    x_train = imp.transform(x_train)
    x_test_new = imp.transform(x_test_new)
    x_test = imp.transform(x_test)

    # 使用training_new数据建立RF模型
    rf = RandomForestClassifier()

    # 模型比较
    # 逻辑回归，二分类模型
    lr = LogisticRegression()
    # 拟合逻辑回归模型
    lr.fit(x_train, y_train)
    # 预测训练集中各样本落入各个类别的概率
    predicted_probs_train = lr.predict_proba(x_train)
    # predict_proba()返回值是按目标类别自然排序的概率
    predicted_probs_train = [x[1] for x in predicted_probs_train]
    # 计算AUC值
    compute_auc(y_train, predicted_probs_train)

    # 预测测试集中各样本落入各个类别的概率
    predicted_probs_test_new = lr.predict_proba(x_test_new)
    predicted_probs_test_new = [x[1] for x in predicted_probs_test_new]
    compute_auc(y_test_new, predicted_probs_test_new)

    # 树模型中的决策树模型
    model = tree.DecisionTreeClassifier()
    model.fit(x_train, y_train)
    predicted_probs_train = model.predict_proba(x_train)
    predicted_probs_train = [x[1] for x in predicted_probs_train]
    compute_auc(y_train, predicted_probs_train)

    predicted_probs_test_new = model.predict_proba(x_test_new)
    predicted_probs_test_new = [x[1] for x in predicted_probs_test_new]
    compute_auc(y_test_new, predicted_probs_test_new)

    # 随机森林
    rf.fit(x_train, y_train)
    # 模型AUC值比较
    predicted_probs_train = rf.predict_proba(x_train)
    predicted_probs_train = [x[1] for x in predicted_probs_train]
    compute_auc(y_train, predicted_probs_train)

    predicted_probs_test_new = rf.predict_proba(x_test_new)
    predicted_probs_test_new = [x[1] for x in predicted_probs_test_new]
    compute_auc(y_test_new, predicted_probs_test_new)

    # 输出特征重要性评估
    print(sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), dftrain.columns), reverse=True))
    # 使用具有crossvalidation的网格搜索执行参数调整
    param_grid = {"max_features": [2, 3, 4], "min_samples_leaf": [50]}
    grid_search = GridSearchCV(rf, cv=10, scoring='roc_auc', param_grid=param_grid, iid=False)
    # 输出最佳模型
    # 使用最优参数和训练数据构建模型
    grid_search.fit(x_train, y_train)
    print('the best parameter:', grid_search.best_params_)
    print('the best score:', grid_search.best_score_)

    # 使用rf预测train
    predicted_probs_train = grid_search.predict_proba(x_train)
    predicted_probs_train = [x[1] for x in predicted_probs_train]
    compute_auc(y_train, predicted_probs_train)

    # 使用rf预测test
    predicted_probs_test_new = grid_search.predict_proba(x_test_new)
    predicted_probs_test_new = [x[1] for x in predicted_probs_test_new]
    compute_auc(y_test_new, predicted_probs_test_new)

    # 使用rf预测test data
    predicted_probs_test = grid_search.predict_proba(x_test)
    predicted_probs_test = ['%.9f' % x[1] for x in predicted_probs_test]
    submission = pd.DataFrame({'ID': test_id, 'Probability': predicted_probs_test})
    submission.to_csv('rf_submission.csv', index=False)


# 如果直接运行.py文件，则__name__ == '__main__'
# 如果是引入.py文件，则__name__　＝＝　文件名
if __name__ == '__main__':
    main()


