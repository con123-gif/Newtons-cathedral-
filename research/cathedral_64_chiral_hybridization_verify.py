"""Cathedral 64D chiral incidence hybridization: reproducible numerical verification.
Full exact SymPy reference is the conversation artifact of 29 Oct 2026.
Requires numpy and networkx. No measured physical inputs.
"""
import itertools
import numpy as np
import networkx as nx

g=nx.icosahedral_graph()
vs=sorted(g.nodes())
faces=[t for t in itertools.combinations(vs,3)
       if all(g.has_edge(a,b) for a,b in itertools.combinations(t,2))]
assert len(faces)==20
B=np.zeros((12,20))
for j,t in enumerate(faces):
    for i in t:B[i,j]=1
AI=nx.to_numpy_array(g,nodelist=vs)
LI=5*np.eye(12)-AI
AD=np.zeros((20,20))
for i,j in itertools.combinations(range(20),2):
    if len(set(faces[i]) & set(faces[j]))==2:AD[i,j]=AD[j,i]=1
LD=3*np.eye(20)-AD
assert np.allclose(B@B.T,15*np.eye(12)-2*LI)
assert np.allclose(B.T@B,AD@(AD+2*np.eye(20)))
assert np.linalg.matrix_rank(B)==12

v=np.ones((12,1))/np.sqrt(12)
P0=v@v.T
Q=np.eye(12)-P0
KV=np.block([[LI+np.eye(12),-np.ones((12,1))@v.T],
             [-v@np.ones((1,12)),LI+12*P0]])
KF=np.block([[LD+np.eye(20),-np.eye(20)],
             [-np.eye(20),LD+np.eye(20)]])
K=np.zeros((64,64))
K[:24,:24]=KV
K[24:,24:]=KF
C=Q@B/np.sqrt(30)
K[12:24,24:44]=C
K[12:24,44:64]=-C
K[24:44,12:24]=C.T
K[44:64,12:24]=-C.T
assert np.allclose(K,K.T)
assert np.isclose(np.trace(K),304)
assert np.isclose(np.trace(K@K),1826)
P13=np.zeros((64,64))
P13[:12,:12]=np.eye(12)
P13[12:24,12:24]=P0
assert np.isclose(np.trace(P13),13)
assert np.allclose(K@P13,P13@K)

r=np.sqrt(5)
s3=np.sqrt((5+2*r)/15)
s3p=np.sqrt((5-2*r)/15)
s5=np.sqrt(6/5)
pairs=[(0,1),(6-r,3),(7,5),(6+r,3),(13,1),
       (0,1),(2,1),(3-r,3),(5-r-s3,3),(5-r+s3,3),
       (3+r,3),(5+r-s3p,3),(5+r+s3p,3),
       (2,5),(5-s5,5),(5+s5,5),(3,4),(5,8),(7,4)]
expected=sorted(e for e,m in pairs for _ in range(m))
actual=np.linalg.eigvalsh(K)
assert len(expected)==64
assert np.allclose(actual,expected,atol=1e-10)
assert (abs(actual)<1e-10).sum()==2
assert np.isclose((s3p/s3)**2,((np.sqrt(5)-1)/2)**6)

# Hidden face kernel is annihilated by each added vertex-face link.
PH=np.eye(20)-B.T@np.linalg.solve(B@B.T,B)
assert np.isclose(np.trace(PH),8)
assert np.allclose(B@PH,0,atol=1e-12)
assert np.allclose(C@PH,0,atol=1e-12)
assert np.allclose(LD@PH,PH@LD)

print("PASS: 64D real symmetric PSD, 13/51 preservation,")
print("PASS: Tr K=304; Tr K²=1826; 2 zero modes")
print("PASS: exact chiral 3/3' and off-resonant 5 spectra")
print("PASS: double-sheet 8D hidden space is protected")
print("E3±:",5-r-s3,5-r+s3)
print("E3p±:",5+r-s3p,5+r+s3p)
