# Cathedral relative-information gravity sector — 2026-10-30

**Physical status:** Exact information-metric curvature, long-range scalar Green function, spin-2 algebra and linearized Ward checks; not a derived Newton constant, equivalence principle, or evidence of physical gravitons.

Start from the existing hidden 4+4 state rho_*=(I4 ⊕ Delta² I4)/[4(1+Delta²)], eta=-ln Delta, Delta=3/20-80pi/(1053phi). Map an SO(3) spatial symmetric-tracefree quadrupole Q (five independent components) by a Frobenius-isometric B(Q) into Hom(R4,R4), with skew J(Q)=[0,-B(Q)^T;B(Q),0]. Its state rho(Q)=exp(J(Q))rho_*exp(-J(Q)) obeys

D(rho(0)||rho(dQ)) = [eta*tanh(eta)/2] ||dQ||² + O(||dQ||³).

**New physical premise:** Give adjacent spatial regions a *relative* information energy sum_{<xy>} D(rho(Q_x)||rho(Q_y)). This yields a gradient coefficient kappa=eta*tanh eta = 5.995723686480836 with **no on-site mass term** for a common uniform Q. On-site divergence to a fixed rho_* would instead generate screening.

Under the **further** Newtonian-metric-constraint/source premise E[Phi]=kappa/2 ∫|grad Phi|² - ∫J Phi, the static field has -kappa Laplacian Phi=J and Phi(r)=J/(4pi kappa r). In 3D, the force has inverse-square dependence. Explicit numerical inversion of the 128³ periodic lattice Laplacian (zero mode removed), fitting r=6..23 to A/r+B, gives A=0.01333504578; analytic 1/(4pi kappa)=0.01327237139 (0.4722% finite-lattice deviation). At r=8 the screened reference Green function is 7.884e-7, vs 0.00137252 for the massless model.

For 30 random nonzero spatial wavevectors, the TT projector on the 5D STF space has rank 2. The 4D massless Fierz–Pauli linearized Einstein operator separately satisfies k^mu E_mu nu=0 and E(k_mu xi_nu+k_nu xi_mu)=0 in 100 random checks. **These are necessary ingredients, not sufficient:** neither the 4D diffeomorphism symmetry nor universal stress-energy coupling has been derived from microscopic URT. Five STF scalar components do not become a physical graviton merely by projecting two components.

The earlier 64-history finite U(1) link-twist Hessian 0.03258930167 is not a gravitational coupling. An internal compact U(1) interpretation with this as bare beta would be in a strong-coupling regime; it does not yield a long-range spin-2 mediator. Instead, candidate gravity arises from a **distinct geometric variation of the same history state**. This exact kappa is also numerically identical to the 2026-10-28 SU(2) entropic Wilson coefficient under a separately constructed bridge, because both are eta*tanh eta. Equal stiffness does not identify the gauge group or field.

**Critical next calculation:** derive a single 4D coframe and Einstein/Fierz–Pauli Ward constraint from the source-loaded **whole Cathedral** 190D all-Platonic geometry × coupled history × 24-time ordering, and show universal source coupling. Newton's physical G and the Planck scale are not predicted; a spatial scale and source normalization remain necessary.

Executed artifact in conversation: `cathedral_gravity_candidate.py`, `CATHEDRAL_GRAVITY_CANDIDATE_RESULTS.json`, `CATHEDRAL_INFORMATION_GRAVITY_2026-10-30.md`.