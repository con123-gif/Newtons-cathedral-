# Cathedral 190D → 64D → 8D: double-gap transfer theorem (29 Oct 2026)

**Status:** Exact finite-dimensional *constructed model*, not a verified unique Golay/URT dynamics or physical theory. All equations below independently verified using exact SymPy matrices. The identification of corresponding face states across two 20-state history sheets is a stated geometric choice; no experimental values or fitted coefficients are used.

## The verified operator bridge

Construct oriented boundary matrices on all five Platonic solids. The total Hodge space has dimension 190 and its Hodge–Dirac operator obeys

- `Tr D² = 720`
- `Tr D⁴ = 3456`.

The icosahedral face block of `D²` is exactly `L_F=3I20-A_D`, the dodecahedral graph Laplacian. Its unsigned vertex–face incidence `B` has rank 12 and hidden kernel `H8=ker B=4_3⊕4_5`, with orthogonal projectors `P3,P5` of rank 4, obeying `L_F P3=3P3`, `L_F P5=5P5`.

Now use the explicitly specified 64-dimensional carrier

`H64=V_A(12)⊕V_B(12)⊕F_A(20)⊕F_B(20)`.

The first vertex copy plus the normalized invariant singlet of the second has dimension 13; its orthogonal complement has dimension 51. The 13-cell centred Laplacian and the residual 11D vertex Laplacian can be assembled within these two vertex copies.

Match corresponding faces across the two 20-state sheets by one unit-weight link per face. The face transfer generator is

```
K_F = [ L_F + I20    -I20    ]
      [ -I20          L_F + I20 ]
```

The full resulting 64×64 positive-semidefinite generator `K64=K_vertex⊕K_F` preserves the 13/51 split and satisfies `Tr K64=304`, `Tr K64²=1820`.

Define diagonal and anti-diagonal isometric embeddings `J±(h)=(h,±h)/√2`. They obey the exact intertwining identities

`K_F J+ = J+ L_F`, `K_F J- = J- (L_F+2I)`.

Consequently, `exp(-t K_F)J+ = J+exp(-t L_F)`: this is an actual transfer-compatible map from the Hodge face block to the 64-state face copies.

## Minimum-energy embedding selection

For an isometric map `Φ:H8→H8_A⊕H8_B`, the unit-link energy is `E(Φ)=||Φ_A−Φ_B||²_HS≥0`. Its minimum 0 occurs precisely when the two sheet maps coincide. Therefore the **range** of the minimizer is uniquely the diagonal 8D hidden subspace `J+(H8)`. It leaves internal intertwiner basis freedom and does not independently establish that the Golay action chooses this link energy.

## Exact double-gap heat state

The 16D doubled hidden sector decomposes into four rank-four spectral projectors with eigenvalues

- `(3,+):3`
- `(3,−):5`
- `(5,+):5`
- `(5,−):7`

Thus `spec K16={3×4,5×8,7×4}`. Both elementary splittings equal 2: one from the face eigenvalues 3/5, the other from the two-sheet Laplacian 0/2.

With `q=e^(−2t)`, the exact normalized heat state is

`ρ16=[P3,+ +q(P3,−+P5,+)+q² P5,−]/[4(1+q)²]`.

It factorizes into a uniform 4D representation and two identical binary states with populations `(1,q)/(1+q)`. Tracing out the sheet gives

`ρ8 = (P3+q P5)/[4(1+q)]`.

At the frozen Cathedral `t=ηΔ=−lnΔ`, `q=Δ²`, and this is **exactly** the pre-existing eight-state master state. Entropies:

`S16/kB=ln4+2 H2(p)`, `S8/kB=ln4+H2(p)`, `p=q/(1+q)`.

## Three-level exchange-symmetric tower

On the 4D multiplicity factor `C²_hidden⊗C²_sheet`, the energies are `3,5,5,7`. Since the two binary gaps match, exchanging the factors commutes with the Hamiltonian. The symmetric subspace `Sym²(C²)` has exactly three distinct levels, `3,5,7`, with weights `1:q:q²=1:Δ²:Δ⁴`. The antisymmetric singlet has energy 5 and probability `q/(1+q)²` in the full heat state.

**Status boundary:** This constructs three mathematical history levels, not three physical lepton generations or their masses. The symmetric exchange is a property of this explicit doubled-gap realization; a Golay history operator selecting the construction and a physical chiral mass/gauge action still have to be derived.

Exact standalone verification code for this theorem was produced in the same research session as `cathedral_64_history_double_gap_2026_10_29.py`.
