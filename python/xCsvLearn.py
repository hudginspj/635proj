import sklearn
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import csv
xsArr = []
ysArr = []
with open('../features/pred-seq-34702.out', 'r') as csvfile:
    csvfile.readline() # Ignore first line
    reader = csv.reader(csvfile, delimiter=',',)
    for row in reader:
        xsArr.append(row[1:-1])
        ysArr.append(row[-1])


X = np.array(xsArr)
Y = np.array(ysArr)


clf = RandomForestClassifier()
clf.fit(X[:100], Y[:100])
pred = clf.predict(X[-10:])

# f = open('../features/seq-34702.out')
# f.readline()  # skip the header
# data = np.loadtxt(f, delimiter=',')
# X = data[:, 1:]  # select columns 1 through end
# y = data[:, 0]   # select column 0, the stock price
# print(y)