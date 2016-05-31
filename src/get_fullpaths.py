__author__ = 'Jonathan Rubin'

import os

def run(TFdir,Histonedir):
    TFdict = dict()
    with open(TFdir + 'metadata.tsv') as F:
        for line in F:
            line = line.strip().split()
            if line[1] is 'bed' and line[3] is 'peaks' and 'control' not in line[-3]:
                TFdict[line[-3]] = TFdir + line[0] + '.sorted.cut'
                
    Histonedict = dict()
    for folder in os.listdir(Histonedir):
        if 'py' not in folder:
            for file1 in os.listdir(Histonedir + folder):
                if '.bed' in file1:
                    Histonedict[folder] = Histonedir + folder + '/' + file1
    
    return TFdict,Histonedict