import textwrap

PROTEINS_PER_FILE = 1000

def open_segment_file(num, start):
    filename = f"./sequences/635_num_{num}_start_{start}.fasta"
    segment_file = open(filename, 'w')
    return segment_file
    

def convert_all():
    with open('./spec/sequences_training.txt') as seq_file:
        with open('./sequences/raw_sequences.txt', 'w') as out_file:
            with open('./sequences/635_all.fasta', 'w') as fasta_all_file:
                counter = 1
                segment_file = open_segment_file(PROTEINS_PER_FILE, counter)
                for line in seq_file.readlines():
                    if counter % PROTEINS_PER_FILE == 0:
                        segment_file.close()
                        segment_file = open_segment_file(PROTEINS_PER_FILE, counter)
                    seq = line.split(',')[0]
                    print(line)
                    # print(seq)
                    # print("---")
                    out_file.write(f"{seq}\n")
                    fasta_all_file.write(f">seq{counter}\n")
                    fasta_all_file.write(textwrap.fill(seq, width=100))
                    fasta_all_file.write("\n")
                    segment_file.write(f">seq{counter}\n")
                    segment_file.write(textwrap.fill(seq, width=100))
                    segment_file.write("\n")
                    counter += 1


if __name__ == "__main__":
    convert_all()





