import math
import sklearn.metrics as metrics

def calc_sensitivity(tp, fn):
    return 100 * (tp / (tp + fn))

def calc_specificity(tn, fp):
    return 100 * (tn / (tn + fp))

def calc_predictive_acc(tp, tn, fp, fn):
    return 100 * ((tp+tn) / (tp+fp+tn+fn))


def calc_mcc(tp, tn, fp, fn):
    s1 = (tp+fp)
    s2 = (tp+fn)
    s3 = (tn+fp)
    s4 = (tn+fn)
    prd = s1 * s2 * s3 * s4
    #print('s1: {} - s2: {} - s3: {} - s4: {} - prd {}'.format(s1, s2, s3, s4, prd))
    if (prd == 0):
        return 0

    sq = math.sqrt(prd)
    #print('sq: {}'.format(sq))
    return abs((tp*tn - fp*fn) / sq)

def calc_class_mcc(ys, pred, cla):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(ys)):
        if ys[i] == cla and pred[i] == cla:
            tp += 1
        elif ys[i] != cla and pred[i] != cla:
            tn += 1
        elif ys[i] != cla and pred[i] == cla:
            fp += 1
        elif ys[i] == cla and pred[i] != cla:
            fn += 1
    print(cla, " tptnfpfn: ", tp, tn, fp, fn)
    return calc_mcc(tp, tn, fp, fn)

def calc_avg_mcc(mccdna, mccrna, mccdrna, mccnon):
    return (mccdna + mccrna + mccdrna + mccnon)/4

def drnaMcc(clf, xs, ys):
    pred = clf.predict(xs)
    print("finished prediction")
    drna_mcc = calc_class_mcc(ys, pred, " DRNA")
    print("drna mcc: ", drna_mcc)
    return drna_mcc

def avgMcc(clf, xs, ys):
    pred = clf.predict(xs)
    print("finished prediction")
    
    dna_mcc = calc_class_mcc(ys, pred, " DNA")
    rna_mcc = calc_class_mcc(ys, pred, " RNA")
    drna_mcc = calc_class_mcc(ys, pred, " DRNA")
    non_mcc = calc_class_mcc(ys, pred, " nonDRNA")
    
    avg_mcc = calc_avg_mcc(dna_mcc, rna_mcc, drna_mcc, non_mcc)
    print("MCCs: ", dna_mcc, rna_mcc, drna_mcc, non_mcc, avg_mcc)
    return avg_mcc

def mccScore():
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





