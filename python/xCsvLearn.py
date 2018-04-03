import sklearn
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import csvToExamples
import csv
from sklearn.model_selection import cross_val_score
# xsArr = []
# ysArr = []
# with open('../features/pred-seq-34702.out', 'r') as csvfile:
#     csvfile.readline() # Ignore first line
#     reader = csv.reader(csvfile, delimiter=',',)
#     for row in reader:
#         # print(len(row))
#         xsArr.append(row[1:-1])
#         ysArr.append(row[-1])


# X = np.array(xsArr)
# Y = np.array(ysArr)

(xs, ys) = csvToExamples.xsAndYs('../features/pred-seq-34702.out')

clf = RandomForestClassifier()
# clf.fit(xs[:-10], ys[:-10])
# pred = clf.predict(xs[-10:])
# print(pred)
# print(ys[-10:])

scores = cross_val_score(clf, xs, ys, cv=5)
print(scores)