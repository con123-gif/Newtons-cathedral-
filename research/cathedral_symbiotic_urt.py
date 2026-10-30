#!/usr/bin/env python3
"""Newton's Cathedral: symbiotic URT history <-> geometry prototype.
A constructive finite model, NOT a claim to have derived physical spacetime.
Requires numpy and scipy. See 2026-10-30-symbiotic-urt-history-geometry.md.
"""
from math import comb, pi, sqrt, log
import numpy as np
from scipy.special import logsumexp

PHI=(1+sqrt(5))/2
DELTA=3/20-80*pi/(1053*PHI)
ETA=-log(DELTA)

def history_hamiltonian(n):
    N=1<<n
    H=comb(n,2)*np.eye(N)
    for a in range(n):
        for b in range(a+1,n):
            mask=(1<<a)|(1<<b)
            for x in range(N):
                H[x,x^mask]-=1
    return H

def exact_spectrum(n):
    return sorted([2*k*(n-k) for k in range(n+1)
                   for _ in range(comb(n,k))])

class SymbioticURT:
    def __init__(self,n=6,source=True,seed=None):
        self.n=n
        self.N=1<<n
        self.i,self.j=np.triu_indices(self.N,1)
        self.E=len(self.i)
        self.B=self.N-1
        self.H=history_hamiltonian(n) if source else np.zeros((self.N,self.N))
        self.shells=np.array([(int(x)^int(y)).bit_count()
                              for x,y in zip(self.i,self.j)])
        if seed is None:
            self.w=np.full(self.E,self.B/self.E)
        else:
            rng=np.random.default_rng(seed)
            self.w=np.exp(rng.uniform(-1,1,size=self.E))
            self.w*=self.B/self.w.sum()

    def laplacian(self,w):
        L=np.zeros((self.N,self.N))
        np.add.at(L,(self.i,self.i),w)
        np.add.at(L,(self.j,self.j),w)
        np.add.at(L,(self.i,self.j),-w)
        np.add.at(L,(self.j,self.i),-w)
        return L

    def response(self,w=None):
        if w is None:w=self.w
        A=np.eye(self.N)+self.H+self.laplacian(w)
        ev,Q=np.linalg.eigh(A)
        if ev.min()<1-1e-9:raise AssertionError("positivity failed")
        C=(Q/ev)@Q.T
        R=C[self.i,self.i]+C[self.j,self.j]-2*C[self.i,self.j]
        F=np.log(ev).sum()/2 + (w*np.log(w/(self.B/self.E))).sum()/ETA
        return float(F), R, C

    def iterate(self,steps=100):
        initial,*_=self.response()
        for step in range(steps):
            before,R,C=self.response()
            old=self.w.copy()
            scores=-ETA*R/2
            self.w=self.B*np.exp(scores-logsumexp(scores))
            after,*_=self.response()
            if after>before+1e-9:
                raise AssertionError(f"free energy increased: {before} -> {after}")
            if np.max(np.abs(self.w-old))<1e-13:break
        final,R,C=self.response()
        return {
            "N":self.N, "iterations":step+1,"F_before":initial,
            "F_after":final,"weight_coefficient_of_variation":float(self.w.std()/self.w.mean()),
            "weights_by_hamming_shell":{
                str(d):float(self.w[self.shells==d].mean()/(self.B/self.E))
                for d in range(1,self.n+1)},
            "total_edge_budget":float(self.w.sum()),
        }

def verify():
    for n in (4,5,6):
        H=history_hamiltonian(n)
        assert np.allclose(np.linalg.eigvalsh(H),exact_spectrum(n))
        for source in (True,False):
            model=SymbioticURT(n,source)
            before,R,_=model.response()
            edge=1
            wplus=model.w.copy();wplus[edge]+=1e-6
            wminus=model.w.copy();wminus[edge]-=1e-6
            def log_det(w):
                return np.linalg.slogdet(np.eye(model.N)+model.H+
                                         model.laplacian(w))[1]/2
            derivative=(log_det(wplus)-log_det(wminus))/(2e-6)
            assert abs(derivative-R[edge]/2)<1e-7
            result=model.iterate()
            if not source:assert result["weight_coefficient_of_variation"]<1e-10
            assert abs(result["total_edge_budget"]-(model.N-1))<1e-8
            print("history" if source else "no-history",result)
        other=SymbioticURT(n,True,5).iterate()
        print("random initial geometry:",other["N"],other["weight_coefficient_of_variation"])
    print("PASS: exact spectra, resistance response, positive bounded feedback, monotone free energy.")

if __name__=="__main__":
    verify()
