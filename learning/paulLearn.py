import sklearn
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import csvToExamples
import csv
from sklearn.model_selection import cross_val_score
import sklearn.metrics as metrics
import math
import pickle

first = True

def avgMcc(clf, xs, ys):
    global first
    if first:
        print("MCC:")
        print(clf)
        print(xs)
        print(ys)
        print("-----")
    first = False
    pred = clf.predict(xs)
    print("finished prediction")
    # pred = [0] * len(ys)
    # pred = ys
    # score = metrics.accuracy_score(ys, pred)
    # score = clf.score(xs, ys) 
    # print("score ", score)
    score = metrics.matthews_corrcoef(ys, pred)
    return score

def learnOn(filename, threshold):
    (xs, ys) = csvToExamples.xsAndYs(filename)


    clf = RandomForestClassifier()


    # clf.fit(xs[:-10], ys[:-10])
    # pred = clf.predict(xs[-10:])
    # print(pred)
    # print(ys[-10:])
    # importances = clf.feature_importances_
    # features = csvToExamples.feature_list(filename)
    # print(importances)
    # for i in range(len(importances)):
    #     if importances[i] > threshold:
    #         print(features[i], importances[i])

    # pickle.dump(importances,open('learning/save.p','wb'))


    

    scores = cross_val_score(clf, xs, ys, cv=5, scoring=avgMcc)
    # scores = cross_val_score(clf, xs, ys, cv=5, scoring=None)
    print(filename)
    print(scores)
    print(np.mean(scores))
    

if __name__ == "__main__":
    # learnOn('./features/pred-seq-34702.out')
    # learnOn('./training_data/pred-profeat.csv', 0.006)
    # learnOn('./features/pred-ProtrWeb-aac.csv')
    #learnOn('./features/pred-nikki_features.csv')
    learnOn('./features/pred-fa_feat_ProtrWeb.csv', 0.001)
