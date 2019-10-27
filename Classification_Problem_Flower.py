import pydotplus
import PyPDF4
import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from IPython.display import Image
import os
iris=load_iris()

print (iris.feature_names) #feature/meta data
print (iris.target_names) #level
print (iris.data[0])
print (iris.target[0])

for i in range(len(iris.target)):
    print("example %d: label %s, feature %s"%(i,iris.target[i],iris.data[i]))

test_idx=[0,50,100]

train_target=np.delete(iris.target,test_idx)
train_data=np.delete(iris.data,test_idx,axis=0)

test_target=iris.target[test_idx]
test_data=iris.data[test_idx]

clf=tree.DecisionTreeClassifier()

clf=clf.fit(train_data,train_target)

print(test_target)
print (clf.predict(test_data))

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)


import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("ighjgris.pdf")
graph = graphviz.Source(dot_data)
