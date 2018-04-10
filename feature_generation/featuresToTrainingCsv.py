import os
# FEATURES_FILENAME = 'nikki_features.csv'

def ignoreFirst(commaSeperatedLine):
    return ','.join(commaSeperatedLine.split(',')[1:])

def process_segment(features_lines, original_file, out_file):
    for i in range(1, len(features_lines)):
        original_line = original_file.readline()
        prot_class = original_line.strip().split(',')[1]
        features = features_lines[i].strip()
        features = ignoreFirst(features) #Uncomment this line to ignore the first "feature" (seqn)
        out_file.write(features + ', ' + prot_class + '\n')

def process_all(features_prefix):
    first_file = True
    with open('./spec/sequences_training.txt') as original_file:
        with open(f"./training_data/pred-{features_prefix}.csv", 'w') as out_file:
            for features_filename in os.listdir("./features"):
                if features_filename.startswith(features_prefix):
                    with open('./features/' + features_filename) as features:
                        features_lines = features.readlines()
                        if first_file:
                            out_file.write(ignoreFirst(features_lines[0].strip()) + ",class\n")
                            first_file = False
                        process_segment(features_lines, original_file, out_file)
                        
            
if __name__ == "__main__":
    process_all("profeat")

                
                
            







