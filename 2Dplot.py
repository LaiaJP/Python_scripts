#!python
'''
======================
2D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import csv


#fig = plt.figure()
#ax = fig.gca(projection='3d')

# Read data.
Xtot=[]
Ytot=[]
Ztot=[]
#for i in np.arange(5.5, 5.8, 0.1):
X=[]
Y=[]
Z=[]
filename='free_energy'
with open(filename,'r') as f:
    reader = csv.reader(f,delimiter=' ')
    for row in reader:
        X.append(float(row[0]))
        Y.append(float(row[1])*180/(-3.141592))
        Z.append(float(row[2]))
#Xtot.append(X)
#Ytot.append(Y)
#Ztot.append(Z)
Xproba=[0.0]*500
Yproba=[0.0]*500
Zproba=[]
for i in range(0, 500, 1):
     Ztemp=[]
     Yproba[i]=Y[i]
     for j in range(0, 500, 1):
         Xproba[j]=X[j*500]
         Ztemp.append(Z[i+j*500])
     Zproba.append(Ztemp)


# Plot the surface.
#surf = ax.contourf(Xtot, Ytot, Ztot, zdir='z', offset=0, cmap=cm.jet, linewidth=0, antialiased=False)
plt.contourf(Xproba, Yproba, Zproba, 100, cmap=cm.jet, linewidth=0, antialiased=False, vmin=0, vmax=20)

# Customize the axis.
#plt.set_xlabel('Coordinate 1')
#plt.xlim(5.5, 13)
#plt.ylabel('Coordinate 2')
#plt.ylim(70, -70)
#ax.set_zlabel('Energy')
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.3, aspect=5)
plt.colorbar(shrink=0.3, aspect=5)

# Customize the axis.
plt.xlabel('Reaction coordinate 1')
#plt.xlim(5.5, 13)
plt.ylabel('Reaction coordinate 2')
#plt.ylim(7.6, 12)

plt.savefig('2Dplot.svg')
plt.show()

