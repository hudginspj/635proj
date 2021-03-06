#FEATURES_FILENAME = 'nikki_features.csv'
FEATURES_FILENAME = 'fa_feat_ProtrWeb.csv'
DIFF_IN_INDEX = True  #To maintain the same class, True if the prediction file doesn't have the same indexes as the original data set.

def ignoreFirst(commaSeperatedLine):
    return ','.join(commaSeperatedLine.split(',')[1:])

with open('./spec/sequences_training.txt') as original:
    with open('./features/' + FEATURES_FILENAME) as features:
        with open('./features/pred-' + FEATURES_FILENAME, 'w') as out_file:
            original_lines = original.readlines()
            features_lines = features.readlines()
            out_file.write(ignoreFirst(features_lines[0].strip()) + ",class\n")
            # print(len(features_lines), len(original_lines))
            for i in range(1, len(features_lines)):
                # print(i, original_lines[i].__len__())

                if (DIFF_IN_INDEX):
                    feat_seq_number = features_lines[i].strip().split(',')[0].replace('"', '')
                    feat_seq_number = feat_seq_number[3:]               
                    prot_class = original_lines[int(feat_seq_number)-1].strip().split(',')[1]
                else:
                    prot_class = original_lines[i-1].strip().split(',')[1]
                
                feats = features_lines[i].strip()
                feats = ignoreFirst(feats) #Uncomment this line to ignore the first "feature" (seqn)
                out_file.write(feats + ', ' + prot_class + '\n')






