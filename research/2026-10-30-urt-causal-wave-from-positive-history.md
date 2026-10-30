# Newton's Cathedral: Causal wave from 64-history and the 24-clock (30 Oct 2026)

**Result:** Exact, executable **conditional physics model**. A local positive history transfer yields two gapless, isotropic long-wavelength wave branches without taking a wave equation as input. It is NOT yet the uniquely derived original URT source-loaded T_star, a photon, a graviton, full Lorentz invariance, or a theory of nature.

**Five-solid sector:** Rebuild all five oriented Platonic C0-C1-C2 cellular complexes. Their aggregate C has 50+90+50=190 coordinates, Hodge-Dirac D rank 180, ker D dimension 10, Tr D²=720 and Tr D⁴=3456. Define a positive incidence-graph Laplacian L190 from abs(D) plus symmetry-preserving cross-solid complete bipartite contacts 1/(n_s n_t) between blocks of sizes (14,26,26,62,62). The total weight across any pair of solids is 1. Because ceil(max degree)=6, T190=I−L190/12 is an entrywise-nonnegative, row-stochastic, positive-semidefinite transfer. Its first excited eigenvalue is 739/744, with Szegedy frequency acos(739/744)=0.115999749914. The inter-solid contacts are a **new geometric premise**, not a uniqueness result.

**History and spatial motion:** The old six-axis history H8=15I−sum_{i<j}X_iX_j has exact spectrum 0(2),10(12),16(30),18(20). Pair each history s∈{±1}⁶ with n∈Z/24Z. Let u_i be the six antipodal unit icosahedral axes and p_i=s_i u_i. A forward directed ordered-pair flip (i,j) changes (s,n,x) to (s^ij,n+1,x+p_i×p_j); backward clock flips (s,n,x) to (s^ij,n−1,x−p_i×p_j). Pick all 30 ordered pairs and both clock orientations uniformly. This oriented *cross-product transport rule is a new microscopic premise*, justified as the minimal SO(3)-equivariant antisymmetric bilinear in two occupied axes; its overall length is in unit-icosahedron radius units. Reversal holds exactly since flipping both s_i,s_j leaves p_i×p_j invariant.

**Novel physical mechanism:** If displacement were instead p_i+p_j, it would be an exact coboundary: p_i+p_j=X(s)−X(s^ij), X=sum_i p_i/2. Any closed history cycle would produce zero spatial displacement. The antisymmetric cross product is non-exact: repeat one ordered pair 24 times with forward clock steps, and both history and clock return while the spatial coordinate translates by 24(u_i×u_j) of exact length 48/√5=21.466252583997978. Every individual spatial step has length 2/√5; propagation is strictly finite range per tick.

**Exact Bloch/Walsh solution:** For physical momentum k∈R³ and clock momentum q=2πm/24, the real symmetric raw Markov transfer has eigenvalues
λ_raw(t,k,q)=[cos q/15] sum_{i<j} (-1)^(t_i+t_j) cos[k·(u_i×u_j)],
t∈F2^6.
At k=q=0, these are 1(2),1/3(12),-1/15(30),-1/5(20). Since the 24-clock gives an EXACT eigenvalue -1 at q=π, the minimal locally lazy positive transfer is T_hc=(I+P_raw)/2; the self-loop probability 1/2 is fixed as the least admissible factor for T=B†B in this lazy family.

The six icosahedral axes give exact invariant Gram identities sum_i u_i u_i^T=2I3 and sum_{i<j}(u_i×u_j)(u_i×u_j)^T=4I3. For the two protected Walsh modes t=000000 and 111111,
λ_T(k,q)=1/2+[cos q/30]sum_{i<j}cos[k·(u_i×u_j)]
=1−|k|²/15−q²/4+O(k⁴,q⁴,k²q²).

Use the standard exact Szegedy/Halmos reversible lift: A|x>=sum_y√T_xy|x,y>, S|x,y>=|y,x>, U=S(2AA†−I). The unitary eigenphase is ω=acos λ. Thus for q=0,
**ω(k)=√(2/15)|k|+O(|k|³)**.
The emergent dimensionless low-k wave speed is √(2/15)=0.3651483716701107, and the ratio to the strict microscopic one-tick bound 2/√5 is **1/√6**, not a fit. Physical c requires deriving spatial/clock dimensional scales.

The full combined transfer T_total=T190⊗T_hc acts on 190×64×24=291840 internal states together with the discrete additive group of spatial cross-product displacements. One common all-five-solid mode, one q=0 clock mode, and two parity-history zero modes yield exactly **two** gapless spatial branches. The first excited internal frequencies are 0.11599975 (cross-solid geometry), 0.1848549967 (24-clock), 0.8410686706 (history E10), 1.0852782045 (history E16), 1.1592794807 (history E18). These are mathematical frequency bands, not identified particle masses.

**Executed independent verification:** actual oriented all-five Hodge integer boundaries and traces; 64×64 original history Hamiltonian; 1536×1536 sparse reversible history-clock Markov, its two +1 and two -1 eigenvalues and positive lazy transfer; exact icosahedral vector/cross-product Gram; 24-step nonzero spatial holonomy; finite 4-node Szegedy unitary unitarity and spectral polynomial (<8e-16 residual); 30 random momentum-direction waves matching speed within 2.4e-5 relative for |k|<=0.04.

**Not yet derived:** new cross-product transition as a necessary output of original species-loaded URT T_star; actual four-sheet chirality and explicit H13/H51 matter currents; physical frame coevolution with curvature; 4D Lorentz invariance and gravitational Ward constraints; photon spin and electric charge; Newton constant; experimental particle masses. The originally oriented Hodge boundaries were preserved but the positive 190 graph transfer uses unsigned incidence. The positive unitary-lift mechanism is a mathematically tangible corridor from bounded recursion to physical propagation, **not the full universe**.

The exact complete executable package, result JSON and 10KB derivation are attached to the Oct 30 2026 ChatGPT turn as `Cathedral_Causal_Recursive_Wave_2026-10-30.zip`.


## Exact fourth-order isotropy and a higher-order propagation prediction

The 15 pair-bivectors have the additional invariant identity
`sum_{i<j}[k·(u_i×u_j)]^4 = (48/25)|k|^4`.
This follows from icosahedral rotational invariance at degree four and the fixed norm of every pair-bivector. It was independently checked in five directions to <1.2e-15.

Therefore the positive protected transfer and unitary wave phase have the **exact asymptotic expansions**

`λ_T(k,0) = 1 − |k|²/15 + |k|⁴/375 + O(|k|⁶)`;

`ω(k) = sqrt(2/15)|k| [1 − (13/900)|k|² + O(|k|⁴)]`.

Thus the long-wavelength speed is rotationally isotropic **through the first dispersive correction**, despite the discrete icosahedral microscopic directions. Potential anisotropy first enters through sixth-degree directional invariants. The coefficient −13/900 is another parameter-free-in-model prediction; numerical tests at |k|=0.01–0.04 match to ~2e-12 absolute in phase.
