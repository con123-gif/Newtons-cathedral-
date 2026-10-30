#!/usr/bin/env python3
"""Selected topology from reciprocal URT geometry; requires symbiotic_urt module."""
from math import comb
import numpy as np
from cathedral_symbiotic_urt import SymbioticURT

def analyze(n):
    s=SymbioticURT(n,True)
    s.iterate()
    N=s.N;k=N//2
    select=s.w>s.B/s.E+1e-12
    A=np.zeros((N,N),dtype=bool)
    A[s.i[select],s.j[select]]=True
    A[s.j[select],s.i[select]]=True
    parity=np.array([i.bit_count()%2 for i in range(N)])
    # No parity information entered the symbiotic update or the threshold.
    assert np.array_equal(A,(parity[:,None]==parity[None,:]) & (~np.eye(N,dtype=bool)))
    edges=int(select.sum())
    triangles=2*comb(k,3)
    r1=N-2
    r2=edges-N+2
    beta2=triangles-r2
    assert edges==2*comb(k,2)
    assert beta2==2*comb(k-1,3)
    if n==4:
        edgelist=list(zip(s.i[select].tolist(),s.j[select].tolist()))
        lookup={e:t for t,e in enumerate(edgelist)}
        B1=np.zeros((N,len(edgelist)),dtype=int)
        for t,(a,b) in enumerate(edgelist):
            B1[a,t]=-1; B1[b,t]=1
        faces=[(a,b,c) for a in range(N) for b in range(a+1,N)
               for c in range(b+1,N) if A[a,b] and A[b,c] and A[a,c]]
        B2=np.zeros((len(edgelist),len(faces)),dtype=int)
        for t,(a,b,c) in enumerate(faces):
            B2[lookup[(b,c)],t]=1
            B2[lookup[(a,c)],t]=-1
            B2[lookup[(a,b)],t]=1
        assert not np.any(B1@B2)
        assert np.linalg.matrix_rank(B1)==r1
        assert np.linalg.matrix_rank(B2)==r2
    return dict(N=N,components=2,edges=edges,faces=triangles,
                rank_d1=r1,rank_d2=r2,betti0=2,betti1=0,
                betti2_truncated_2_skeleton=beta2,
                betti2_full_flag_complex=0)

if __name__=="__main__":
    for n in (4,5,6):
        print(analyze(n))
    print("PASS: history graph and integer cellular topology")
