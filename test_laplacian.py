# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:33:49 2021

@author: ek672
"""

import numpy as np
import matplotlib.pyplot as plt

import fft_legendre_trans as rfl
import params as p
import initial_conditions as ic
import tstepping_new as tstep

M = 63
# N = p.N
# Length of the run in time steps
tmax = p.tmax
# Sine of the latitude
# mus = p.mus
# Wieghts for integrating
# w = p.w
# lambdas=p.lambdas
g=p.g
taurad=p.taurad
taudrag=p.taudrag
Phibar=p.Phibar
omega=p.omega
a=p.a
a1=np.pi/2-0.05#p.a1
test=1
N,I,J,dt,K4,lambdas,mus,w=ic.spectral_params(M)
# K4=K4*10**10
dt=100 #dt/10

# Associated Legendre Polynomials and their derivatives
Pmn, Hmn = rfl.PmnHmn(J, M, N, mus)

SU0, sina, cosa, etaamp,Phiamp=ic.test1_init(a, omega, a1)
etaic0, etaic1, deltaic0, deltaic1, Phiic0, Phiic1=ic.state_var_init(I,J,mus,lambdas,test,etaamp,a,sina,cosa,Phibar,Phiamp)
Uic,Vic=ic.velocity_init(I,J,SU0,cosa,sina,mus,lambdas,test)
Aic,Bic,Cic,Dic,Eic=ic.ABCDE_init(Uic,Vic,etaic0,Phiic0,mus,I,J)


fmn=np.zeros([M+1,N+1]) #TODO make a function in tstep
fmn[0,1]=omega/np.sqrt(0.375)

flatlon=np.zeros((J,I))
for i in range(I):
    flatlon[:,i]=2*omega*mus

tstepcoeffmn=tstep.tstepcoeffmn(M,N,a)
tstepcoeff=tstep.tstepcoeff(J,M,dt,mus,a)
tstepcoeff2=tstep.tstepcoeff2(J,M,dt,a)
mJarray=tstep.mJarray(J,M)
marray=tstep.marray(M, N)
narray=tstep.narray(M,N)

sf=np.zeros((J,I))
vp=np.zeros((J,I))
for i in range(I):
    sf[:,i] = -a*SU0*(mus*cosa-sina*np.cos(lambdas[i])*np.sqrt(1-mus**2))


def laplacian(Xi,I,J,M,N,Pmn,w,a,narray):
    
    Xim=rfl.fwd_fft_trunc(Xi,I,M)
    
    Xim=rfl.fwd_fft_trunc(Xi,I,M)
    step1=Xim/a**2
    step2=rfl.fwd_leg(step1, J, M, N, Pmn, w)
    
    step3=np.multiply(-narray,step2)
    
    step4=rfl.invrs_leg(step3, I,J, M, N, Pmn)
    lapXi=rfl.invrs_fft(step4, I)
    
    return lapXi

WolframLap=np.zeros((J,I))
WolframLap2=np.zeros((J,I)) 
WolframLap3=np.zeros((J,I)) 

for i in range(I):
    for j in range(J):
        WolframLap[j,i]=-2*a*SU0*(cosa*mus[j]/np.sqrt(1-mus[j]**2)+np.cos(lambdas[i])*sina)*mus[j]/a**2
        WolframLap2[j,i]=-2*SU0*(cosa*np.sqrt(1-mus[j]**2)/mus[j]+np.cos(lambdas[i])*sina)*np.sqrt(1-mus[j]**2)/a    
        WolframLap3[j,i]=np.sqrt(2)*SU0*(mus[j]+np.cos(lambdas[i]-np.pi)*np.sqrt(1-mus[j]**2))/a  
        
        #etaic0[j,i]=(SU0/a)*(+0.0999583*mus[j]+1.9975*np.cos(lambdas[i]-np.pi)*np.sqrt(1-mus[j]**2))
 
lapSF=laplacian(sf,I,J,M,N,Pmn,w,a,narray)

plt.contourf(lambdas, mus, lapSF)
plt.colorbar()
plt.title('Laplacian')
plt.show()

plt.contourf(lambdas, mus, WolframLap3)
plt.colorbar()
plt.title('Wolfram Laplacian')
plt.show()

plt.contourf(lambdas, mus, etaic0)
plt.colorbar()
plt.title('eta')
plt.show()

plt.contourf(lambdas, mus, lapSF+flatlon)
plt.colorbar()
plt.title('Laplacian with Coriolis force')
plt.show()

plt.contourf(lambdas, mus, lapSF+flatlon-etaic0)
plt.colorbar()
plt.title('Difference')
plt.show()

plt.contourf(lambdas, mus, flatlon)
plt.colorbar()
plt.title('Coriolis force')
plt.show()


plt.contourf(lambdas, mus, sf)
plt.colorbar()
plt.title('Stream Function')
plt.show()
    
    
    