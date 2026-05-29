# Analysis & Findings — "Newton's Cathedral" / URT‑Enhanced v2.0

**Date:** 2026-05-29
**Scope:** `newtons_cathedral/` package, `cathedral_v8_complete.py`, `README.md`,
`docs/DERIVATION.md`, and the mirror snapshot in the `Newtons-cathedral-` repo.

This report separates two questions that the project conflates:

1. **As software / mathematics** — is the code correct, tested, and internally consistent?
2. **As physics** — does it actually *derive* the constants of nature "from D = 3 alone,
   with zero free parameters," as claimed?

The short version: **(1) is largely yes; (2) is no.** The repository is a clean,
well-engineered numerology engine. What it demonstrates is curve-fitting with a large
hidden discrete search space, not a parameter-free derivation of physics.

---

## 1. What is solid

These parts are correct and worth acknowledging:

- **The group theory is real.** Finite subgroups of SO(3) (Jordan): {Cₙ, Dₙ, A₄, S₄, A₅};
  A₅ is the unique non-cyclic simple one. Icosahedral counts V=12, E=30, F=20, |A₅|=60,
  Euler χ = V−E+F = 2. The kissing-number coincidence K(D)=D+D² holds for D∈{1,2,3}
  (K=2,6,12). All correct.
- **The graph/spectral math is real and correctly computed.** G₁₃ Laplacian spectrum
  {0,3,5,7,9,13}, heat-kernel trace, Cheeger constant 7/3, Ollivier–Ricci κ>0 (LP
  Earth-Mover), Ramanujan check, Betti numbers, Hodge decomposition — these are genuine,
  reproducible computations.
- **The engineering is good.** Modular, typed, documented; 138 tests pass and
  `all_audits_pass()` returns `True`. Clean greenfield structure.

None of this is in dispute. The problem is the leap from "here is some nice icosahedral
mathematics" to "therefore these are the constants of nature."

---

## 2. The central claim does not hold: "zero free parameters" is false

The headline is *zero free parameters; only input is D=3.* This is incorrect in two
independent ways.

### 2a. Hidden discrete degrees of freedom (the real free parameters)

Each observable gets its **own bespoke formula** assembled from a large alphabet:

- integers `{D,q,V,E,F,G,N,1,2,...}` and their products/sums/differences,
- constants `{π, φ, e, γ, δ★, δ_cl, Δ, η}`,
- free choice of operations, exponents, and **integer "correction coefficients."**

The "no continuous fit parameter" claim hides the fact that *choosing the formula* is the
fit. A concrete, reproducible demonstration — the muon/electron mass:

```
m_μ/m_e = D·(G+D²)·(1 − k·η/N),   bare = 207,  target = 206.7682830
   k= 8 → 206.8457  (0.037%)
   k= 9 → 206.8264  (0.028%)
   k=10 → 206.8072  (0.019%)
   k=11 → 206.7879  (0.009%)
   k=12 → 206.7686  (0.000%)   ← the value shipped in the code
   k=13 → 206.7493  (0.009%)
```

The coefficient `12` is not derived — it is the integer that minimizes the error. That is
a fitted parameter wearing an integer costume. The same pattern (`11·η/N`, `2q·η`, `8/9`,
`32/9`, …) recurs throughout `fermions.py`, `cosmology.py`, `qcd.py`, `baryogenesis.py`.

### 2b. Documented post-hoc "residual-closing" correction factors

The code's own docstrings admit fitting. From `chain.py`:

> `Λ_QCD … secondary (1 − γ·D/E) QCD-scheme correction; closes residual from +0.114 %
> to −0.009 % vs PDG 210 MeV.`

> `The (1 − Δ) factor in v_EW … shifts every mass by ~0.25 % which is exactly the residual
> seen without this factor.`

Adding a factor specifically because it cancels the leftover gap to the measured value is
the definition of curve-fitting, not derivation.

### 2c. Real dimensional inputs are smuggled in

"Zero external dimensional input" is contradicted by the code:

- `cathedral_v8_complete.py` hardcodes `m_e = 0.5109989461e-3 GeV` and `v_EW = 246.22 GeV`
  (commented "Reference … used as unit conversions") and uses `v_EW` directly to produce
  m_W, m_Z, m_H. Those are empirical inputs.
- `chain.py` is more honest: it states the chain needs **one measured input**, the
  cosmological-constant density `ρ_Λ = (2.34 meV)⁴` (Planck 2018), from which M_Pl, v_EW,
  m_e, m_p follow. That is one external dimensionful anchor — fine, but it directly
  contradicts the "zero external input / mass anchor is purely internal" marketing.
- `M★ = 4π√2 ≈ 17.77` is declared an internal mass anchor and then asserted to be
  "≈1.777 GeV in units where m_τ = 0.1·M★." That last step uses the measured τ mass to set
  the unit — circular.

---

## 3. The "predictions" are mostly retrodictions with adjustable structure

- **Integer "predictions" are nearest integers to known data**, chosen from many candidate
  integer combinations: `m_H = q^D = 125` (PDG 125.25), `m_top = (N+1)V+q = 173`
  (172.69), `δ_CP = (D+1)F+(N−D−1)N = 197°`. There is no mechanism forcing *these*
  combinations over the combinatorially many others that land equally close.
