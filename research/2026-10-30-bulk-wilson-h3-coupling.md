# Whole-Cathedral bulk dipole + Wilson clock dynamics (30 October 2026)

**Status:** Executed finite constructive model; the H3 relative-rotation physical interpretation is a proposed dynamical extension, not established experimental physics.

## Full operator
D is the complete 190D five-Platonic Hodge–Dirac operator; K64 the coupled 64D history operator; S_theta the 24-cycle shift with uniform **per-link** phase theta. Set r=pi/e and Delta=3/20-80pi/(1053phi), eta=-ln Delta. Define
B_theta=D⊗I⊗I+r I⊗sqrt(K64)⊗S_theta;
K_new(theta)=B_theta† B_theta+(C_top+C_bulk)⊗I64⊗I24.
C_top connects five solids' harmonic vertex/face modes, with spectrum {0 (2),5 (8)}. C_bulk connects the **30 vertex and face dipoles**, with spectrum {0 (6),5 (24)}. Both positive; C_top C_bulk=0.

## Exact invariant bulk reduction
The 30 dipole modes and their 30 D images form a 60D invariant subspace, separating from 10 harmonic and 120 other nonharmonic Hodge modes. Vertex eigenvalues are lambda=(4,2,4,3-sqrt5,5-sqrt5); face-normal values are the same multiset by duality. Each of two dipole types in each of three directions gives the same 10x10 block. With Lambda=diag(lambda), R=sqrt(Lambda), L5=5I5-J5, a=r sqrt(kappa), c=cos(theta+2pi k/24):
K_dip(kappa,k,theta)=[[Lambda+L5+a²I,2acR],[2acR,Lambda+a²I]],
repeated six times. Thus the full 291840D operator can be spectrally calculated without forming it as a dense matrix.

**Do not apply the previously factorized scalar Fourier–Bessel partition identity to the new full operator:** [D,C_bulk] is nonzero. The identity remains exact in the unaffected commuting sectors. Independently, graph winding guarantees that spectral traces of degree m<24 remain holonomy-independent; the first phase-bearing trace moment is m=24.

## Computed results
At the historical URT **per-link** theta=2pi/phi²:
- Kernel remains exactly 96: 2 common five-solid harmonics × 2 K64 zero modes × 24 clock sites.
- 384 relative harmonic-history-clock states are lifted to eigenvalue E=5.
- New minimum positive eigenvalue is **0.00767156306625516**, versus **0.00599216698241545** before C_bulk.
- The interacting dipole subspace itself has minimum **0.16395641569562946**.
- The global minimum comes from an unaffected Hodge eigenvalue d=-2 and history kappa=3, with opposite-sign partner. Exact eigenvalue expression:
lambda1=4+3(pi/e)²-4sqrt3(pi/e)cos[2pi(phi^-2-3/8)],
numerically 0.00767156306625516; multiplicity 48. This is an eigenvalue formula with global ordering checked numerically.

## Distinguish per-link and total holonomy
The original q=(pi/e) exp(i2pi/phi²) uses theta=2pi/phi² on **every link**, so the physical 24-step Wilson loop is Theta=24theta mod 2pi=1.05044974887139 rad. A distinct geometric H3 **total-loop** holonomy is Theta_H3=2pi/phi²=2.39996322972865 rad; its uniform link phase would be theta=Theta_H3/24. These are not the same physical prescription.

## Dynamical gauge-link equation
For 24 gauge sites with U(1) link phases theta_j(x), use
L_link=(f²/2)Σ_j(∂_mu theta_j-A_(mu,j+1)+A_(mu,j))².
The gauge-invariant Wilson scalar Θ=Σ_j theta_j has reduced kinetic action (f²/48)(∂Θ)² and hence equation
(f²/24)□Θ+∂_Θ V_eff(Θ)=0.
Twenty-three relative vector fields acquire masses, leaving one diagonal massless U(1) vector and one compact Wilson scalar.

With thermal effective potential V_th(Θ)=-(1/eta)log Tr exp[-eta K_new(Θ/24)]:
Z(0)=3065.59827904567; Z(Theta_H3)=2937.83123624578; Z(24Theta_H3)=3028.61643678190.
V'_th(Theta_H3)=0.00281969, so **golden holonomy is not the ordinary thermal equilibrium**. At trivial holonomy V''(0)=0.00400160965, corresponding to small-oscillation frequency 0.30990100309/f in model units.

## New parameter-free relative-frequency candidate for selecting golden holonomy
Take existing D6->H3 conjugate eigenvalues phi and -phi^-1 as **signed angular velocities** Omega*phi and -Omega/phi. After the fast branch's full period T_fast=2pi/(Omega phi), the slow branch accumulates signed phase -2pi/phi². The relative unitary holonomy is therefore exp(+i 2pi/phi²), independent of the arbitrary clock rate Omega. A gauge-invariant relative-holonomy effective potential V_rel(Θ)=V_th(Θ-Theta_H3) then has a golden minimum with no measured fine-structure input.

**Physical qualification:** Taking representation eigenvalues as angular velocities and coupling this relative phase to the Wilson clock are new dynamical postulates, not consequences of A5 representation theory. Without their derivation from microscopic URT dynamics this remains a parameter-free candidate model, not confirmation of nature. Equality of a spectral E=5 with a hidden-sector level alone does not imply mixing or gravitational entanglement.

Executable numerical calculation: conversation artifact `cathedral_bulk_wilson_dynamics.py`.