FEATURES_FILENAME = 'nikki_features.csv'

def ignoreFirst(commaSeperatedLine):
    return ','.join(commaSeperatedLine.split(',')[1:])

with open('../spec/sequences_training.txt') as original:
    with open('../features/' + FEATURES_FILENAME) as features:
        with open('../features/pred-' + FEATURES_FILENAME, 'w') as out_file:
            original_lines = original.readlines()
            features_lines = features.readlines()
            out_file.write(ignoreFirst(features_lines[0].strip()) + ",class\n")
            for i in range(1, len(features_lines)):
                prot_class = original_lines[i].strip().split(',')[1]
                feats = features_lines[i].strip()
                feats = ignoreFirst(feats) #Uncomment this line to ignore the first "feature" (seqn)
                out_file.write(feats + ', ' + prot_class + '\n')







