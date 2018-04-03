# print("hello")
with open('../spec/sequences_training.txt') as seq_file:
    with open('strip_seqs.txt', 'w') as out_file:
        for line in seq_file.readlines():
            seq = line.split(',')[0]
            print(line)
            # print(seq)
            # print("---")
            out_file.write(seq + '\n')






