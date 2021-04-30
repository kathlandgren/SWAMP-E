# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:07:20 2021

@author: ek672
"""

import params as p
import main_function as main


M=p.M

dt1=10
# Length of the run in time steps
tmax = p.tmax
#surface gravity
g=p.g
#radiative time scale in Earth days
taurad=p.taurad
#drag time scale in Earth days
taudrag=p.taudrag
#mean geopotential height. In hot Jupiter case, Phibar is the flat nightside thickness
Phibar=p.Phibar
#the difference in radiative-equilibrium thickness between the substellar point and the nightside
DPhieq=p.DPhieq

#rotation rate of the planet, radians per second
omega=p.omega
#planetary radius, meters
a=p.a
#angle for test cases 1 and 2, radians
a1=p.a1
#test case, number
test=p.test

#colorbar settings for plotting
minlevel=p.minlevel
maxlevel=p.maxlevel

#forcing flag
forcflag=p.forcflag
#hyperviscosity filter flag
diffflag=p.diffflag

#continuation flag
contflag=p.contflag
#flag to save
saveflag=p.saveflag
#save frequency
savefreq=p.savefreq

#flag for anti-aliasing filter as in Hack and Jakob (1992) eq. (4.4)
modalflag=p.modalflag
# if modalflag==1:
alpha=p.alpha

plotflag=p.plotflag
plotfreq=p.plotfreq

#make these optional arguments
k1=p.k1
# k2=p.k2
pressure=p.pressure
R=p.R
Cp=p.Cp
sigmaSB=p.sigmaSB

k2vec=[0.0002,0.002,1*10**(-2),2*10**(-2)]
for i in range(len(k2vec)):
    k2=k2vec[i]
    print(k2)
    
    main.main(M,dt1,tmax,g,taurad,taudrag,Phibar,DPhieq,omega,a,a1,test,minlevel, maxlevel, forcflag,diffflag,modalflag,alpha,plotflag, plotfreq,contflag,saveflag,savefreq,k1,k2,pressure,Cp,R,sigmaSB)





