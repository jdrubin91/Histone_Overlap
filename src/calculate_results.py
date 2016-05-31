__author__ = 'Jonathan Rubin'

import os

def run(TFdict,Histonedict,files):
    Enhancer = files + "Enhancer_Bidir.bed"
    TSS = files + "TSS_Bidir.bed"
    results = dict()
    
    for TF in TFdict:
        os.system("bedtools intersect -c -a " + TFdict[TF] + " -b " + Enhancer + " > " + files + "TF_Enhancer_bidir_intersect.bed")
        pos = list()
        neg = list()
        with open(files + "TF_Enhancer_bidir_intersect.bed") as F:
            for line in F:
                if line.strip().split()[-1] == '0':
                    neg.append(line)
                else:
                    pos.append(line)
        outfile1 = open(files + "TF_Enhancer_bidir_intersect_pos.bed",'w')
        for line in pos:
            outfile1.write(line)
        outfile1.close()
        outfile2 = open(files + "TF_Enhancer_bidir_intersect_neg.bed",'w')
        for line in neg:
            outfile2.write(line)
        outfile2.close()
        
        
        os.system("bedtools intersect -c -a " + TFdict[TF] + " -b " + TSS + " > " + files + "TF_TSS_bidir_intersect.bed")
        pos = list()
        neg = list()
        with open(files + "TF_TSS_bidir_intersect.bed") as F:
            for line in F:
                if line.strip().split()[-1] == '0':
                    neg.append(line)
                else:
                    pos.append(line)
        outfile1 = open(files + "TF_TSS_bidir_intersect_pos.bed",'w')
        for line in pos:
            outfile1.write(line)
        outfile1.close()
        outfile2 = open(files + "TF_TSS_bidir_intersect_neg.bed",'w')
        for line in neg:
            outfile2.write(line)
        outfile2.close()
        
        for mod in Histonedict:
            if mod not in results:
                results[mod] = list()
            os.system("bedtools intersect -c -a " + files + "TF_Enhancer_bidir_intersect_pos.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_Enhancer_bidir_intersect_pos.bed")
            os.system("bedtools intersect -c -a " + files + "TF_Enhancer_bidir_intersect_neg.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_Enhancer_bidir_intersect_neg.bed")
            os.system("bedtools intersect -c -a " + files + "TF_TSS_bidir_intersect_pos.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_TSS_bidir_intersect_pos.bed")
            os.system("bedtools intersect -c -a " + files + "TF_TSS_bidir_intersect_neg.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_TSS_bidir_intersect_neg.bed")
            
            filelist = ["Histone_TF_Enhancer_bidir_intersect_pos.bed","Histone_TF_Enhancer_bidir_intersect_neg.bed","Histone_TF_TSS_bidir_intersect_pos.bed","Histone_TF_TSS_bidir_intersect_neg.bed"]
            for filename in filelist:
                filename = files + filename
                total = 0
                pos = 0
                with open(filename) as F:
                    for line in F:
                        if line.strip().split()[-1] == '0':
                            total += 1.0
                        else:
                            pos += 1.0
                            total += 1.0
                results[mod].append(pos/total)
                
    return results