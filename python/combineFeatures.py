from os import listdir, path
import json
import csv

#
# Combine the features generated from the three tools into one file.
#

def ignoreFirst(commaSeperatedLine):
    return ','.join(commaSeperatedLine.split(',')[1:])

def dontIgnoreFirst(commaSeperatedLine):
    return ','.join(commaSeperatedLine.split(',')[0:])   

with open('./features/nikki_features.csv') as nikki:
    with open('./training_data/pred-profeat.csv') as paul:
        with open('./features/fa_feat_ProtrWeb.csv') as fa:
            with open('./training_data/all_features.csv', 'w') as out_file:
                nikki_lines = nikki.readlines()
                paul_lines = paul.readlines()
                fa_lines = fa.readlines()

                out_file.write(ignoreFirst(fa_lines[0].strip()) + ', ' + ignoreFirst(nikki_lines[0].strip()) + ', ' + dontIgnoreFirst(paul_lines[0].strip()) + "\n") #Paul's file already has the class

                for i in range(1, len(fa_lines)):
                    feat_seq_number = fa_lines[i].strip().split(',')[0].replace('"', '')
                    feat_seq_number = feat_seq_number[3:]               
                    idx_seq = int(feat_seq_number)                      

                    feats_fa = fa_lines[i].strip()
                    feats_fa = ignoreFirst(feats_fa) #Uncomment this line to ignore the first "feature" (seqn)
                
                    feats_nikki = nikki_lines[idx_seq].strip()
                    feats_nikki = ignoreFirst(feats_nikki)
                
                    feats_paul = paul_lines[idx_seq].strip()
                    feats_paul = dontIgnoreFirst(feats_paul)

                    out_file.write(feats_fa + ', ' + feats_nikki + ', ' + feats_paul + '\n')