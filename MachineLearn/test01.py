import numpy
import pandas
import sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
import numpy as np

# 特征抽取
#
# 导入包
from sklearn.feature_extraction.text import CountVectorizer

# 实例化CountVectorizer

vector = CountVectorizer()

# 调用fit_transform输入并转换数据

res = vector.fit_transform(["life is short,i like python","life is too long,i dislike python"])

# 打印结果
print(vector.get_feature_names())

print(res.toarray())

