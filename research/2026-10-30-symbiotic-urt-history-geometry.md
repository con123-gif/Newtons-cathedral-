# Symbiotic URT — history generates geometry, geometry constrains history (30 Oct 2026)

**Status:** Exact constructive variational theorem and independently executed numerical tests, **not yet a physical theory of nature**. This is a dimension-independent **candidate URT recursion**. It does not claim to reconstruct the whole Cathedral, or to derive the original URT recursion from primitive first principles.

## No preselected spatial geometry

Start from n signed history axes, N=2^n states, and their existing canonical pair-flip history operator:

H_n = C(n,2) I - sum_{i<j} X_i X_j.

Its exact spectrum is 2k(n-k) with multiplicity C(n,k), for k=0,...,n. In the historical n=6 case it is 0(2),10(12),16(30),18(20).

All E=N(N-1)/2 undirected candidate links start at the **same strength**. With v_e=e_i-e_j, let L(w)=sum_e w_e v_e v_e^T. Use the *existing frozen* Cathedral eta=-log(3/20 - 80pi/(1053 phi)). Choose the structural edge budget B=N-1 and unit dimensionless mass as explicit postulates (not measured fit or forced results).

## Exact symbiotic generator

A(w)=I+H_n+L(w) > 0,
C(w)=A(w)^(-1) = integral_0^infinity exp(-t A(w)) dt,
R_e=v_e^T C(w) v_e,
w_e(next)=B exp(-eta R_e/2) / sum_f exp(-eta R_f/2).

The geometry changes the positive history propagator. The history's integrated response changes the next geometry. Both remain bounded, positive, and normalised. Repetition is genuine two-way feedback; graph response is not selected from a readout after the dynamics finishes.

## The exact variational theorem

For symmetric positive-definite C and w_e>0, sum w_e=B, define

F(C,w)= 1/2 Tr[(I+H_n+L(w))C] - 1/2 log det C - N/2
        + (1/eta) sum_e w_e log[w_e/(B/E)].

Minimising at fixed w gives the unique C=A(w)^(-1). Minimising at fixed C gives the unique softmax w-update. Therefore exact alternating minimisation never raises F. Eliminating C gives

F_eff(w)= 1/2 log det[I+H_n+L(w)]
          + (B/eta) KL(w/B || uniform).

Since H_n,L(w) are PSD, A>=I, 0<C<=I, and F_eff>=0. Thus the energy converges. Unique global minimiser or convergence of every coordinate **is not claimed in general**. The response identity is

d(1/2 log det A)/dw_e = 1/2 v_e^T A^(-1)v_e = R_e/2.

This equation makes the mutual regulation endogenous: history effective resistance *is* the geometric force.

## Executed results, no spatial graph input

Relative strengths of the final links versus equal starting links, classified **only after evolution** by history Hamming distance:

- n=4, N=16: d1 0.911499, d2 1.110517, d3 0.911499, d4 1.044905.
- n=5, N=32: d1 0.950958, d2 1.065008, d3 0.950958, d4 1.026919, d5 0.950958.
- n=6, N=64: d1 0.973822, d2 1.038907, d3 0.973822, d4 1.016320, d5 0.973822, d6 1.009281.

For n=6, F_eff falls from 90.55081135 to 90.54684590. Random initial geometry also converges to the same symmetry-class weights in the tested runs. Remove H_n and all weights remain uniform: the historical pair-flip correlations are what select the nonuniform geometry.

Executed checks: exact H_n spectra for n=4,5,6; finite-difference derivative of logdet against R_e/2; positive history covariance; non-increasing free energy; convergence and conserved edge budget; local gauge-conjugation of both history and geometry.

## 64 histories to the 24 readout

For the historical 64x24 binary G with rank(G)=13, the symbiotically generated SPD covariance pushes forward to C24=G^T C64 G. Rank(C24)=13 exactly, with numerical eigenvalues 384 (1), 2.46215195 (12), 0 (11). A 24-cycle **does not emerge** from the real symmetric readout: time/orientation needs a further covariant history rule. This readout rank does **not** identify the complete physical H13/H51 carrier.

## Next generator to construct (not yet derived)

Complex clock links can enter as v_e(theta)=e_i-exp(i theta_e)e_j, with A=I+H_n(theta)+sum_e w_e v_e(theta)v_e(theta)^dagger; the history H_n itself must be Peierls-covariant, not just the geometric links. The same variational response determines both weights and phase currents from the history covariance. Then evolve the *cellular boundary* operators with constraints ∂1∂2=0, instead of merely the graph, and test what ranks, topology, and geometries URT itself selects. The full 190-cell/64-history/24-clock/D6-H3/Golay system is a target, not a claimed output of this preliminary model.

This note records a **new testable construction**, not proof of electromagnetic gravity, Planck scales, golden holonomy or nature's unique law.