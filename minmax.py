#!python

import sys
import pandas as pd
import numpy as np

# Iteration over all arguments:
sys.argv.remove('minmax.py')

dis = []
dihe = []

for eachArg in sys.argv:
        eachArg_list = []
        with open(eachArg, 'r') as infile:
            file = [list(map(float, i.split(' '))) for i in infile]            
        data = np.array(file)
        [a,b,c] = np.amin(data, axis=0)
        dis.append(b)
        dihe.append(c)
        [a,b,c] = np.amax(data, axis=0)
        dis.append(b)
        dihe.append(c)

#print(dis,dihe)     
#min_dis = min(dis)
#max_dis = max(dis)
#min_dihe = min(dihe)
#max_dihe = max(dihe)              
#
#print('Min dis: ',min_dis)
#print('Max dis: ',max_dis)
#print('Min dihe: ',min_dihe)
#print('Min dihe: ',max_dihe)

f=open("minmax.txt", "a")
print >> f, min(dis), max(dis), min(dihe), max(dihe)
f.close()

