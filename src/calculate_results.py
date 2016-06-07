__author__ = 'Jonathan Rubin'

import os

def run(TFdict,Histonedict,Bidirdir,Genedir,files):
    results = dict()    
    overlap = list()
    for TF in TFdict:
        print TF
        TFdir = TFdict[TF]
        os.system("bedtools intersect -c -a " + TFdir + " -b " + Bidirdir + " > " + files + "TF_bidir_intersect.bed")
        pos = list()
        neg = list()
        with open(files + "TF_bidir_intersect.bed") as F:
            for line in F:
                if line.strip().split()[-1] == '0':
                    neg.append(line)
                else:
                    pos.append(line)
        overlap.append(float(len(pos))/float(len(pos)+len(neg)))
        outfile1 = open(files + "TF_posbidir_intersect.bed",'w')
        for line in pos:
            outfile1.write(line)
        outfile1.close()
        outfile2 = open(files + "TF_negbidir_intersect.bed",'w')
        for line in neg:
            outfile2.write(line)
        outfile2.close()
        
        
        os.system("bedtools intersect -c -a " + files + "TF_posbidir_intersect.bed -b " + Genedir + " > " + files + "TF_posbidir_gene_intersect.bed")
        TSS = list()
        Enhancer = list()
        with open(files + "TF_posbidir_gene_intersect.bed") as F:
            for line in F:
                if line.strip().split()[-1] == '0':
                    TSS.append(line)
                else:
                    Enhancer.append(line)
        outfile1 = open(files + "TF_posbidir_TSS_intersect.bed",'w')
        for line in TSS:
            outfile1.write(line)
        outfile1.close()
        outfile2 = open(files + "TF_posbidir_Enhancer_intersect.bed",'w')
        for line in Enhancer:
            outfile2.write(line)
        outfile2.close()
        
        
        os.system("bedtools intersect -c -a " + files + "TF_negbidir_intersect.bed -b " + Genedir + " > " + files + "TF_negbidir_gene_intersect.bed")
        TSS = list()
        Enhancer = list()
        with open(files + "TF_negbidir_gene_intersect.bed") as F:
            for line in F:
                if line.strip().split()[-1] == '0':
                    TSS.append(line)
                else:
                    Enhancer.append(line)
        outfile1 = open(files + "TF_negbidir_TSS_intersect.bed",'w')
        for line in TSS:
            outfile1.write(line)
        outfile1.close()
        outfile2 = open(files + "TF_negbidir_Enhancer_intersect.bed",'w')
        for line in Enhancer:
            outfile2.write(line)
        outfile2.close()
        
        
        for mod in Histonedict:
            print mod
            if mod not in results:
                results[mod] = list()
            os.system("bedtools intersect -c -a " + files + "TF_posbidir_TSS_intersect.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_Enhancer_bidir_intersect_pos.bed")
            os.system("bedtools intersect -c -a " + files + "TF_posbidir_Enhancer_intersect.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_Enhancer_bidir_intersect_neg.bed")
            os.system("bedtools intersect -c -a " + files + "TF_negbidir_TSS_intersect.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_TSS_bidir_intersect_pos.bed")
            os.system("bedtools intersect -c -a " + files + "TF_negbidir_Enhancer_intersect.bed" + " -b " + Histonedict[mod] + " > " + files + "Histone_TF_TSS_bidir_intersect_neg.bed")
            
            filelist = ["Histone_TF_Enhancer_bidir_intersect_pos.bed","Histone_TF_Enhancer_bidir_intersect_neg.bed","Histone_TF_TSS_bidir_intersect_pos.bed","Histone_TF_TSS_bidir_intersect_neg.bed"]
            resultlist = [TF]
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
                if total == 0:
                    resultlist.append(0)
                else:
                    resultlist.append(pos/total)
            results[mod].append(resultlist)
            
    outfile3 = open(files+'results.txt','w')
    for key in results:
        outfile3.write("#" + key + "\n")
        for item in results[key]:
            for val in item:
                outfile3.write(str(val) + '\t')
    for item in overlap:
        outfile3.write(str(item) + ',')
        
        
    return results
        
    
def run2(TFdict,Histonedict,Bidirdir,Genedir,files):
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
            resultlist = list()
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
                resultlist.append(pos/total)
            results[mod].append(resultlist)
    
    outfile3 = open(files+'results.txt','w')
    for key in results:
        outfile3.write("{'")
        outfile3.write(key + "': [")
        for item in results[key]:
            outfile3.write("[")
    
    return results