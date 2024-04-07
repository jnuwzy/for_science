import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 使用相对路径读取data文件夹下的v2.xls文件
file_path = '../data/v2.xls'
df = pd.read_excel(file_path)

# 选择特征列和标签列
X = df.iloc[:, [2, 5, 6, 18, 20, 21]].values
y = df.iloc[:, 23].values

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建SVM分类器实例
clf = svm.SVC(kernel='linear')  # 线性核，您也可以尝试其他核函数，如'rbf'

# 训练SVM分类器
clf.fit(X_train, y_train)

# 使用训练好的模型进行预测
y_pred = clf.predict(X_test)

# 计算并打印预测的准确率
accuracy = accuracy_score(y_test, y_pred)
print("SVM分类器的准确率: {:.2f}%".format(accuracy * 100))