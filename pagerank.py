# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

n=int(input("Enter the number of pages"))

d=0.85
eps=1.0e-8

print("\nPLease Enter the Adjancency matrix")
print("\nTyp 1 if thier is link from a page i to j else type 0")

links=[]
for i in range(0,n):
    L=[]
    in range(0,n):
        L.append(int(input('Page'+str(i+1)+' to Page '+str(j+1)+':')))
    links.append(L) for j
        
outboundL=np.zeros((n,1),dtype=int)

for i in range(0,n):
    for j in range(0,n):
        if links[i][j]==1:
            outboundL[i]=outboundL[i]+1
 

M=np.zeros((n,n))
for i in range(0,n):
    for j in range(0,n):
        if links[j][i]==1:
            M[i][j]= 1/outboundL[j]
            
M=np.matrix(M)
oneColMat=np.matrix(np.ones((n,1),dtype=int))

R=np.matrix(np.full((n,1),1/n))
    
while True:
    Rnext = d *np.dot(M,R)+((1-d)/n)*oneColMat
    diff=np.subtract(Rnext,R)
    if np.linalg.norm(diff)<eps:
        break
    R=Rnext

    
               