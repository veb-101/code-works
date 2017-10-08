from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 1]]  # 0 - bumpy, 1 - smooth
labels = [0, 0, 1, 1]  # 0 - Apple, 1 - Apple
clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)
print(clf.predict([[160, 0]]))
