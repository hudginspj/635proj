import numpy as np
import csv

def xsAndYs(filename):
    xsArr = []
    ysArr = []
    with open(filename, 'r') as csvfile:
        csvfile.readline() # Ignore first line
        reader = csv.reader(csvfile, delimiter=',',)
        counter = 0
        first_row_len = None
        last_row = None
        for row in reader:
            if not first_row_len:
                first_row_len = len(row)
            if len(row) != first_row_len:
                print("malformed row: ", counter, " length: ", len(row), " should be: ", first_row_len)
                row = last_row                             ##################TODO figure out what the hell is happening here
            xsArr.append(row[0:-1])  #Started with 1 for some reason
            ysArr.append(row[-1])
            counter += 1
            last_row = row
    xs = np.array(xsArr)
    ys = np.array(ysArr)

    print(xs.shape)
    drnaCount = 0
    for y in ys:
        if y == " DRNA":
            drnaCount += 1
    print("DRNA count: ", drnaCount)
    return xs, ys

def feature_list(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',',)
        for row in reader:
            return row

if __name__=="__main__":
    # xsAndYs("training_data/pred-seq-34702.out")
    xsAndYs("training_data/pred-profeat.csv")
    # xsAndYs('./features/pred-nikki_features.csv')