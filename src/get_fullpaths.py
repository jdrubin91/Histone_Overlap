__author__ = 'Jonathan Rubin'

import os

def run(TFdir,Histonedir):
    TFdict = dict()
    with open(TFdir + 'metadata.tsv') as F:
        for line in F:
            line = line.strip().split()
            if line[3] == 'optimal' and 'human' in line[18]:
                TFdict[line[18]] = TFdir + line[0] + '.bed.sorted.cut'
    
    #Used in IMR90 cell type (roadmap) where data is structure in folder for each Histone Modification            
    #Histonedict = dict()
    #for folder in os.listdir(Histonedir):
    #    if 'py' not in folder:
    #        for file1 in os.listdir(Histonedir + folder):
    #            if '.bed' in file1:
    #                Histonedict[folder] = Histonedir + folder + '/' + file1
    
    Histonedict = dict()
    with open(Histonedir + 'metadata.tsv') as F:
        for line in F:
            line = line.strip().split()
            if line[2] == 'narrowPeak':
                Histonedict[line[15]] = Histonedir + line[0] + '.bed.sorted.cut'
    
    
    return TFdict,Histonedict