- **No look-elsewhere accounting.** With ~9 integers, ~6 transcendental/derived constants,
  and free arithmetic, the density of expressions landing within 0.1 % of any O(1)–O(10³)
  target is high. The quoted "median error 0.042 %, 47 predictions" has no error model and
  no penalty for the size of the search space that produced each formula.
- **Tautological tests.** The pytest suite and `*_audit()` functions compare each closed
  form to a *hardcoded experimental target* within a tolerance chosen after seeing the
  data (e.g. `abs(ALPHA_INV_FULL − 137.035999084)/… < 2e-7`). Passing means "the constant I
  fitted still equals the number I fitted it to." Green tests here are not evidence for the
  physics.

---

## 4. Internal inconsistencies (a forced theory would not have these)

If every number were truly forced, the same observable would have one formula. It does not:

| Observable | `cathedral_v8_complete.py` | `newtons_cathedral/` package |
|---|---|---|
| Ω_m | `4/13 = 0.3077` (2.6 % off) | `(D+1)/N·(1+2γ) = 0.3153` (0.16 %) |
| Axion mass | `δ★/|R_mass|·1e3 ≈ 58.2 µeV` | `60.8 µeV` (README) |
| H₀ ratio | `1 + 2D/(Fπ) = 1.0955` | `N/V = 1.0833` (README "canonical") |
| Ω_Λ | `9/13 = 0.692` | `1 − Ω_m = 0.6847` |

`cosmology.py` even keeps two H₀ formulas and labels one "canonical" — i.e. the closer one
was selected after comparison to data. These are choices, not derivations.

---

## 5. Physics-correctness problems beyond the fitting

- **Scheme/scale dependence ignored.** α_s, quark masses (m_u…m_t), Λ_QCD, sin²θ_W and
  1/α(M_Z) are renormalization-scheme- and scale-dependent. Quoting a single dimensionless
  closed form for, e.g., the MS̄ "current" light-quark masses or α_s(M_Z) without a scheme
  or running is physically ill-defined; the "target" numbers themselves are convention-laden.
- **Ω_m = 4/13** ignores radiation/neutrino contributions and the actual flat-ΛCDM budget;
  the clean ratio is aesthetic, not physical.
- **"Consciousness integration proxy"** in `run_urt()` (a mean/std ratio of 4 random-init
  graph values) is presented alongside physics observables. This is not a measurable
  quantity and signals the project's epistemic stance.
- **Falsifiable predictions are wide bands** (axion 50–100 µeV, WIMP 10–20 GeV, microwave
  1–30 GHz) — low falsification power; almost any future null result can be accommodated.
- **No peer review, no derivation of dynamics.** The "Lorentzian signature derived from K₄"
  and "Sakharov–Visser gravity" sections relabel graph-Laplacian eigenvalues as a metric
  signature; they do not produce field equations with predictive, independently-checkable
  content beyond the spectral facts already noted in §1.

---

## 6. Why the matches look impressive but are not evidence

The persuasive force comes from (a) many digits quoted, (b) green tests, and (c) elegant
integers. But:

- digits come from fitted correction terms (§2),
- tests compare fits to their own targets (§3),
- the integers are selected post-hoc from a large pool (§3), and
- the framework freely switches formulas to whichever fits (§4).

A genuine parameter-free theory makes **a** prediction for **each** quantity, *before*
looking, with a single fixed formal apparatus, and is then exposed to falsification with a
proper trials/error model. This project does the opposite: it fixes the answer and searches
the (large) expression space for a closed form that reproduces it.

---

## 7. Recommendations

If the goal is honest scientific work rather than persuasion:

1. **Pre-register.** Fix the *entire* formula-generating grammar and the selection rule
   (e.g. "smallest expression in these symbols") *once*, then derive every constant with no
   per-observable choices. Report every miss, not just the hits.
2. **Quantify the look-elsewhere effect.** Enumerate how many expressions under your grammar
   land within tolerance of each target; report the effective trials. This is the single most
   important missing number.
3. **Drop the "zero parameters / zero input" language.** State plainly: D=3 + icosahedral
   symmetry + **one** dimensional anchor (ρ_Λ), plus a chosen expression grammar. That is
   defensible; the current framing is not.
4. **Stop adding residual-closing factors.** Either a term is independently motivated or it
   is a fit; the docstrings currently admit the latter.
5. **Make tests non-tautological.** A test that a fitted constant equals its fit target is
   not a test. Tests should check independent, derivable relations, not re-assert data.
6. **Respect scheme/scale.** For running quantities, specify scheme and scale or don't quote
   single numbers.
7. **Keep §1.** The icosahedral graph mathematics is genuinely nice and could stand on its
   own as recreational/structural mathematics without the physics overclaim.

---

## 8. Bottom line

- **Software:** clean, tested, reproducible. ✔
- **Mathematics (group/graph theory):** correct. ✔
- **Physics claim ("all constants from D=3, zero free parameters"):** not supported.
  The "zero parameters" rests on (i) a large hidden discrete search over formulas and
  integer coefficients, (ii) explicitly documented post-hoc correction factors, and
  (iii) at least one real dimensional input (ρ_Λ, or hardcoded v_EW/m_e). The matches are
  retrodictions produced by curve-fitting with an unaccounted look-elsewhere effect, not
  parameter-free predictions. ✘

This is best characterized as **physics numerology**: mathematically literate, internally
tidy, aesthetically appealing, and not evidence for a theory of nature.
