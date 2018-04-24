import csvToExamples

fatima_121 = "D|G|L|K|RR|KR|SR|KK|TK|AS|PS|RV|TAR|HIE|LRG|LLT|CIDH920105.lag22|CIDH920105.lag24|CIDH920105.lag28|CIDH920105.lag29|BHAR880101.lag5|BHAR880101.lag11|BHAR880101.lag16|CHAM820101.lag7|CHAM820102.lag2|CHAM820102.lag6|CHAM820102.lag16|CHAM820102.lag17|CHAM820102.lag19|CHAM820102.lag24|CHAM820102.lag30|BIGC670101.lag23|CHAM810101.lag4|CHAM810101.lag30|DAYM780201.lag28|CIDH920105.lag17|CHAM820101.lag1|CHOC760101.lag1|CIDH920105.lag9|CIDH920105.lag28|CHAM820101.lag13|CHOC760101.lag6|CHOC760101.lag7|CHOC760101.lag8|CHAM810101.lag1|CHAM810101.lag3|CHAM810101.lag24|CHAM810101.lag28|DAYM780201.lag29|hydrophobicity.Group1|hydrophobicity.Group3|polarity.Group1|polarizability.Group3|charge.Group1|secondarystruct.Group1|secondarystruct.Group3|solventaccess.Group2|prop2.Tr1221|prop3.Tr1221|prop3.Tr2332|prop4.Tr1331|prop5.Tr1221|prop5.Tr1331|prop6.Tr2332|prop7.Tr1221|prop1.G2.residue0|prop2.G2.residue25|prop2.G2.residue50|prop3.G2.residue50|prop3.G3.residue50|prop4.G2.residue0|prop4.G2.residue100|prop4.G3.residue75|prop5.G1.residue25|prop6.G2.residue0|prop6.G3.residue100|VS332|VS452|VS525|VS155|VS255|VS555|VS266|Schneider.lag13|Schneider.lag18|Schneider.lag29|Grantham.lag9|Grantham.lag12|Grantham.lag18|Grantham.lag20|Grantham.lag25|Grantham.lag28|Schneider.Xr.A|Schneider.Xr.R|Schneider.Xr.D|Schneider.Xr.C|Schneider.Xr.E|Schneider.Xr.P|Grantham.Xr.E|Grantham.Xr.K|Grantham.Xr.P|Schneider.Xd.1|Schneider.Xd.6|Xc1.D|Xc1.C|Xc1.E|Xc1.H|Xc1.F|Xc2.lambda.1|Xc2.lambda.13|Pc1.R|Pc1.D|Pc1.H|Pc1.M|Pc1.S|Pc1.T|Pc1.W|Pc2.Hydrophilicity.3|Pc2.Hydrophobicity.15|Pc2.Hydrophilicity.20|Pc2.Hydrophilicity.23"

feature_file = './features/pred-fa_feat_ProtrWeb.csv'


def reduce(xs, feature_string):
    feature_labels = csvToExamples.feature_list(feature_file)
    features = feature_string.split("|")
    feature_indexes = []
    for i in range(len(feature_labels)):
        if features[i] in feature_labels:
            feature_indexes.push[i]
    


