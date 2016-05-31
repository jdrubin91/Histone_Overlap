__author__ = 'Jonathan Rubin'

import os
import get_fullpaths
import separate_bidir

#User Input
#############################################################################
TFdir = '/scratch/Shares/dowell/ENCODE/SVM/IMR90/TF_ChIP-Seq/'
Histonedir = '/scratch/Shares/dowell/ENCODE/SVM/IMR90/histone_mods/'
Bidirdir = '/scratch/Shares/dowell/EMG_out_files/human/SRR639050-1_divergent_classifications.bed'
Genedir = '/scratch/Users/joru1876/hg19_reference_files/refFlat_hg19.bed'
#############################################################################


#Return parent directory
def parent_dir(directory):
    pathlist = directory.split('/')
    newdir = '/'.join(pathlist[0:len(pathlist)-1])
    
    return newdir

#Home directory
homedir = os.path.dirname(os.path.realpath(__file__))

#Files directory
files = parent_dir(homedir) + '/files/'

#Requires the following modules:
#module load bedtools2_2.22.0

def run():
    TFdict,Histonedict = get_fullpaths.run(TFdir,Histonedir)
    separate_bidir.run(Bidirdir, Genedir, files)
    print Histonedict,TFdict