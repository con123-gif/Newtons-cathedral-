#!/usr/bin/env python3
"""Cathedral causal URT: regression checks of the 64-history/24-clock wave theorem.
For the complete all-five-Hodge verifier, see the Oct 30 research ZIP.
Requires numpy, scipy.
"""
from math import sqrt, pi, acos
import numpy as np
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import eigsh

phi=(1+sqrt(5))/2
v=[]
for a in (-1,1):
    for b in (-1,1):
        v += [(0.,a,b*phi),(a,b*phi,0.),(b*phi,0.,a)]
u=[]
for x in v:
    x=np.array(x,dtype=float)/sqrt(1+phi*phi)
    if not any(np.linalg.norm(x-y)<1e-12 or np.linalg.norm(x+y)<1e-12 for y in u):
        u.append(x)
u=np.array(u)
assert u.shape==(6,3)
assert np.allclose(u.T@u,2*np.eye(3))
cross=np.array([np.cross(u[i],u[j]) for i in range(6) for j in range(i+1,6)])
assert np.allclose(cross.T@cross,4*np.eye(3))
assert np.allclose(np.sum(cross**2,axis=1),4/5)
# The original (not guessed) 64-history pair-flip kinetic.
H=15*np.eye(64)
for i in range(6):
    for j in range(i+1,6):
        for b in range(64):
            H[b,b^(1<<i)^(1<<j)]-=1
assert np.allclose(np.linalg.eigvalsh(H),
                   [0]*2+[10]*12+[16]*30+[18]*20)
# Independently construct the exact 64*24 reversible Markov matrix.
rows=[];cols=[];weights=[]
for b in range(64):
    for n in range(24):
        for i in range(6):
            for j in range(i+1,6):
                flip=b^(1<<i)^(1<<j)
                for step in (-1,1):
                    rows.append(24*b+n)
                    cols.append(24*flip+(n+step)%24)
                    weights.append(1/30)
R=coo_matrix((weights,(rows,cols)),shape=(1536,1536)).tocsr()
assert (R-R.T).nnz==0
assert np.allclose(np.asarray(R.sum(axis=1)).ravel(),1)
hi=eigsh(R,k=4,which='LA',return_eigenvectors=False)
lo=eigsh(R,k=4,which='SA',return_eigenvectors=False)
assert np.sum(abs(hi-1)<1e-9)==2
assert np.sum(abs(lo+1)<1e-9)==2
T=(eye(1536,format='csr')+R)/2
assert min(eigsh(T,k=3,which='SA',return_eigenvectors=False))>-1e-11
# Oriented cross-product movement is not the gradient of an internal state.
b=0;clock=0;movement=np.zeros(3)
for _ in range(24):
    s0=-1 if b&1 else 1
    s1=-1 if b&2 else 1
    movement+=np.cross(s0*u[0],s1*u[1])
    b^=3;clock=(clock+1)%24
assert (b,clock)==(0,0)
assert np.isclose(np.linalg.norm(movement),48/sqrt(5))
def lam(k,q=0.,t=0):
    index=0;acc=0.
    for i in range(6):
        for j in range(i+1,6):
            sign=(-1)**(((t>>i)&1)^((t>>j)&1))
            acc+=sign*np.cos(k@cross[index])
            index+=1
    return (1+np.cos(q)*acc/15)/2
assert np.isclose(lam(np.zeros(3)),1)
assert np.isclose(lam(np.zeros(3),t=63),1)
assert np.isclose(lam(np.zeros(3),q=pi),0)
speed=sqrt(2/15);limit=2/sqrt(5)
for k in (0.005,0.01,0.02,0.04):
    for direction in np.eye(3):
        obs=acos(lam(k*direction))/k
        assert abs(obs/speed-1)<3e-5
assert np.isclose(speed/limit,1/sqrt(6))
clockgap=acos(lam(np.zeros(3),q=2*pi/24))
assert np.isclose(clockgap,0.18485499673482714)
print('PASS: H64, Z24, oriented holonomy, T=B†B positivity, and causal wave.')
print('speed',speed,'max single-step',limit,'speed ratio',speed/limit)
print('closed 24-step displacement',np.linalg.norm(movement))
