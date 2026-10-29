# Newton's Cathedral: whole-machine 278-cell experiment and Golay-rank theorem (29 Oct 2026)

## Scope / evidentiary status
A **constructed finite interacting network**, not the previously frozen source-loaded URT transfer T_star and not a demonstrated physical theory. The original five Platonic cellular complexes, signed 64 histories, 24 Golay coordinates, dodecahedral hidden projectors, and frozen Delta are retained. New premises: unit-weight intersolid nearest-direction contacts, a cell-incidence (Hasse) graph kinetic rather than the oriented Hodge kinetic, and a chosen cyclic order of the 24 Golay coordinates. The D6/H3, Leech/higher-dimensional, gauge, matter, gravity and continuum sectors are not fully dynamically incorporated.

## Exact 24->13+51 theorem
Enumerate all 64 histories by choosing one vertex from each of six antipodal icosahedral pairs. For each history x in F2^12, define its 24-coordinate binary Golay word as (x,(J-A_ico)x mod 2). Let G be the resulting 64-by-24 real 0/1 matrix and C=2G-1.

Direct combinatorial checks: every column of C is a nonconstant Walsh character of six history bits, the 24 columns form 12 **opposite pairs**, distinct pairs are orthogonal, and every column has zero sum. Consequently C^T C has eigenvalues 128 (12 times), 0 (12 times), and C is orthogonal to the constant column. Thus

G^T G = 16 J_24 + C^T C/4,

spec(G^T G) = {384(1), 32(12), 0(11)}.

This proves **rank G=13**, hence R^64 = im(G) (13) orthogonal-direct-sum ker(G^T) (51), and the columns of C satisfy H_8 C=10 C for the two-bit-flip history Laplacian H_8=15I-sum_{i<j} X_i X_j. The induced Golay-readout 13-space has history spectrum 0(1)+10(12); do **not** silently equate it with every earlier 13-carrier with different representation content.

The existing face-occupancy isometry U_h=M P_h/sqrt(2), P_h=P_3+P_5, obeys U_h^T U_h=P_h and H_8 U_h P_3=18 U_h P_3, H_8 U_h P_5=16 U_h P_5. An additional exact readout identity verified in this construction is G^T U_h=0 (numerical residual 1.47e-14). Thus both four-dimensional hidden eigenspaces lie in the newly identified 51-dimensional readout kernel.

## Full simultaneous linear operator
Each oriented Platonic surface complex contributes vertex, edge, face coordinates: (50,90,50), dimension 190. The oriented direct-sum Hodge-Dirac has Tr(D^2)=720, Tr(D^4)=3456. Define a **separate** 190-cell Hasse adjacency joining incident vertex-edge and edge-face cells (360 links). Connect tetra-cube, cube-octa, cube-dodeca and dodeca-icosa by unit-weight nearest-direction vertex links (respectively 16,24,32,36 links for the specified regular-coordinate embeddings). Add the H_8 history graph (480 links), the chosen 24-cycle (24 links), history-to-icosa vertex selection contacts (384 links), and history-to-24-bit Golay coordinate contacts (768 links). This gives a connected undirected 278-vertex contact graph with **2124 edges**. Let K be its combinatorial Laplacian.

Computed smallest eigenvalues of K:
0, 0.23735390582700938, 0.5485028763267096, 0.6481142203247416, 0.9311088758545342, 1.0123125609338146.
The zero mode is unique; the first positive gap is 0.2373539058 in **dimensionless chosen-graph units**, not a particle mass. Every bridge class is essential for connectivity of the original 190-cell tree: deleting it yields two disconnected components. A tetra-vertex impulse under exp(-tK) activates all five solids, edges/faces, histories and clock.

## Hidden sector stays protected by *linear* contact
Every history selects exactly six icosahedral vertices and has exactly 12 occupied Golay coordinates, so its degree grows by 18. The history diagonal of K is H_8+18I. The existing hidden isometry has zero overlap with both contact matrices, giving **exactly**
K J_h P_3=36 J_h P_3; K J_h P_5=34 J_h P_5
where J_h inserts U_h into the 64 history coordinates of the 278-space. Numerical invariance residual 3.11e-14. The old embedded rho_star therefore COMMUTES with this linear K, but is *not* the global Gibbs state of all 278 coordinates. This is a testable protected-channel theorem for the explicitly defined network.

## Nonlinear return and all-cogs shifts
Keep the previous fixed Delta = 3/20-80pi/(1053phi) = 0.0024891898404204027. Let x be the 190-cell state, y the 64-history state; let B (12x20) be the unsigned icosahedral vertex-to-face incidence, x_I the icosa vertex portion, and
h_3=P_3[(B^T x_I)⊙(B^T x_I)], h_5=P_5[(B^T x_I)⊙(B^T x_I)].
On the full z=(x,y,c24), choose
V(z)=1/2 z^T K z+1/4(||h_3||²+Delta²||h_5||²)-y^T U_h(h_3+Delta h_5).
The chosen cubic and quartic terms are the prior all-five/H64 constructive contact. Because the hidden carriers have full-network energies 36 and 34, eliminating them by exact completion of the square yields coefficients

c_3=1/4-1/(2·36)=17/72; 
c_5/Delta²=1/4-1/(2·34)=4/17.

The previously separate all-five/H64 action had coefficients 2/9 and 7/32; therefore **turning on the other contacts changes the history feedback**, even though Delta remains frozen. Full-network gradient flow from one tetra vertex gave a nonzero hidden-P3 amplitude 3.70e-10 at t=0.2 and 2.46e-10 at t=1.0; the hidden-P5 amplitude 3.60e-12 at t=0.2. These are dimensionless illustrative amplitudes, not measured masses or couplings.

## Nonuniqueness gate
The 24-coordinate linear readout has a canonical 13/51 split in this specified six-axis Golay construction, but **there is no proof that a cyclic graph on the 24 coordinate labels is a selected physical time operator**. Reordering the cycle can change the bulk spectrum; in a fixed seeded permutation test the spectral maximum pointwise difference is 1 although the lowest gap is unchanged. The nearest-direction gluing between solids is also a declared construction. Neither is uniquely selected by the original URT q=(pi/e) exp(i 2pi/phi²) or the full microscopic source-loaded T_star.

## Reproducibility
The executed conversation artifacts are `cathedral_whole_machine_2026_10_29.py`, `cathedral_whole_machine_278_2026_10_29.py` and their respective JSON result files. Run both with NumPy and SciPy, with the files side-by-side. The scripts assert exact incidence and history identities to numerical precision, the Golay Gram spectral theorem, full-network connectedness, hidden invariance, Schur coefficients and dynamical response.

**Claim:** rigorous combinatorial rank identities and a completely specified/executed candidate whole-network model. **Not claimed:** unique or physical selection of the intersolid and 24-cycle couplings, all Cathedral sectors already dynamical, or predictions of physical constants.
