# URT recursive bounding selects a candidate golden holonomy — 30 Oct 2026

**Status: exact new projective-recursion theorem and a constructed Wilson selection model; not a proven consequence of the historical URT source operator or experimental reality.** Full executable verification: conversation artifact `Cathedral_Recursive_Bounding_Holonomy_2026-10-30.zip`.

## Primitive binary recurrence and its fixed point

Among 2x2 matrices with entries in {0,1}, determinant ±1, and primitivity (some strictly positive power), only `[[1,1],[1,0]]` and its relabeling `[[0,1],[1,1]]` qualify. Their eigenvalues are `phi` and `-phi^-1`, matching the previously found D6->H3 conjugate pair. This is an exact classification, but **choosing minimal binary primitivity as the microscopic URT rule is new dynamical input**.

The projective Fibonacci ratio iterates by

`x_0=0, x_(n+1)=(1-x_n)/(2-x_n)`, with `x_n=F_n/F_(n+2)`.

On [0,1/2] it is a contraction with Lipschitz bound 4/9, hence its unique fixed point is `x*=(3-sqrt(5))/2=phi^-2`. Consecutive rational iterates bracket the irrational with exact gap `1/(F_(n+2) F_(n+3))`. At n=24, `x24=46368/121393`, error `3.03478353558e-11`, so the terminal Wilson phase `2pi x24` differs from `2pi/phi²` by `1.906808e-10` rad. This is a 24-step readout, **not** an identification with the older q_URT per-link phase.

Control: positive unimodular substitution with larger integer entries such as `[[2,1],[1,0]]` selects a silver irrational. Recursive boundedness alone is insufficient: minimal binary primitivity is the selector hypothesis.

## Archived URT contraction and a gauge-compatible extension

The historical URT controlled fibre is `P_(n+1)=beta[alpha(P_n-theta_H Phi(P_n))+u_n]`, historical defaults `alpha=1.155,beta=.235,theta_H=2.4`, coarse contraction `beta alpha(1+theta_H)=.922845<1`. To preserve U(1) phase, the newly specified equivariant bounded nonlinearity is `Phi(z)=z/(1+|z|)`, driven by the **recursively selected** `u_n=(pi/e)exp(2pi i x_n)`. Multiple complex starting points converge to the same fixed phase `2pi/phi²`; the radial fixed value for those historical coefficients is `0.214726868598248`. The original archived real sin/sign branch is not equivalent to the new complex radial extension without proof. The phase depends on the projective Fibonacci selection, not on fitting measured electromagnetic alpha.

## Relative history phase survives positive transfer

Let M be the nonzero chronological 3->3' matrix. Two coherently prepared histories with relative phase from the bounded selector give

`C_n(Theta)=M+exp[i(Theta-2pi x_n)]M`, `T_n=C_n†C_n>=0`.

The normalized source weight is exactly `R_n(Theta)=Tr(T_n)/(4Tr(M†M))=cos²[(Theta-2pi x_n)/2]`; its maximum is at the selected phase. Only relative histories can carry this phase through B†B. **The two-path equal-amplitude coherent preparation and conditioning are newly postulated, not yet derived from the full 64-history microscopic B*.**

## Full five-solid thermal test

For `Z_selected(Theta)=Z_whole(Theta) R_24(Theta)`, with the previous 190D five-solid Hodge, coupled 64-state history, 24-track clock and both harmonic and 30-mode dipole bridges, numerical minimization yields stable local equilibrium `Theta_eq=2.364902132072154 rad=135.4989111292244 deg` with curvature `0.08049278177324481>0`. The intrinsic selected phase is `137.50776405003785 deg`. At zero phase the normalized selector contributes free-energy penalty `0.3385957956124188`, overwhelming the thermal difference `V_th(golden)-V_th(0)=0.007100157997985` **for the conditioned ensemble**. This reverses zero-holonomy selection without fitting an observable.

However, normalizing the history readout removes the absolute suppression of the unconditioned positive 64-history propagation. The historical source-loaded instrument has not been proven to use this conditioning, nor has it forced the minimal primitive Fibonacci substitution. Those are the two priority derivations. No claims of direct physical evidence are made.

**Bundle:** `Cathedral_Recursive_Bounding_Holonomy_2026-10-30.zip` (conversation artifact) contains the full note, exact script, numerical thermal test, and dependencies.
