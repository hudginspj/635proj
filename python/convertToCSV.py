#import csv
#input_file = open('635_Prot.txt', 'r')
#output_file = open('some_tab_separated_file.csv', 'w')
#input_file.readline() # skip first line 
#for line in input_file:
 #   (FASTA_NAME,	Gs(U)_NO_ALA_N2,	Gs(U)_NO_AHR_N2,	Gs(U)_NO_AHR_Ar,	Gs(U)_NO_AHR_K,	Gs(U)_NO_AHR_SI50,	Gs(U)_NO_PRT_N2,	Gs(U)_NO_PRT_Ar,	Gs(U)_NO_PRT_K,	Gs(U)_NO_PRT_SI50,	Mw_NO_ALA_N2,	Mw_NO_AHR_N2,	Mw_NO_AHR_Ar,	Mw_NO_AHR_K,	Mw_NO_AHR_SI50,	Mw_NO_PRT_N2,	Mw_NO_PRT_Ar,	Mw_NO_PRT_K,	Mw_NO_PRT_SI50) = line.strip().split('\t')
 #   output_file.write(','.join([FASTA_NAME,	Gs(U)_NO_ALA_N2,	Gs(U)_NO_AHR_N2,	Gs(U)_NO_AHR_Ar,	Gs(U)_NO_AHR_K,	Gs(U)_NO_AHR_SI50,	Gs(U)_NO_PRT_N2,	Gs(U)_NO_PRT_Ar,	Gs(U)_NO_PRT_K,	Gs(U)_NO_PRT_SI50,	Mw_NO_ALA_N2,	Mw_NO_AHR_N2,	Mw_NO_AHR_Ar,	Mw_NO_AHR_K,	Mw_NO_AHR_SI50,	Mw_NO_PRT_N2,	Mw_NO_PRT_Ar,	Mw_NO_PRT_K,	Mw_NO_PRT_SI50) = line.strip().split('\t']) + '\n')
#input_file.close()
#output_file.close()



import csv


# with open(filename, 'r') as csvfile:
#         csvfile.readline() # Ignore first line
#         reader = csv.reader(csvfile, delimiter=',',)
#         for row in reader:
with open('635_all_2_Prot.txt', 'r') as in_file:
    with open('../features/nikki_features.csv', 'w') as out_file:
        for line in in_file:
            string_values = line.strip().split()
            row = []
            for string_value in string_values:
                row.append(string_value.replace(",", ""))
            newLine = ",".join(row)
            out_file.write(newLine + "\n")
        

#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)

# with open('635_Prot.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     with open('log.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)