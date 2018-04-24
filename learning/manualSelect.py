import csvToExamples
import numpy

fatima_121 = "D|G|L|K|RR|KR|SR|KK|TK|AS|PS|RV|TAR|HIE|LRG|LLT|CIDH920105.lag22|CIDH920105.lag24|CIDH920105.lag28|CIDH920105.lag29|BHAR880101.lag5|BHAR880101.lag11|BHAR880101.lag16|CHAM820101.lag7|CHAM820102.lag2|CHAM820102.lag6|CHAM820102.lag16|CHAM820102.lag17|CHAM820102.lag19|CHAM820102.lag24|CHAM820102.lag30|BIGC670101.lag23|CHAM810101.lag4|CHAM810101.lag30|DAYM780201.lag28|CIDH920105.lag17|CHAM820101.lag1|CHOC760101.lag1|CIDH920105.lag9|CIDH920105.lag28|CHAM820101.lag13|CHOC760101.lag6|CHOC760101.lag7|CHOC760101.lag8|CHAM810101.lag1|CHAM810101.lag3|CHAM810101.lag24|CHAM810101.lag28|DAYM780201.lag29|hydrophobicity.Group1|hydrophobicity.Group3|polarity.Group1|polarizability.Group3|charge.Group1|secondarystruct.Group1|secondarystruct.Group3|solventaccess.Group2|prop2.Tr1221|prop3.Tr1221|prop3.Tr2332|prop4.Tr1331|prop5.Tr1221|prop5.Tr1331|prop6.Tr2332|prop7.Tr1221|prop1.G2.residue0|prop2.G2.residue25|prop2.G2.residue50|prop3.G2.residue50|prop3.G3.residue50|prop4.G2.residue0|prop4.G2.residue100|prop4.G3.residue75|prop5.G1.residue25|prop6.G2.residue0|prop6.G3.residue100|VS332|VS452|VS525|VS155|VS255|VS555|VS266|Schneider.lag13|Schneider.lag18|Schneider.lag29|Grantham.lag9|Grantham.lag12|Grantham.lag18|Grantham.lag20|Grantham.lag25|Grantham.lag28|Schneider.Xr.A|Schneider.Xr.R|Schneider.Xr.D|Schneider.Xr.C|Schneider.Xr.E|Schneider.Xr.P|Grantham.Xr.E|Grantham.Xr.K|Grantham.Xr.P|Schneider.Xd.1|Schneider.Xd.6|Xc1.D|Xc1.C|Xc1.E|Xc1.H|Xc1.F|Xc2.lambda.1|Xc2.lambda.13|Pc1.R|Pc1.D|Pc1.H|Pc1.M|Pc1.S|Pc1.T|Pc1.W|Pc2.Hydrophilicity.3|Pc2.Hydrophobicity.15|Pc2.Hydrophilicity.20|Pc2.Hydrophilicity.23"

