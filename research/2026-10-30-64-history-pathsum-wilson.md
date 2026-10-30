# Exact 64-history path sum and chronological Wilson sewing — 30 Oct 2026

**Status:** Exact finite/operator mathematics for the specified models; hypothetical gravitational/physical identification. Full code and extended research note delivered in the conversation as `cathedral_history_pathsum_completion.py` and `CATHEDRAL_64_HISTORY_PATH_SUM_2026-10-30.md`.

## Two distinct 64-dimensional machines (do not conflate)

(1) Six-bit URT binary-history carrier `Hbits=15I64 - Σ_{0<=i<j<6} X_i X_j = 18I - (Σ X_i)^2/2`. Its exact spectrum is `0(x2), 10(x12), 16(x30), 18(x20)`.

(2) Coupled 12+12+20+20 vertex/face `K64`, the 2026-10-29 history/hybridization construction. Its chiral `3,3'` vertex/face blocks are `K3=d3 I2+v3 σx`, `K3p=d3p I2+v3p σx`, with `d3=5-√5`, `d3p=5+√5`, `v3²=(5+2√5)/15`, `v3p²=(5-2√5)/15`. **No intertwiner proving equivalence between these two 64D objects has been supplied.**

## Theorem A: exact 64-history-to-24-track path sum

For the existing 64×24 antipodal-icosahedron readout G, let `C=2G-J_(64,24)`. Integer identities are `Hbits C=10 C`, `Hbits J=0`, `Jᵀ C=0`.

Therefore, for every `t≥0`,

`Gᵀ exp(-t Hbits) G = 16 J24 + exp(-10t)(GᵀG-16J24)`.

`spec(GᵀG) = {384(x1),32(x12),0(x11)}`, and hence the **exact** returned spectrum is `{384(x1), (32e^(-10t))(x12),0(x11)}`. At frozen `t=η=-log Δ`, `Δ=3/20-80π/(1053φ)`, its 12 contrast eigenvalues each equal `32Δ^10=2.9223361864073×10^-25`. Thus the 64-bit history path sum strongly preserves one common track mode while suppressing contrasts. It is real and cannot alone induce a nontrivial complex holonomy.

## Theorem B: 24-link path integral with actual coupled-K64 chiral energy

Let the two-sided positive bilinear history generator on `Hom(3-sheet,3'-sheet)` be `Hhom(X)=K3p X + X K3`. Exact spectrum: `μ_{s,t}=10+s v3+t v3p`, `s,t=±1` (each ×9 on the 36D bilinear). Numerical distinct levels: `9.017753053623, 9.392938001793, 10.607061998207, 10.982246946377`. The five-orientation chronological source `M=P3' T5(1)P3` has `S=Tr M†M=0.02827748405946`; its vertex-to-vertex sheet injection places exactly 1/4 of the squared norm in each of four channels.

Specify a local Euclidean 24-link action on a clock circumference `ℓ`, `a=ℓ/24`:

`E= a^-1 Σ_{j=0}^{23} |z_(j+1)-u_j z_j|² + a Σ_{j=1}^{23} μ|z_j|²`.

Integrating/minimizing the intermediate 23 fields gives exact boundary Green coefficient `b(x)=sinh(arcosh(1+x/2))/sinh(24 arcosh(1+x/2))`, `x=a² μ` (limit `b(0)=1/24`). The six all-five-solid dipole sewing lanes then give the complete phase-dependent potential

`V_sew(Θ;ℓ)=C(ℓ)[1-cos(Θ-2π/φ²)]`,
`C(ℓ)=12S/ a × [Σ_{s,t} b(a² μ_{s,t})/4]`.

This is the explicitly history-propagated replacement for the former **unpenalized** coefficient `12S/24=0.0141387420`.

## Full bulk-Cathedral thermal comparison and derived threshold

Reconstructed full five-solid Hodge/64-history/24-clock block trace:

`V_th(0)=-1.3389373765014974`, `V_th(2π/φ²)=-1.3318372185035126`, difference `0.007100157997985`.

Endpoint preference equality is precisely `C(ℓcrit)(1-cos(2π/φ²)) = 0.007100157997985`, with numerical root

**`ℓcrit=1.99755450498253` (internal units)**.

For `ℓ=2π`, the natural angular-clock circumference, `C=1.18474540275×10^-8`, and the sewing preference for golden rather than zero is `2.05833979119×10^-8`, only `2.8990×10^-6` of the thermal penalty. For `ℓ=1`, `C=0.09186547`, and golden beats zero. The threshold compares **two endpoints**, not automatically actual stationary points, a phase-transition theorem or a compactification-length prediction. The physical length and relative action normalisation have not yet been independently fixed.

## Alternative conditional/unitary transport

The same D6→H3 signed rates `φ,-φ^-1` rotate nonzero `M` by `e^{i√5 t}`. After `t*=2π/φ`, phase is `e^{i2π/φ²}`. For `F=exp(-a Hhom) exp(i√5 t*/24)`, its exact polar/unitary factor is `U=exp(i√5 t*/24)`. Transporting by U preserves the golden phase without the positive-history attenuation; recovering the previous `1/24` strength requires using a **conditional/unitary connection**, which the present microscopic model does not force. The positive history sum and polar normalized transport are not interchangeable physical dynamics.

## Verification and next physical discriminant

Standalone Python source reconstructs both 64-history operators, G and its 24-column spectrum, and the actual fivefold chronological matrix; verifies exact G heat-identity at several t, direct inverse of all 23×23 tridiagonal matrices, chiral spectra, full five-solid thermal trace, ℓcrit, and polar unitary.

**Next discriminant:** derive whether the URT selection functional transports chiral amplitudes using positive Euclidean weights or a norm-conserving polar/unitary connection; then derive the proper clock circumference and relative action scale. Without that input, the previously reported stable 123.29° vacuum does not follow from the actual positive history path sum at ℓ=2π.