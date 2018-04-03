

import numpy as np
import csv

def xsAndYs(filename):
    xsArr = []
    ysArr = []
    with open(filename, 'r') as csvfile:
        csvfile.readline() # Ignore first line
        reader = csv.reader(csvfile, delimiter=',',)
        for row in reader:
            # print(len(row))
            xsArr.append(row[1:-1])
            ysArr.append(row[-1])
    xs = np.array(xsArr)
    ys = np.array(ysArr)
    return xs, ys