all_483 = "R|D|C|H|I|K|S|V|RR|KR|RN|DD|SQ|AG|RG|EG|GL|KL|AK|EK|GK|HK|AF|RF|HF|RP|SP|NS|PS|VS|RV|VV|KRA|SHA|ILA|MAR|HRR|QNR|IER|CHR|VLR|NKR|WQN|NTN|STN|RVN|PQC|VSE|HCQ|PQQ|DHQ|FEG|KKG|NVG|SDH|DPH|LPH|SSH|QAI|ARI|SRI|NSI|CTI|FKL|MPL|PPL|VTL|KVL|RKK|RMK|KPK|TPK|QLM|RCF|DHF|FTF|TIP|SFP|LQS|RHS|YFT|LVT|CTW|LVW|MRY|LVV|CIDH920105.lag26|BHAR880101.lag9|BHAR880101.lag12|BHAR880101.lag14|BHAR880101.lag21|BHAR880101.lag25|CHAM820101.lag5|CHAM820101.lag9|CHAM820101.lag20|CHAM820101.lag24|CHAM820102.lag3|CHAM820102.lag6|CHAM820102.lag8|CHAM820102.lag13|CHAM820102.lag14|CHAM820102.lag17|CHAM820102.lag22|CHAM820102.lag24|CHAM820102.lag25|CHAM820102.lag27|CHAM820102.lag28|CHAM820102.lag29|CHOC760101.lag2|CHOC760101.lag10|BIGC670101.lag1|BIGC670101.lag10|BIGC670101.lag24|BIGC670101.lag28|CHAM810101.lag6|CHAM810101.lag13|CHAM810101.lag16|CHAM810101.lag18|CIDH920105.lag1|CIDH920105.lag19|CIDH920105.lag30|BHAR880101.lag2|BHAR880101.lag5|BHAR880101.lag8|BHAR880101.lag25|BHAR880101.lag30|CHAM820101.lag5|CHAM820101.lag6|CHAM820101.lag10|CHAM820101.lag26|CHAM820102.lag7|CHAM820102.lag8|CHOC760101.lag7|CHOC760101.lag17|BIGC670101.lag2|BIGC670101.lag27|CHAM810101.lag2|CHAM810101.lag3|CHAM810101.lag7|CHAM810101.lag13|DAYM780201.lag11|DAYM780201.lag12|DAYM780201.lag15|CIDH920105.lag26|BHAR880101.lag15|BHAR880101.lag27|CHAM820101.lag7|CHAM820101.lag25|CHAM820101.lag30|CHAM820102.lag2|CHOC760101.lag15|CHOC760101.lag24|BIGC670101.lag7|BIGC670101.lag9|BIGC670101.lag13|BIGC670101.lag22|BIGC670101.lag29|CHAM810101.lag2|CHAM810101.lag25|DAYM780201.lag19|DAYM780201.lag21|DAYM780201.lag28|polarity.Group1|polarity.Group3|polarizability.Group3|charge.Group1|charge.Group2|charge.Group3|solventaccess.Group1|prop1.Tr2332|prop2.Tr2332|prop3.Tr1221|prop4.Tr1221|prop4.Tr1331|prop5.Tr1221|prop5.Tr2332|prop6.Tr2332|prop7.Tr1221|prop1.G2.residue75|prop2.G1.residue25|prop4.G2.residue0|prop4.G3.residue50|prop5.G2.residue50|prop5.G3.residue0|prop5.G3.residue50|prop6.G2.residue50|prop6.G2.residue100|prop6.G3.residue75|prop7.G1.residue50|VS321|VS151|VS651|VS352|VS414|VS644|VS454|VS315|VS325|VS535|VS145|VS155|VS255|VS265|VS567|Schneider.lag3|Schneider.lag6|Schneider.lag9|Schneider.lag12|Grantham.lag5|Grantham.lag13|Grantham.lag15|Grantham.lag19|Schneider.Xr.R|Schneider.Xr.I|Schneider.Xr.S|Schneider.Xr.V|Grantham.Xr.V|Schneider.Xd.8|Schneider.Xd.16|Schneider.Xd.24|Grantham.Xd.4|Grantham.Xd.7|Grantham.Xd.14|Grantham.Xd.30|Xc1.R|Xc1.F|Xc1.W|Xc1.Y|Xc2.lambda.1|Xc2.lambda.11|Xc2.lambda.12|Xc2.lambda.13|Xc2.lambda.17|Xc2.lambda.21|Xc2.lambda.24|Xc2.lambda.30|Pc1.R|Pc1.D|Pc1.Q|Pc1.I|Pc1.P|Pc2.Hydrophilicity.7|Pc2.Hydrophilicity.16|Pc2.Hydrophilicity.20| Gw(U)_NO_ARG_N1|Gw(U)_NO_ARG_MI50|Gw(U)_NO_GLN_MI50|Gw(U)_NO_LYS_N1|Gw(U)_NO_AHR_N1|Gw(U)_NO_AHR_P2|Gw(U)_NO_ARM_N1|Gw(U)_NO_PCR_N1|Gw(U)_NO_PRT_N1|Gw(U)_NO_PRT_P2|Gw(U)_NO_PRT_DE|Gw(U)_NO_PRT_MI50|Gs(U)_NO_ALA_N1|Gs(U)_NO_ARG_N1|Gs(U)_NO_GLU_N1|Gs(U)_NO_SER_N1|Gs(U)_NO_NPR_P2|Gs(U)_NO_NPR_DE|Gs(U)_NO_PCR_N1|Gs(U)_NO_PRT_P2|Gs(U)_NO_PRT_DE|Mw_NO_NPR_N1|Mw_NO_PCR_N1|Mw_NO_PCR_DE|HP_NO_GLU_N1|HP_NO_AHR_P2|HP_NO_PCR_N1|HP_NO_PRT_DE|Z1_NO_ARG_N1|Z1_NO_GLU_N1|Z1_NO_LEU_N1|Z1_NO_PCR_N1|Z1_NO_PCR_DE|Z1_NO_PRT_MI50|Pa_NO_ARM_N1|[G3.1.1.1.19]|[G3.1.1.1.25]|[G3.1.1.1.29]|[G3.1.2.1.8]|[G3.1.2.1.10]|[G3.1.4.1.3]|[G3.1.4.1.12]|[G3.1.4.1.15]|[G3.2.1.1.6]|[G3.2.1.1.12]|[G3.2.2.1.7]|[G3.2.4.1.28]|[G3.3.1.1.15]|[G3.3.1.1.18]|[G3.3.1.1.23]|[G3.3.2.1.18]|[G3.3.2.1.22]|[G3.3.4.1.17]|[G4.1.1.1]|[G4.1.1.3]|[G4.1.2.2]|[G4.1.2.3]|[G4.1.3.1]|[G4.1.3.3]|[G4.1.5.1]|[G4.1.5.3]|[G4.1.6.1]|[G4.1.7.1]|[G4.1.9.3]|[G4.1.10.1]|[G4.1.11.1]|[G4.1.11.2]|[G4.1.13.1]|[G4.1.14.1]|[G4.1.14.2]|[G4.1.14.3]|[G4.1.16.1]|[G4.1.17.1]|[G4.1.17.3]|[G4.1.18.1]|[G4.1.19.1]|[G4.1.19.3]|[G4.1.20.1]|[G4.1.21.1]|[G4.1.21.2]|[G4.1.23.1]|[G4.1.23.3]|[G4.1.24.3]|[G4.2.1.2]|[G4.2.1.3]|[G4.2.3.1]|[G4.2.3.2]|[G4.2.3.3]|[G4.2.5.1]|[G4.2.5.3]|[G4.2.8.3]|[G4.2.10.2]|[G4.2.10.3]|[G4.2.11.2]|[G4.2.11.3]|[G4.2.13.3]|[G4.2.14.1]|[G4.2.16.3]|[G4.2.17.2]|[G4.2.19.2]|[G4.2.21.1]|[G4.2.22.1]|[G4.2.23.2]|[G4.2.23.3]|[G4.3.1.15]|[G4.3.2.9]|[G4.3.3.1]|[G4.3.3.2]|[G4.3.3.3]|[G4.3.3.11]|[G4.3.3.12]|[G4.3.4.10]|[G4.3.5.9]|[G4.3.5.11]|[G4.3.5.13]|[G4.3.6.4]|[G4.3.6.12]|[G4.3.7.6]|[G4.3.7.9]|[G4.3.8.4]|[G4.3.8.12]|[G4.3.9.4]|[G4.3.9.6]|[G4.3.9.8]|[G4.3.9.10]|[G4.3.9.13]|[G4.3.10.3]|[G4.3.10.9]|[G4.3.10.12]|[G4.3.13.5]|[G4.3.13.6]|[G4.3.13.7]|[G4.3.13.12]|[G4.3.13.15]|[G4.3.14.7]|[G4.3.14.10]|[G4.3.14.15]|[G4.3.15.11]|[G4.3.16.4]|[G4.3.16.10]|[G4.3.17.1]|[G4.3.17.5]|[G4.3.17.9]|[G4.3.18.5]|[G4.3.19.1]|[G4.3.19.3]|[G4.3.19.4]|[G4.3.19.6]|[G4.3.19.12]|[G4.3.20.6]|[G4.3.20.9]|[G4.3.20.12]|[G4.3.22.6]|[G4.3.23.2]|[G4.3.23.7]|[G4.3.23.10]|[G4.3.24.1]|[G5.1.1.12]|[G5.1.1.13]|[G5.1.1.16]|[G5.1.1.18]|[G5.1.1.22]|[G5.1.1.23]|[G5.1.1.24]|[G5.1.1.27]|[G5.1.1.29]|[G5.1.1.30]|[G5.1.2.1]|[G5.1.2.9]|[G5.1.2.10]|[G5.1.2.15]|[G5.1.2.32]|[G5.1.2.44]|[G5.2.1.7]|[G5.2.1.15]|[G5.2.1.18]|[G5.2.1.21]|[G5.2.1.24]|[G5.2.1.27]|[G5.2.2.2]|[G5.2.2.14]|[G5.2.2.16]|[G5.2.2.20]|[G5.2.2.36]|[G7.1.1.4]|[G7.1.1.12]|[G7.1.1.19]|[G7.1.1.44]|[G7.1.1.50]|[G7.1.1.66]|[G7.1.1.68]|[G7.1.1.70]|[G7.1.1.79]|[G9.1]"
all_131 = "R|V|RR|RG|KL|GK|SP|PS|RV|LPH|LVT|BHAR880101.lag9|BHAR880101.lag14|BHAR880101.lag25|CHAM820101.lag5|CHAM820102.lag3|CHAM820102.lag13|CHAM820102.lag25|CHAM810101.lag6|CHAM810101.lag16|BHAR880101.lag25|CHAM820102.lag7|DAYM780201.lag11|BIGC670101.lag13|polarity.Group1|polarity.Group3|polarizability.Group3|charge.Group1|charge.Group2|charge.Group3|solventaccess.Group1|prop1.Tr2332|prop3.Tr1221|prop5.Tr1221|prop5.Tr2332|prop7.Tr1221|prop1.G2.residue75|prop2.G1.residue25|prop4.G2.residue0|prop6.G3.residue75|VS151|VS315|VS255|VS567|Grantham.lag5|Grantham.lag13|Grantham.lag15|Grantham.lag19|Schneider.Xr.R|Schneider.Xr.I|Grantham.Xr.V|Grantham.Xd.4|Grantham.Xd.30|Xc1.R|Xc1.F|Xc1.Y|Xc2.lambda.1|Xc2.lambda.11|Pc1.D|Pc1.I|Gw(U)_NO_ARG_MI50|Gw(U)_NO_GLN_MI50|Gw(U)_NO_AHR_P2|Gw(U)_NO_PCR_N1|Gw(U)_NO_PRT_N1|Gw(U)_NO_PRT_P2|Gw(U)_NO_PRT_DE|Gs(U)_NO_ARG_N1|Gs(U)_NO_SER_N1|Gs(U)_NO_PRT_P2|Mw_NO_NPR_N1|Mw_NO_PCR_N1|HP_NO_GLU_N1|HP_NO_AHR_P2|HP_NO_PCR_N1|Z1_NO_PCR_DE|[G3.3.1.1.15]|[G3.3.1.1.23]|[G4.1.1.1]|[G4.1.1.3]|[G4.1.2.3]|[G4.1.3.1]|[G4.1.3.3]|[G4.1.5.1]|[G4.1.6.1]|[G4.1.7.1]|[G4.1.11.1]|[G4.1.11.2]|[G4.1.13.1]|[G4.1.14.3]|[G4.1.17.1]|[G4.1.18.1]|[G4.1.19.1]|[G4.1.19.3]|[G4.1.20.1]|[G4.1.21.1]|[G4.1.21.2]|[G4.1.23.3]|[G4.2.3.1]|[G4.2.5.1]|[G4.2.5.3]|[G4.2.8.3]|[G4.2.11.3]|[G4.2.13.3]|[G4.2.21.1]|[G4.2.23.3]|[G4.3.3.1]|[G4.3.6.4]|[G4.3.9.10]|[G4.3.13.5]|[G4.3.13.6]|[G4.3.13.15]|[G4.3.17.5]|[G4.3.17.9]|[G4.3.19.3]|[G4.3.19.12]|[G4.3.20.9]|[G4.3.20.12]|[G5.1.1.13]|[G5.1.1.16]|[G5.1.1.22]|[G5.1.1.24]|[G5.1.1.27]|[G5.1.2.9]|[G5.1.2.15]|[G5.2.1.15]|[G5.2.1.21]|[G5.2.1.27]|[G5.2.2.2]|[G7.1.1.19]|[G9.1]"
feature_string = all_131

