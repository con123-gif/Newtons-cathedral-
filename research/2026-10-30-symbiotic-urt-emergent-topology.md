# Symbiotic URT: topology generated from history feedback — 30 October 2026

The reciprocal history↔geometry generator in `research/2026-10-30-symbiotic-urt-history-geometry.md` begins with all N(N-1)/2 links **equal**, with the six-axis history Hamiltonian supplying the only distinction between history labels.

Take the simple, explicitly defined structural readout: retain a link if its final strength is greater than the initially uniform baseline B/E, where B=N-1 is the graph edge budget and E=N(N-1)/2. No parity target or spatial coordinates are used by this readout.

**Computed, verified for N=16, 32, 64:** the selected links are precisely those joining bitstrings at even Hamming distance. Thus the graph splits into two complete parity sectors, `K_(N/2) ⊔ K_(N/2)`. This matches the two zero modes of the underlying pair-flip history Hamiltonian. It recovers an *existing* protected history symmetry by a reciprocal geometric selection rule; it does not independently discover that symmetry or demonstrate a physical 3D space.

Generate the simplicial 2-skeleton by using selected edges and all triangles formed by selected triples. Orient edges and triangles by ordered labels: ∂2[a,b,c]=[b,c]-[a,c]+[a,b], ∂1[a,b]=[b]-[a]. Then ∂1∂2=0 identically. For the computed graphs:

| N | components | edges | triangular faces | rank ∂1 | rank ∂2 | β0 | β1 | β2 of the 2-skeleton |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 2 | 56 | 112 | 14 | 42 | 2 | 0 | 70 |
| 32 | 2 | 240 | 1120 | 30 | 210 | 2 | 0 | 910 |
| 64 | 2 | 992 | 9920 | 62 | 930 | 2 | 0 | 8990 |

The 16-history chain boundary identities and ranks were also checked using explicit integer matrices. The general counts follow from the combinatorics of two complete graphs.

**Critical limitation:** The enormous β2 is an artifact of stopping the clique complex at dimension 2; in the *full flag complex*, the two components are simplices and have no positive-dimensional homology. These are not two 2-spheres, nor the five Platonic solids, nor physical gravitational degrees of freedom. The threshold w>initial uniform is a meaningful but chosen geometric readout, not yet a uniquely derived microscopic selection rule.

**New insight for the Cathedral programme:** a positive history operator can feed back to select links; selected links can generate consistent boundary operators and hence a Hodge–Dirac complex; but URT still needs an intrinsic rule choosing *which cell dimensions survive*. That dimensional closure, as well as oriented 24-clock holonomy, must be part of the enlarged symbiotic recursion rather than supplied after it. The program is **constructive mathematics, not experimentally verified physics**.