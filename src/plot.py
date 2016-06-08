__author__ = 'Jonathan Rubin'

import matplotlib
matplotlib.use('Agg')
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt

def run(files):
    resultpath = files + 'results.txt'
    results = dict()
    mod = 'none'
    with open(resultpath) as F:
        for line in F:
            line = line.strip()
            if '#' in line[0]:
                mod = line[1:]
                results[mod] = list()
            else:
                line = line.split()                    
                results[mod].append([line[0],float(line[1]),float(line[2]),float(line[3]),float(line[4])])
    for mod in results:
        list1 = [[],[],[],[]]
        for items in results[mod]:
            TF = items[0]
            list1[0].append(items[1])
            list1[1].append(items[2])
            list1[2].append(items[3])
            list1[3].append(items[4])
            
            
        F = plt.figure()
        ax1 = F.add_subplot(1,1,1)
        bp1 = ax1.boxplot(list1,patch_artist=True)
        ax1.set_xticklabels(["TSS;+B","Enhancer;+B","TSS;-B","Enahncer;-B"],rotation = 45, fontsize=8)
        ax1.get_xaxis().tick_bottom()
        ax1.get_yaxis().tick_left()
        ## change outline color, fill color and linewidth of the boxes
        for box in bp1['boxes']:
            # change outline color
            box.set( color='#7570b3', linewidth=2)
            # change fill color
            box.set( facecolor = '#1b9e77' )
        ## change color and linewidth of the whiskers
        for whisker in bp1['whiskers']:
            whisker.set(color='#7570b3', linewidth=2)
        ## change color and linewidth of the caps
        for cap in bp1['caps']:
            cap.set(color='#7570b3', linewidth=2)
        ## change color and linewidth of the medians
        for median in bp1['medians']:
            median.set(color='#b2df8a', linewidth=2)
        ## change the style of fliers and their fill
        for flier in bp1['fliers']:
            flier.set(marker='o', color='#e7298a', alpha=0.5)
        
        #plt.savefig(directory + '/' + cell + '/' + cell + '_overlap_boxplot1.png')
        plt.savefig(files + mod + '_overlaps.png')