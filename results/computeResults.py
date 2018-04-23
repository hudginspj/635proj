import math

def calc_sensitivity(tp, fn):
    return 100*tp / (tp + fn)

def calc_specificity(tn, fp):
    return 100*tn / (tn + fp)

def calc_predictive_acc(tp, tn, fp, fn):
    return 100* (tp+tn) / (tp+fp+tn+fn)

def calc_mcc(tp, tn, fp, fn):
    s1 = (tp+fp)
    s2 = (tp+fn)
    s3 = (tn+fp)
    s4 = (tn+fn)
    #print('s1: {} - s2: {} - s3: {} - s4: {}'.format(s1, s2, s3, s4))
    prd = s1 * s2 * s3 * s4
    print('s1: {} - s2: {} - s3: {} - s4: {} - prd {}'.format(s1, s2, s3, s4, prd))
    if (prd == 0):
        return 0

    sq = math.sqrt(prd)
    #print('sq: {}'.format(sq))
    return (tp*tn - fp*fn) / sq

def calc_avg_mcc(mccdna, mccrna, mccdrna, mccnon):
    return (mccdna + mccrna + mccdrna + mccnon)/4

