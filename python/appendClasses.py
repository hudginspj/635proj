import textwrap
# print("hello")
FEATURES_FILENAME = 'seq-34702.out'
with open('../spec/sequences_training.txt') as original:
    with open('../features/' + FEATURES_FILENAME) as features:
        with open('../features/classes-' + FEATURES_FILENAME, 'w') as out_file:
            original_lines = original.readlines()
            features_lines = features.readlines()
            out_file.write(features_lines[0] + ", class\n")
            for i in range(1, len(features_lines)):
                prot_class = original_lines[i].split(',')[1]
                feats = features_lines[i]
                out_file.write(feats + ", " + prot_class + "\n")
                






