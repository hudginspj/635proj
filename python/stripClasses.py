import textwrap
# print("hello")
with open('../spec/sequences_training.txt') as seq_file:
    with open('../sequences/strip_seqs.txt', 'w') as out_file:
        with open('../sequences/635.fasta', 'w') as fasta_file:
            counter = 0
            for line in seq_file.readlines():
                if counter >= 999:
                    break
                seq = line.split(',')[0]
                print(line)
                # print(seq)
                # print("---")
                out_file.write(f"{seq}\n")
                fasta_file.write(f">seq{counter}\n")
                fasta_file.write(textwrap.fill(seq, width=100))
                fasta_file.write("\n")
                counter += 1






