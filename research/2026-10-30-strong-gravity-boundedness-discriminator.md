# Strong-field gravity test of URT recursive bounding (30 Oct 2026)

**Status: constructive physical diagnostic, not a derived new gravity theory.** Tested actual nonlinear Einstein equations with two distinct regular bounded-energy profiles. Both have the same density cap, de Sitter core and asymptotically Schwarzschild exterior, **but different horizon thresholds by 47.82%**. URT's boundedness alone therefore does not determine the physical gravitational response law.

In geometrised units G=c=1, use a total gravitational mass M, enclosed mass m(V), proper areal-volume coordinate V=4πr³/3 and a density cap rho_c=3/(8π ell²). The undetermined length ell is *not* derived from microscopic URT. Consider the candidate symbiotic saturated-source law

    d(m/M)/dV = (rho_c/M) [1-m/M]^p,   m(0)=0.

Its residual exponent p is an explicit new **physical hypothesis**, not a theorem of the old URT contraction.

**Quadratic feedback p=2:** Integrating gives m(r)=M r³/(r³+2M ell²). Einstein's spherical metric f(r)=1-2m(r)/r is exactly the known Hayward regular-black-hole solution, not novel. Effective stress tensor: rho=3 M² ell²/[2π(r³+2M ell²)²], p_r=-rho, p_t=3M²ell²(r³-Mell²)/[π(r³+2Mell²)³]. The r→0 core has f=1-r²/ell²+O(r^5), Ricci scalar 12/ell² and Kretschmann 24/ell^4, all finite. The r→∞ exterior has f=1-2M/r+4M²ell²/r⁴+… . Radial NEC saturates, tangential NEC holds; strong energy condition is violated for r³<Mell², permitting a finite core.

Horizon equation: r³-2Mr²+2Mell²=0. Critical double root at rcrit=√3 ell, Mcrit=3√3 ell/4 ≈ **1.299038105676658 ell**. For M=2ell, horizons r-/ell=1.19393656647, r+/ell=3.70927535944, and dimensionless Hawking temperature Tell=0.0167758164755. This is a static exact spacetime, not a dynamical collapse calculation.

**Linear feedback p=1:** Equally bounded source law instead integrates to m(r)=M[1-exp(-r³/(2Mell²))] and rho(r)=rho_c exp(-r³/(2Mell²)). This also has R(0)=12/ell², Kretschmann(0)=24/ell^4 and Schwarzschild exterior. Its extremal horizon solves e^x=1+3x, xcrit=1.90381369444, giving Mcrit/ell=**0.878794537877033**, rcrit/ell=1.49570953991.

**Decisive comparison:** same physical bounding, same central curvature and same 1/r exterior, but different horizon threshold by **47.8204574%**. Generic URT boundedness cannot uniquely identify gravity or select its black-hole physics. The physical task is to derive the actual energy-loaded radial source and cap from the complete history/geometry transfer, including its stress-energy response and conserved Ward constraints. The full Cathedral is not reduced to these spherical examples.

All symbolic identities (Einstein density/stresses, curvature, exact ODE) and numerical horizon checks were executed. Source and JSON results are delivered as conversation artifacts in `Cathedral_Strong_Gravity_Decisive_Test_2026-10-30.zip`.

Known-source acknowledgement: Sean Hayward (2006), *Formation and Evaporation of Nonsingular Black Holes*, Physical Review Letters 96 031103, https://doi.org/10.1103/PhysRevLett.96.031103.
