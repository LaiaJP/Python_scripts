import pandas as pd
import numpy as np
import sys

# Iteration over all arguments:
sys.argv.remove('histogram.py')
for eachArg in sys.argv:
     ventana=pd.read_csv(eachArg, delim_whitespace=True, header=0, names=['frame', 'dis'])
     ventana=ventana.set_index('frame')
     ventana=ventana['dis']
     freqs, bins = np.histogram(ventana, bins=50, range=[2,6], normed=True)
     bins_m = (bins[1:]+bins[:-1] )/2
     histo=np.column_stack((bins_m,freqs))
     nom_arxiu=eachArg.rstrip('.dat')
     np.savetxt('histo_'+nom_arxiu+'.hist',histo,delimiter=' ')

