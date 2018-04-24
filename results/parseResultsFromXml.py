from os import listdir, path
from computeResults import calc_sensitivity, calc_specificity, calc_predictive_acc, calc_mcc, calc_avg_mcc
import json
import csv
import xml.etree.ElementTree as ET

RESULTS_FILENAME = 'results02.xml'

def parseXML(): 
    # create element tree object
    tree = ET.parse('./results/' + RESULTS_FILENAME)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    counter = root.find('PerformanceVector').find('AverageVector').find('default').find('averagesList').find('kappa').find('kappa').find('default').find('counter')
    values = []
    # iterate child elements of item
    for item in counter.findall('double-array/double'): 
        # append news dictionary to news items list
        values.append(item.text)
     
    #print(values)
    # return news items list
    return values

values = parseXML()
w, h = 4, 4
matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(w):
    if (i == 0):
        matrix[0][i] = values[i]
        matrix[1][i] = values[i+1]
        matrix[2][i] = values[i+2]
        matrix[3][i] = values[i+3]
        #print(matrix)
    elif (i == 1):
        matrix[0][i] = values[i+3]
        matrix[1][i] = values[i+4]
        matrix[2][i] = values[i+5]
        matrix[3][i] = values[i+6]
        #print(matrix)
    elif (i == 2):
        matrix[0][i] = values[i+6]
        matrix[1][i] = values[i+7]
        matrix[2][i] = values[i+8]
        matrix[3][i] = values[i+9]
        #print(matrix)
    elif (i == 3):
        matrix[0][i] = values[i+9]
        matrix[1][i] = values[i+10]
        matrix[2][i] = values[i+11]
        matrix[3][i] = values[i+12]
        #print(matrix)
print('Confusion Matrix')        
print(matrix)    

dna_tp = float(matrix[0][0])
dna_tn = float(matrix[1][0]) + float(matrix[2][0]) + float(matrix[3][0])
dna_fp = float(matrix[0][1]) + float(matrix[0][2]) + float(matrix[0][3])
dna_fn = float(matrix[1][1]) + float(matrix[1][2]) + float(matrix[1][3]) + float(matrix[2][1]) + float(matrix[2][2]) + float(matrix[2][3]) + float(matrix[3][1]) + float(matrix[3][2]) + float(matrix[3][3])
print("\nDNA -> TP: {} TN: {} FP: {} FN: {}".format(dna_tp, dna_tn, dna_fp, dna_fn))

rna_tp = float(matrix[1][1])
rna_tn = float(matrix[0][1]) + float(matrix[2][1]) + float(matrix[3][1])
rna_fp = float(matrix[1][0]) + float(matrix[1][2]) + float(matrix[1][3])
rna_fn = float(matrix[0][0]) + float(matrix[0][2]) + float(matrix[0][3]) + float(matrix[2][0]) + float(matrix[2][2]) + float(matrix[2][3]) + float(matrix[3][0]) + float(matrix[3][2]) + float(matrix[3][3])
print("RNA -> TP: {} TN: {} FP: {} FN: {}".format(rna_tp, rna_tn, rna_fp, rna_fn))

drna_tp = float(matrix[2][2])
drna_tn = float(matrix[0][2]) + float(matrix[1][2]) + float(matrix[3][2])
drna_fp = float(matrix[2][0]) + float(matrix[2][1]) + float(matrix[2][3])
drna_fn = float(matrix[0][0]) + float(matrix[0][1]) + float(matrix[0][3]) + float(matrix[1][0]) + float(matrix[1][1]) + float(matrix[1][3]) + float(matrix[3][0]) + float(matrix[3][1]) + float(matrix[3][3])
print("DRNA -> TP: {} TN: {} FP: {} FN: {}".format(drna_tp, drna_tn, drna_fp, drna_fn))

non_tp = float(matrix[3][3])
non_tn = float(matrix[0][3]) + float(matrix[1][3]) + float(matrix[2][3])
non_fp = float(matrix[3][0]) + float(matrix[3][1]) + float(matrix[3][2])
non_fn = float(matrix[0][0]) + float(matrix[0][1]) + float(matrix[0][2]) + float(matrix[1][0]) + float(matrix[1][1]) + float(matrix[1][2]) + float(matrix[2][0]) + float(matrix[2][1]) + float(matrix[2][2])
print("nonDRNA -> TP: {} TN: {} FP: {} FN: {}".format(non_tp, non_tn, non_fp, non_fn))

# Compute measures
print('\nComputing measures..')
dna_sens = calc_sensitivity(dna_tp, dna_fn)
dna_spec = calc_specificity(dna_tn, dna_fp)
dna_pred_acc = calc_predictive_acc(dna_tp, dna_tn, dna_fp, dna_fn)
dna_mcc = calc_mcc(dna_tp, dna_tn, dna_fp, dna_fn)
print("DNA -> SENS: {} SPEC: {} PRED_ACC: {} MCC: {}".format(dna_sens, dna_spec, dna_pred_acc, dna_mcc))

rna_sens = calc_sensitivity(rna_tp, rna_fn)
rna_spec = calc_specificity(rna_tn, rna_fp)
rna_pred_acc = calc_predictive_acc(rna_tp, rna_tn, rna_fp, rna_fn)
rna_mcc = calc_mcc(rna_tp, rna_tn, rna_fp, rna_fn)
print("RNA -> SENS: {} SPEC: {} PRED_ACC: {} MCC: {}".format(rna_sens, rna_spec, rna_pred_acc, rna_mcc))

drna_sens = calc_sensitivity(drna_tp, drna_fn)
drna_spec = calc_specificity(drna_tn, drna_fp)
drna_pred_acc = calc_predictive_acc(drna_tp, drna_tn, drna_fp, drna_fn)
drna_mcc = calc_mcc(drna_tp, drna_tn, drna_fp, drna_fn)
print("DRNA -> SENS: {} SPEC: {} PRED_ACC: {} MCC: {}".format(drna_sens, drna_spec, drna_pred_acc, drna_mcc))

non_sens = calc_sensitivity(non_tp, non_fn)
non_spec = calc_specificity(non_tn, non_fp)
non_pred_acc = calc_predictive_acc(non_tp, non_tn, non_fp, non_fn)
non_mcc = calc_mcc(non_tp, non_tn, non_fp, non_fn)
print("nonDRNA -> SENS: {} SPEC: {} PRED_ACC: {} MCC: {}".format(non_sens, non_spec, non_pred_acc, non_mcc))

avg_mcc = calc_avg_mcc(dna_mcc, rna_mcc, drna_mcc, non_mcc)
print("Average MCC {}".format(avg_mcc))

