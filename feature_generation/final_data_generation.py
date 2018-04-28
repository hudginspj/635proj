from os import listdir, path
import csv

TRAIN_OR_TEST = "training"

def gen_data():
    classes = read_classes()
    fatima_features, fatima_rows = read_features(f"./features/{TRAIN_OR_TEST}_fatima")
    paul_features, paul_rows = read_features(f"./features/{TRAIN_OR_TEST}_paul")
    nikki_features, nikki_rows = read_features(f"./training_data/{TRAIN_OR_TEST}_nikki")
    with open(f"./training_data/{TRAIN_OR_TEST}_all.csv", 'w') as out_file:
        out_file.write(','.join(fatima_features))
        out_file.write(',')
        out_file.write(','.join(paul_features))
        out_file.write(','.join(nikki_features))
        out_file.write(',')
        out_file.write(',class\n')
        # for seq in fatima_rows.keys():
        for i in range(len(classes)):
            seq = f'seq{i+1}'
            # out_file.write(','.join(fatima_rows[seq]))
            # out_file.write(',')
            # try:
            paul_row = ','.join(paul_rows[seq])
            # except:
            #     print("couldn't load row for ", seq)
            out_file.write(paul_row)
            out_file.write(','.join(nikki_rows[seq]))
            out_file.write(',')
            out_file.write(f',{classes[seq]}\n')
            

def read_classes():
    classes = {}
    with open(f'./spec/sequences_{TRAIN_OR_TEST}.txt') as original:
        original_lines = original.readlines()
        for i in range(len(original_lines)):
            classes[f'seq{i+1}'] = original_lines[i].split(',')[-1].strip()
    return classes




def read_features(files_path):
    feature_names = []
    rows = {}

    files = listdir(files_path)
    files.sort()
    # files.remove('test')
    #print(files)

    for i, fileName in enumerate(files):

        tk_path = path.join(files_path, fileName)
        print("Loading %s " % tk_path)
    
        with open(tk_path, 'r', encoding='utf-8') as features:        
            features_lines = features.readlines()
            if (i == 0):  # We only print the header with the features when reading the first file.
                feature_names = features_lines[0].strip().split(',')[1:]
                #print(feature_names)
            
            for j in range(1, len(features_lines)):
                feats = features_lines[j].strip()
                feats = feats.split(',')
                rows[feats[0].strip('"')] = feats[1:]

                #print(feats[0:2])
    return feature_names, rows
                

if __name__ == "__main__":
    #read_features("./features/fa")
    gen_data()
    #read_features(f"./features/{TRAIN_OR_TEST}_paul")
