

import numpy as np
import csv

def xsAndYs(filename):
    xsArr = []
    ysArr = []
    with open(filename, 'r') as csvfile:
        csvfile.readline() # Ignore first line
        reader = csv.reader(csvfile, delimiter=',',)
        counter = 0
        for row in reader:
            if (len(row) != 1438):
                # print(counter, len(row))
                continue                             ##################TODO figure out what the hell is happening here
            xsArr.append(row[0:-1])  #Started with 1 for some reason
            ysArr.append(row[-1])
            counter += 1
    xs = np.array(xsArr)
    ys = np.array(ysArr)
    # print(xs.shape)
    return xs, ys

if __name__=="__main__":
    # xsAndYs("training_data/pred-seq-34702.out")
    xsAndYs("training_data/pred-profeat.csv")