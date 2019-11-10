import pandas as pd
import numpy as np
import sys
#import seaborn as sns
#import matplotlib.pyplot as plt
#get_ipython().magic(u'matplotlib inline')
sys.maxsize=5000000
print('Valor sys.maxsize', sys.maxsize)

#se espera una lista de archivos .dat que se llamen nombre_valordeRo.dat, todos en un mismo directorio
def sacarRo(nombreArchivo):
    return float(nombreArchivo.rstrip('.dat').split('_')[-1])

import os
def lista_de_archivos(mypath):
    lista_archivos=[file for file in os.listdir(mypath) if file.endswith('.dat')]
    return lista_archivos

#indicar el path donde estan los archivos .dat
Ro_list=[]
names_list=[]
for x in lista_de_archivos('.'): 
    Ro_list.append(sacarRo(x))
    names_list.append(x)
print('Lista de valores de Ro:',sorted(Ro_list))

sorted(names_list)

def procesarArchivo(nombreArchivo, K=100, n_bins=100,Ro=10.8,range_h=(10.5,11.05)):
    ventana=pd.read_csv(nombreArchivo, delim_whitespace=True, header=None, names=['frame', 'r'])
    ventana=ventana.set_index('frame')
    ventana=ventana['r']
    freqs, bins = np.histogram(ventana, bins=n_bins,normed=True,range=range_h)

    Ro = sacarRo(nombreArchivo)
    n_zero = freqs.nonzero() #posiciones donde no es 0 el freqs
    bins_m = (bins[1:]+bins[:-1] )/2 
    histo=np.column_stack((bins_m,freqs))
    np.savetxt('histo_'+str(Ro)+'.hist',histo,fmt=('%4.3f'),delimiter=' ')
    
    free_en=-0.6*np.log(freqs[n_zero])-K*(bins_m[n_zero]-Ro)**2
    FEvsR=np.column_stack((bins_m[n_zero],free_en))
     
    np.savetxt('free_en_'+str(Ro)+'.en',FEvsR,fmt=('%4.3f'),delimiter=' ')
    print('Procesando:',nombreArchivo)
    #plt.plot(bins_m,freqs)
    #plt.plot(bins_m[n_zero],free_en)
    return free_en

#en n_bins cambias el nro de bins y en range_h podes cambiar el rango del histograma, ahora esta Ro-0.5 a Ro+0.5
for x in range(len(names_list)):
    procesarArchivo(names_list[x],K=100, n_bins=50,Ro=Ro_list[x],range_h=(Ro_list[x]-0.5,Ro_list[x]+0.5))