feature_file = './features/pred-fa_feat_ProtrWeb.csv'
feature_file = './training_data/all_features.csv'

def reduce(xs):
    
    feature_labels = csvToExamples.feature_list(feature_file)[:-1]
    features = feature_string.split("|")
    non_feature_indexes = []
    feature_indexes = []
    selected_features_test = []
    for f in features:
        index = feature_labels.index(f)
        if (index >=0):
            feature_indexes.append(index)
    for i in range(len(feature_labels)):
        if i not in feature_indexes:
            non_feature_indexes.append(i)
    # for i in range(len(feature_labels)):
    #     if feature_labels[i] in features:
    #         selected_features_test.append(feature_labels[i])
    #         feature_indexes.append(i)
    #     else:
    #         non_feature_indexes.append(i)
    # for i in range(len(features)):
    #     print(i, features[i], selected_features_test[i])
        
    
    
    reduced = numpy.delete(xs, non_feature_indexes, 1)   

    # new_xs = []
    # counter = 0
    # for x in xs:
    #     counter +=1 
    #     print(counter)
    #     new_x = []
    #     for i in range(len(x)):
    #         if i in feature_indexes:
    #             new_xs.append(x[i])
    
    # reduced = numpy.array(new_xs)
    print("reduced shape: ", reduced.shape, len(features), len(feature_indexes), len(non_feature_indexes), len(feature_labels))
    return reduced

