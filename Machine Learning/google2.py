import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
# print(iris.feature_names)
# print(iris.target_names)

test_idx = [0, 50, 100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
# for i in range(len(test_target)):
# print("Example:{0}, label:{1}, features:{2}".format(i + 1, test_target[i], test_data[i]))
print(test_data)
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print(clf.predict(test_data))
print(test_target)
