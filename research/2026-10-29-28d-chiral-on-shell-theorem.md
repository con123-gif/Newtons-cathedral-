# Exact 28D two-hidden-state chiral theorem and on-shell three-channel response (2026-10-29)

Status: exact finite mathematics for the stated Cathedral 8D hidden representation; conditional physical interpretation. No observed masses or fitted coefficients.

Let the hidden A5 representation be H8 = 4_3 ⊕ 4_5 = V4 ⊗ C², with L_hid = I4 ⊗ diag(3,5). Form its fermionic/exterior two-excitation sector Λ²H8 (dimension 28). The canonical decomposition is

Λ²(V4⊗C²) = (Λ²V4⊗Sym²C²) ⊕ (Sym²V4⊗Λ²C²).

Since Λ²(4)=3⊕3′ and Sym²(4)=1⊕4⊕5, obtain the exact A5 decomposition

**Λ²H8 = 3(3⊕3′) ⊕ (1⊕4⊕5)**, i.e. 18 chiral-representation states plus 10 other states.

Second-quantized hidden Laplacian dΓ(L_hid) has spectrum 6^(6),8^(16),10^(6). The chiral 18D block has 6^(6),8^(6),10^(6); 10D remainder has eigenvalue 8^(10). Thus exactly three copies of the mathematical 3⊕3′ carrier occur at equal gaps. This does not yet identify physical fermion generations.

**Constructive chiral projector:** take the 10D oriented-pair action R_∧ on Λ²R5. Build the 60 elements of A5 as even permutations of five letters; its 24 five-cycles split into two conjugacy classes C+,C− (12 each). Define P = Λ²(I5−11ᵀ/5) (a rank-6 projector) and Z = Σ_{g∈C+}R_∧(g)−Σ_{g∈C−}R_∧(g). Exact matrices satisfy P²=P, ZP=PZ=Z, Z²=80P. Therefore P3=(P+Z/(4√5))/2 and P3′=(P−Z/(4√5))/2 are A5-equivariant, rank-three orthogonal projectors (labels swap under exchanging the two five-cycle classes).

**Three-level spectral self-energy:** use prior exact vertex-face Schur-complement functions Σ3(z)=(5+2√5)/[15(z−5+√5)], Σ3′(z)=(5−2√5)/[15(z−5−√5)]. At z=3,5,7 the sums are 8/3, 4/15, 0; the products are −1/45, −1/225, −1/45; the absolute chiral ratios are φ^12, φ^6, 1. Hence the functional-calculus operator P3⊗Σ3(diag(3,5,7)) + P3′⊗Σ3′(diag(3,5,7)) is explicitly defined on the 18D chiral carrier, with trace 44/5 and equivariance under all 60 rotations. The on-shell identification z=3,5,7 is a model prescription, not a derived physical mass shell.

**Fixed geometric mixing:** the earlier orbital Pauli flip X/√15 exchanges the two hidden 4D sectors. The second-quantized operator dΓ(L_hid + X/√15) preserves the 18D chiral carrier and has exact spectrum (8−2√2)^(6),8^(6),(8+2√2)^(6), while the other 10 states remain at energy 8. This is an explicit noncommuting, symmetry-preserving three-channel mixing construction.

**Chronological mass-block test:** with the original fivefold cubic M_chron=(2/√15)^3 Σ_{a<b<c}U_c U_bᵀ U_a, its squared singular values are {1/75,1/135,4/675}. The concrete two-leg dressing D_k=Σ3′(E_k) M_chron Σ3(E_k) at E_k=3,5,7 yields exactly D_k = −{M_chron/45,M_chron/225,M_chron/45}. Channel norm ratio 1:1/5:1, not the golden return-shell ratio φ^−4:φ^−2:1. Do not label the nine singular modes as the three charged-lepton masses without an additional dynamical selector.

**Static half-gap correction:** the half-gap for alpha_r(0)=d_r−Σ_r(0) is (19/20)√5, not (17/20)√5; the latter is not derived by this resolvent.

Verified in standalone SymPy script (conversation artifact) using explicit matrices and all 60 A5 rotations; all assertions pass. No empirical values inserted. Next objective: derive the physical A5-breaking chiral Dirac bilinear on the 18D carrier from the chronological history action, rather than assigning masses to representation channels.
