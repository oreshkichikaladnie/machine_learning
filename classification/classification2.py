import random
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import tree

# Обработка данных
X = []
Y = []
t = 0
dataset = open("agaricus-lepiota.data")
data = pd.DataFrame()
da={"cs":[],"cu":[],"cc":[],"b":[],"o":[],"ga":[],"gs":[],"gi":[],"class":[]}
for line in dataset:
    if t < 180:
        da["cs"].append(line[0])
        da["cu"].append(line[2])
        da["cc"].append(line[4])
        da["b"].append(line[6])
        da["o"].append(line[8])
        da["ga"].append(line[10])
        da["gs"].append(line[12])
        da["gi"].append(line[14])
        da["class"].append(random.randint(0, 7))
        t += 1
data["cs"]=da["cs"]
data["cu"]=da["cu"]
data["cc"]=da["cc"]
data["b"]=da["b"]
data["o"]=da["o"]
data["ga"]=da["ga"]
data["gs"]=da["gs"]
data["gi"]=da["gi"]
data["class"]=da["class"]

clf = DecisionTreeClassifier()

one_hot_data = pd.get_dummies(data[['cs','cu','cc','b','o','ga','gs','gi']],drop_first=True)
clf.fit(one_hot_data, data['class'])

print(tree.plot_tree(clf))

plt.figure()
plot_tree(clf, filled=True)
plt.show()