#!/usr/bin/env python
from sys import argv
from math import sqrt

def readFile(ifilename):
    ifile = open(ifilename)

    listedfile = (line.split() for line in ifile) #hace una gran lista del ifile de a un renglon
    lista = [j for i in listedfile for j in i] #truco cool que hace de una lista de listas una sola lista
    ast = [i for i,val in enumerate(lista) if val=='****'] + [len(lista)]#encuentra donde estan los * y le agrega el final
    prevectores = ( lista[x+2:y] for x,y in zip(ast,ast[1:]) )  #arma la lista de vectores, o sea, los valores entre la posicion x+2 e y-1 en la 1ra pos deberia estar el autovalor
    vectores = [ map(float, v) for v in prevectores] #los pasa a float
    return vectores

def norm(x,y,z):
    return sqrt(x**2+y**2+z**2)

def norm2(l):
    return sqrt(sum([x**2 for x in l]))    

def normas(v):
    return [norm(v[i], v[i+1],v[i+2]) for i in range(1,len(v),3)] 
    
def promed4(l):
    return [sum(l[4*i:4*(i+1)])/4 for i in range(len(l)/4)]
    
def sumautov(vectores):
    return sum([v[0] for v in vectores])    
vect = readFile(argv[1])

#ofile = open(argv[1]+'.out','w')
#for v in vect:
#    ofile.write('autovalor: ' + "{0:10.6f}".format(v[0]) + ' componentes x,y,z:\n')
#    for i in range(1,len(v),3):
#        ofile.write('('+"{0:10.6f}".format(v[i])+','+"{0:10.6f}".format(v[i+1])+','+"{0:10.6f}".format(v[i+2])+ ')\n')
#    ofile.write('\n')

#ofile2 = open(argv[1]+'.prj','w')
#para recorrer los vectores entonces 

    
v = vect[0]

ofile = open(argv[1]+'.prj','w')
ofile2 = open(argv[1]+'.out','w')

norms = normas(v)
pmd = promed4(norms)

for i,v in enumerate(vect):
    ofile2.write(str(i+1) + "{0:10.6f}".format(100*v[0]/sumautov(vect))+'\n')

for i,x in enumerate(pmd):
    ofile.write(str(i+1) + "{0:10.6f}".format(x) +'\n')

ofile.close()
#    v[0] #es el autovalor
#    for i in range(1,len(v),3):
#        print (v[i], v[i+1],v[i+2]) , norm(v[i], v[i+1],v[i+2])#son x,y,z las componentes del i-esimo
#    ofile.write('\n')    

#for v in vect:
#    v[0] #es el autovalor
#    for i in range(1,len(v),3):
#        (v[i], v[i+1],v[i+2]) #son x,y,z las componentes del i-esimo
#    minimod= sqrt(v[i]**2+v[i+1]**2+v[i+2]**2)
#    print minimod
#    ofile.write('\n')    
