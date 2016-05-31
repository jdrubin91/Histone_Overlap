__author__ = 'Jonathan Rubin'

import os

def run(Bidirdir, Genedir, files):
    os.system("bedtools intersect -c -a " + Bidirdir + " -b " + Genedir + " > " + files + "Bidir_intersect.bed")
    
    TSS = list()
    Enhancer = list()
    with open(files + "Bidir_intersect.bed") as F:
        for line in F:
            if line.strip().split()[-1] == '0':
                Enhancer.append(line)
            else:
                TSS.append(line)
    
    outfile1 = open(files + "Enhancer_Bidir.bed",'w')
    for line in Enhancer:
        outfile1.write(line)
    outfile1.close()
    
    outfile2 = open(files + "TSS_Bidir.bed",'w')
    for line in TSS:
        outfile2.write(line)
    outfile2.close()
    