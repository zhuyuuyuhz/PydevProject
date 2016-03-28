#coding:utf-8
from boto.gs.cors import HEADERS
from docutils.nodes import header
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
from sklearn.feature_extraction import DictVectorizer
import csv

allElecrronicsData = open('D:\DataSet\Computer_buyers.csv','rb')
reader = csv.reader(allElecrronicsData)

#打印reader读取的数据
# for line in reader:
#     print "line:",line

headers = reader.next()     
print "headers:" ,headers
 
featureList = []
labelList = []
 
for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1,len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print "featureList:",featureList
 
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print "dummyX:" + str(dummyX)
print "feature_names:",vec.get_feature_names()
 
print "labellist:" + str(labelList)
 
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print "dummyY:" + str(dummyY)
 
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
print "clf:" + str(clf)
 
 
#可视化模型
with open("allElectronicInformationGain.dot",'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(),out_file = f)
     
oneRowX = dummyX[0,:]
print "oneRowX:" + str(oneRowX)
 
#预测新人newRowX（修改了第一个和第三个属性值）
newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print "newRowX:" + str(newRowX)
 
predictedY = clf.predict(newRowX)
print "predictedY:" + str(predictedY)