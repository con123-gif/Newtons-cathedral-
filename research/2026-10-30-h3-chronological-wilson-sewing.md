# Cathedral: chronological H3-to-Wilson sewing — 30 Oct 2026

**Status:** exact mathematics of a *specified new local action*, numerical full-geometry test, **not** an established physical theory. Full executed code/research bundle is a conversation artifact `Cathedral_History_Clock_Sewing_2026-10-30.zip`.

## 1. The chronological mixing matrix produces the golden return phase

Use the existing five-orientation 3-by-3 mixing block `M=P_3' T_5(1) P_3`, with nonzero singular values approximately (0.12811926, 0.08432134, 0.06894092), and the D6-to-H3 signed generators
`H_f=phi I_3`, `H_s=-phi^-1 I_3`, `phi=(1+sqrt(5))/2`.

The two-sided transport is

`M(t)=exp(-it H_s)M exp(it H_f)=exp(i sqrt(5)t) M`.

After a complete fast cycle `t*=2pi/phi`, the exact identity `sqrt(5)/phi=1+phi^-2` gives

`M(t*)=exp(i 2pi/phi²) M`.

Thus `Tr[M†M(t*)]/Tr[M†M]=exp(i 2pi/phi²)`. This extraction does not assume a golden Wilson loop. It **does** assume the H3 representation eigenvalues are physical history rotation frequencies and the chronological matrix supplies an actual cross-representation readout.

At the canonical (but not uniquely Stinespring-selected) choice `g=1`, the exact chronological norm is

`S=Tr(M†M)=q³/(1-q)^5 * [3q²-495q/128+45/32]`, `q=tanh²(2/sqrt(15))`,

numerically `S=0.028277484059460196`.

## 2. A *local* 24-step positive quadratic sewing energy

With 24 U(1) clock links `u_j` and Wilson loop `W=prod(u_j)=exp(i Theta)`, introduce history matrix fields `z_j`, endpoints `z_0=M`, `z_24=M(t*)`, and the gauge-covariant energy

`E_chain=sum_{j=0}^{23} ||z_{j+1}-u_j z_j||_F²`.

Sitewise gauge covariance holds with `z_j→exp(i chi_j)z_j`, `u_j→exp(i(chi_{j+1}-chi_j))u_j`, `chi_24=chi_0`.

Gauge-transform the interior by cumulative link products. Cauchy–Schwarz proves the **attained minimum**

`min E_chain = ||M(t*)-W M||²_F/24 = 2S[1-cos(Theta-Theta_H)]/24`,

where `Theta_H=2pi/phi²`. Thus a nonlocal Wilson-loop potential is derived by eliminating variables from local positive quadratic differences.

The existing 30D *all-five-solid* vertex/face dipole space has six coordinate channels (vertex and face, each with x,y,z). Choosing identity sewing on those six channels gives

`V_bridge(Theta)=(6/24)*2S[1-cos(Theta-Theta_H)]`
`=0.014138742029730098*[1-cos(Theta-Theta_H)]`.

The six-channel unit coupling is an explicit geometric dynamical **postulate**, not a unique consequence of URT.

## 3. Competing with the FULL pre-existing bulk-bridged Cathedral thermal trace

Use the actual 190D five-Platonic Hodge operator D, coupled K64, 24 positions, and the harmonic/dipole C_top+C_bulk couplings. Its block-reduced full partition function is `Z(Theta)=Tr exp[-eta K_new(Theta/24)]` with frozen `eta=-log Delta` and `Delta=3/20-80pi/(1053phi)`.

Take `V_total=-(log Z)/eta+V_bridge`. Executed full block-spectrum results:

- `V_th(0)=-1.338937376501498`
- `V_th(Theta_H)=-1.3318372185035128`
- `V_bridge(0)=+0.024564210377630968`
- `V_bridge(Theta_H)=0`
- stable stationary point `Theta_eq≈2.15177697 rad=123.28774°`
- `V_total(Theta_eq)≈-1.33218912195410`
- `V_total''(Theta_eq)≈0.01149695>0`.

The golden history phase **moves the clock away from the trivial thermal vacuum**, but in this combined action the actual equilibrium is **not exactly golden**: the thermal sector shifts it about `-0.24818626 rad`.

With the earlier Wilson kinetic term `(f²/48)(∂Theta)²`, the dimensionless linear oscillation coefficient is `omega*f=sqrt(24 V_total'')≈0.52528747`. Scale `f` remains uncalculated.

### A new channel threshold

For `m` independent dipole sewing channels, the preference between `Theta=0` and `Theta=Theta_H` reverses at

`m_crit=24[V_th(Theta_H)-V_th(0)]/[2S(1-cos Theta_H)]=1.7342689764`.

The full geometry supplies six channels, above threshold. Keeping six channels, the chronological coupling threshold in the same setup is numerically `g≈0.81567`; canonical `g=1` exceeds it. Neither threshold was obtained by fitting experimental data.

## 4. Distinctions that matter

1. The historical URT multiplier `(pi/e) exp(i 2pi/phi²)` has that phase on **each clock step**. The new fast-cycle transport produces `Theta_H=2pi/phi²` for the **entire loop**. These are different histories unless a one-period-per-link vs one-period-per-loop map is derived.
2. The chronological mixing and full thermal free energies are both input to the specified action. Their relative unit weighting, treatment of the sewing fields, and H3 frequency interpretation require derivation from microscopic URT rather than declaration.
3. This produces a classical effective Wilson scalar potential, not a measured electron mass, fine-structure constant, 5D gravitation, or experimental proof of physical reality.
4. All five Platonic solids enter the full thermal operator, while the history sewing couples explicitly through the six collective dipole channels; the remainder is not yet dynamically sewn to that H3 transport.

## Reproducibility

Executed `cathedral_history_clock_sewing.py` tests the actual fivefold chronological matrix, golden normalized overlap, full 24-step local minimization by explicit intermediate matrices, gauge covariance, thermal partition, stationary points and curvature. The script is bundled with `cathedral_bulk_wilson_dynamics.py` and `cathedral_synchronous_engine.py` so it runs without missing dependencies from earlier work.