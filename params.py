
"""
Created on Wed Jun  3 18:41:45 2020

@author: ek672

This is the file containing the spectral, physical, and code parameters.
"""

import numpy as np

# #Spectral parameters
M=42 #the largest Fourier wave number
# N=M #highest degree of the Legendre functions for m=0
# I=192 #length of array/ number of samples
# J=96#int(np.ceil(I/2))


#time-stepping parameters
tmax=100#864 #number of time steps
# dt=900 #time step length, in seconds


#make these into a file that gets read later
test=1
##specifies the testing regime: 
#1 -- test 1 (advection)
# 2 -- Hot Jupiter (PBS) 
a1=np.pi/2 #alpha from test 1

if test==1: 
    omega=7.2921159*10**(-5) #rotation rate of the planet, radians per second
    a=6.37122*10**(6)  #radius of the planet, meters
    Phibar=1*(10**3) #Geopotential height
    g=9.8 #gravity of the planet in m/s^2
elif test==2:
    #Physical parameters
    omega=3.2*(10**(-5))#7.2921159*10**(-5) #rotation rate of the planet, radians per second
    a=8.2*(10**7)#6.37122*10**(6)  #radius of the planet, meters
    Phibar=4*(10**6) #1*(10**3) #Geopotential height #maybe 10*6 instead>
    g=9.8

#Hyperviscosity parameters
diffflag=1


#Modal Splitting Fiter 
modalflag=1
alpha=0.01 #filter coefficient to prevent aliasing

#forcing parameters
forcflag=1
taurad=3600*24*0.1 #in Earth days
taudrag=3600*24*1 #if set to -1, means infinity
Dheq=Phibar/g

zeroflag=0

expflag=1
#1 means explicit,
#anything else means semi-implicit scheme

#lat-lon grid points
# lambdas=np.linspace(-np.pi, np.pi-1/I, num=I) #longitudes
# [mus,w]=sp.roots_legendre(J) #Gaussian latitudes and weights
#\mu ranges from -1 to 1,\lambda ranges from 0 to 2\pi

