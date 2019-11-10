#!python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

plt.rcParams["font.family"] = "freeserif"

## Iteration over all arguments:
#sys.argv.remove('proba.py')
#for eachArg in sys.argv:
#        eachArg_list = []
#        with open(eachArg, 'r') as infile:
#            for line in infile:
#                eachArg_list.extend(line.strip().split(' '))
#            eachArg_list.pop(0)
#            eachArg_list.pop(-1)
#            print(eachArg_list)

labels = ['1', '2', '3', '4','5','6','7','8']
fe2_5c_wt=[8,4,3,1,0,0, 0, 0]
fe2_5c_wt_LysH=[40,11,9,6,4,4,7,9]
fe2_5c_K49A_Lys=[23,12,10,3,1,0,0,0]
fe2_5c_K49A_LysH=[12,7,21,23,12,6,6,7]
fe2_5c_R52A_Lys=[3,0,0,0, 0, 0, 0, 0]
fe2_5c_R52A_LysH=[37,0,0,0,2,5,12,19]
fe2_5c_K49AR52A_Lys=[28,22,10,2,2,1,2,2]
fe2_5c_K49AR52A_LysH=[58,0,0,0,0,1,5,13]

x = np.arange(len(labels))  # the label locations
width = 0.11  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width*4, fe2_5c_wt, width, label='Wt 5c Lys', color='crimson')
rects2 = ax.bar(x - width*3, fe2_5c_wt_LysH, width, label='Wt 5c LysH',color='orange')
rects3 = ax.bar(x - width*2, fe2_5c_K49A_Lys, width, label='K49A 5c Lys',color='magenta')
rects4 = ax.bar(x - width, fe2_5c_K49A_LysH, width, label='K49A 5c LysH',color='darkorchid')
rects5 = ax.bar(x, fe2_5c_R52A_Lys, width, label='R52A 5c Lys',color='cyan')
rects6 = ax.bar(x + width, fe2_5c_R52A_LysH, width, label='R52A 5c LysH',color='teal')
rects7 = ax.bar(x + width*2, fe2_5c_K49AR52A_Lys, width, label='K49A/R52A 5c Lys',color='lime')
rects8 = ax.bar(x + width*3, fe2_5c_K49AR52A_LysH, width, label='K49A/R52A 5c LysH',color='yellow')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Number of water molecules')
#ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = int(rect.get_height())
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() /2 , height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)
autolabel(rects7)
autolabel(rects8)

fig.tight_layout()

plt.figure(figsize=(12, 9))

plt.savefig('wat_%.svg')

plt.show()


