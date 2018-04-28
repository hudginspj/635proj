

def gen_data_training():
    pass


def gen_data_test():
    pass


def gen_data(out_file_name, ):
    pass


def fatima_x():
    files_path = "./features/fa"
    files = listdir(files_path)
    files.sort()
    # files.remove('test')
    #print(files)

    with open('./features/fa_feat_ProtrWeb.csv', 'w') as out_file:
        for i, fileName in enumerate(files):

            tk_path = path.join(files_path, fileName)
            print("Loading %s " % tk_path)
        
            with open(tk_path, 'r', encoding='utf-8') as features:        
                features_lines = features.readlines()
                if (i == 0):  # We only print the header with the features when reading the first file.
                    out_file.write(','.join(features_lines[0].strip().split(',')[0:]))
                    out_file.write('\n')
                
                for j in range(1, len(features_lines)):
                    feats = features_lines[j].strip()
                    feats = ','.join(feats.split(',')[0:])
                    
                    out_file.write(feats + '\n')

if __name__ == "__main__":
    gen_data_training()
