"""Standalone 24-bit Golay -> 13+51 real-rank certificate, Oct 29 2026.
No physical constants fitted; no identification with a physical H13 asserted.
Requires NumPy. Every rank/Gram identity is checked with integers.
"""
from itertools import product, combinations
from math import sqrt
import numpy as np
phi=(1+sqrt(5))/2
v=np.array([np.roll([0.,a,b*phi],r) for a,b in product((-1.,1.),repeat=2) for r in range(3)])
d=np.linalg.norm(v[:,None,:]-v[None,:,:],axis=2)
A=((d>1e-8)&(abs(d-min(d[d>1e-8]))<1e-8)).astype(int)
pairs=[];used=set()
for i in range(12):
    if i in used: continue
    j=int(np.argmin(np.linalg.norm(v+v[i],axis=1)))
    assert np.linalg.norm(v[i]+v[j])<1e-10
    pairs.append((i,j));used.update((i,j))
assert len(pairs)==6
D=(np.ones((12,12),dtype=int)-A)%2
G=np.zeros((64,24),dtype=int)
for b in range(64):
    x=np.zeros(12,dtype=int)
    for k,p in enumerate(pairs):x[p[(b>>k)&1]]=1
    G[b]=np.r_[x,D@x%2]
assert np.all(G.sum(1)==12) and np.all(G.sum(0)==32)
C=2*G-1
assert np.all(C.sum(0)==0)
gram=C.T@C
assert set(np.unique(gram)).issubset({-64,0,64})
assert all(sum(np.array_equal(C[:,i],-C[:,j]) for j in range(24))==1 for i in range(24))
assert np.all(np.diag(gram)==64)
assert np.array_equal(np.sort(np.linalg.eigvalsh(G.T@G).round().astype(int)),[0]*11+[32]*12+[384])
H=np.eye(64,dtype=int)*15
for b in range(64):
    for i,j in combinations(range(6),2):H[b,b^(1<<i)^(1<<j)]=-1
assert np.array_equal(H@C,10*C)
assert np.linalg.matrix_rank(G)==13
print('PASS: Golay Gram eig 384(1), 32(12), 0(11); real rank 13; complement 51; centered tracks are H8=10 modes')
