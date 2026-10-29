# Cathedral: exact 64D chiral hybridization and protected hidden transfer — 29 October 2026

**Status:** Executed exact 64×64 finite operator construction, not a proven unique Golay/URT or particle-physics action. Zero fitted experimental values.

Let B be unsigned 12×20 icosahedral vertex–face incidence, L_I and L_D the icosahedral and dual dodecahedral Laplacians, v=1_12/sqrt(12), Q=I_12−vvᵀ. Exact identities:
- B Bᵀ=15I_12−2L_I; Bᵀ B=A_D(A_D+2I_20); rank B=12; ||B||²=15
- ker B=4_3⊕4_5 (8D), with B P_hidden=0.

Use H64=12_A⊕12_B⊕20_A⊕20_B and the 13D visible carrier 12_A⊕span(v_B). The 24D vertex operator and 40D doubled-face operator are:

```
K_V = [ L_I+I_12       −1_12 vᵀ      ]
      [ −v 1_12ᵀ       L_I+12vvᵀ    ]

K_F = [ L_D+I_20       −I_20        ]
      [ −I_20          L_D+I_20     ]
```

Connect the 11D nonconstant B-vertex complement to the **antisymmetric** face sheet by the operator-norm-normalized incidence C=Q B/sqrt(30). The only nonzero coupling blocks are V_(12_B,20_A)=C, V_(12_B,20_B)=−C and their adjoints. K64=(K_V⊕K_F)+V.

**Exact checks:** K64 is real symmetric positive-semidefinite with 2 zero modes; the 13/51 decomposition remains invariant. Tr K64=304, Tr K64²=1826; before coupling Tr K0²=1820. The added 6 is Tr V²=2(Tr BBᵀ−15)/15.

On A5 irreps 3 and 3′ the vertex and antisymmetric-face energies have zero detuning d_3=5−sqrt(5), d_3′=5+sqrt(5). Their 2×2 hybridization blocks are [d_r,s_r/sqrt(15);s_r/sqrt(15),d_r], with s_3²=5+2sqrt(5), s_3′²=5−2sqrt(5). Hence eigenvalues:
- E_(3,±)=5−sqrt(5) ±sqrt((5+2sqrt(5))/15), each multiplicity 3;
- E_(3′,±)=5+sqrt(5) ±sqrt((5−2sqrt(5))/15), each multiplicity 3.
- s_3′/s_3=φ^(−3) and squared ratio φ^(−6), **derived directly from incidence**.
- On irrep 5, off-resonant mixed eigenvalues 5±sqrt(6/5) (each ×5); symmetric face remains 2 (×5).

All 16 hidden doubled-face modes are **unaffected** because B P_hidden=0. Spectrum remains 3(x4),5(x8),7(x4), with the original 8D master state after tracing out the sheet:
ρ*=(P3+Δ²P5)/[4(1+Δ²)], Δ=3/20−80π/(1053φ).

The exact chiral-vertex self-energy after eliminating the antisymmetric face sheet is
Σ(z)=(1/15) Q B (zI−L_D−2I)^(−1) Bᵀ Q.
On irrep r∈{3,3′}: Σ_r(z)=(15−2d_r)/[15(z−d_r)].
On the irrep 5: Σ_5(z)=1/[5(z−4)].

**Complete characteristic polynomial**
```
χ(z)=z²(z−13)(z−7)^9(z²−12z+31)^3
     (z−2)^6(z²−6z+4)^3(z−3)^4(z−5)^8
     ((45z⁴−900z³+6270z²−17580z+16501)/45)^3
     ((z−5)²−6/5)^5.
```
Degree 64, monic, Tr=304, Tr K²=1826.

**Limitation:** Canonical norm-one incidence and doubled-face identification are constructed geometric choices, not yet uniquely derived from Golay/URT. The 3↔3′ vertex–face resonances are not themselves left↔right mass terms. The chiral-changing chronological operator must be incorporated separately before physical lepton masses can be claimed.

Independent, complete exact SymPy + numerical eigenspectrum verification: `cathedral_64_chiral_hybridization_2026_10_29.py` (conversation artifact).
