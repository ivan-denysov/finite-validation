# Physics from Finite Validation — code

Reproducibility repository for the preprint:

**Physics from Finite Validation: Classical Recovery and the Quantum Boundary**
United Field Initiative (UFI) · [ufi.observer](https://ufi.observer) · ORCID 0009-0000-3163-4426
DOI: [10.5281/zenodo.20628369](https://doi.org/10.5281/zenodo.20628369)

Every script is standalone, seeded, and carries its status in the docstring. Several
of them document arguments the paper itself **withdrew**; that is deliberate, and the
paper reports them as withdrawn.

State as first published is preserved under tag [`v1.0`](../../releases/tag/v1.0).

## Requirements

- Python 3.10+
- `numpy`

```
pip install numpy
```

## Classical sector (§4)

| Script | Section | What it does |
| --- | --- | --- |
| `calibrate_gr.py` | 4.2 | Gravitational time dilation: the model's leading term coincides with weak-field GR; calibration constant A = 1.0000, no fitting. |
| `two_channel_derivation.py` | 4.3, 5.2 | The temporal and spatial contributions to the light deflection are *equal*, forced by the invariance of c = L/τ. Factor 2 not inserted by hand. |
| `close_two_holes.py` | 4.3, 5.2 | Status audit. Equality **derived** under a named reading; the multiplicative composition **imported**, not a lattice theorem. *Withdraws* the claim that multiplicativity follows from lattice orthogonality. |
| `hypothesis_B_compounding.py` | 4.3 | Perihelion fork: the path-compounded law (1+φ/N)^N → exp(φ) gives β = 1 → 42.99″/century (observed 42.98). |
| `beta_mercury_test.py` | 4.3 | The bare two-channel product (β = 1/2) predicts ~50″/century — excluded by the data as the composition law. |
| `hole_b_second_order.py` | 4.3 | Second-order analysis: the additive law is excluded; the composition is product-like. |
| `emc2_energy_derivation.py` | 4.3 | E = mc² as a two-channel structural analogy — *postulated, not derived*; dimensional and electron-rest-energy consistency check. |
| `side_two_independent.py` | 5.7 | The classical bound 2 is a theorem of binarity (exhaustive enumeration of ±1 assignments). |

## Quantum sector (§5)

| Script | Section | Status |
| --- | --- | --- |
| `lock_to_kuramoto.py` | 5.2 | Reading of the model: a lock is an integrate-and-fire oscillator; the coupling threshold. **Withdraws** the claim that the leak is *necessary* for synchronisation. |
| `correlation_identity.py` | 5.4, 5.5 | Identity, exact: `E = 1 − 2D − s`, and its binary limit `E = 1 − 2D`. No postselection. |
| `chsh_alphabet_bound.py` | 5.5 | Exhaustive enumeration: neither a binary nor a ternary local model exceeds CHSH = 2. **Refutes** the hypothesis that the quantum excess lives in the silence. |
| `local_readout_arcsin.py` | 5.7 | Derived: a local sign-readout of pre-distributed data lands on exactly 2. |
| `single_act_vector.py` | 5.7 | Derived: Tsirelson's vector model; why the parallelogram law is *not* the load; the exclusion of the PR-box; pointwise ±1 components cap CHSH at 2 while one zero component reaches 2√2. |
| `angular_resolution.py` | 5.7 | Derived: the residual against the cosine is first order in the act's grid, vanishes on its native directions, and is therefore exactly zero at the CHSH optimum. **Withdraws** the earlier second-order estimate and the bounds K ≳ 64, K ≳ 256. |
| `born_from_count.py` | 5.9 | Derived: the Born value is the differentiation fraction, D = sin²(θ/2). Why Gleason cannot reach dimension two. |
| `indivisibility_consequences.py` | 5.10 | Derived: complementarity, the phase-space bound, the standard quantum limit, the Zeno effect. **Records** a refuted attempt to read the uncertainty relation off frequency estimation. |
| `twist_parity.py` | 5.11 | Taken mathematics: the double cover, and which ℤ₂ actually carries spin. **Corrects** an earlier conflation of Möbius parity with the belt-trick class. |
| `closure_mass_twist.py` | 5.11 | Derived: circuits as rest mass (the de Broglie clock); the claim that this picture supplies **no fermionic option** for a massless excitation. |

**Retained, not deleted:** `single_act_metric_v1_superseded.py` — the earlier and
*incorrect* reading, in which the differentiation count was said to obey the
parallelogram law. Its error is documented in place.

## Where the load sits

One axiom carries the correlational content of the quantum sector. It is named
identically in the abstract, in *Status and Scope*, in 5.7 and in 6.7:

> The settings of a single undivided act are unconstrained unit vectors of a real
> inner-product space, not pointwise ±1 records carried apart.

If it fails, the Tsirelson bound reverts to 2 and PR-boxes are not excluded. The
parallelogram law is *not* the load: a local hidden-variable model satisfies it too,
and the gap is closed by a pointwise fact, not by the geometry.

## How to run

```
python3 <script>.py
```

Each script prints its own verification and states, at the end, what is derived,
what is taken, and what is owed.

## Withdrawn arguments, in one place

| Script | What it withdraws |
| --- | --- |
| `chsh_alphabet_bound.py` | "the quantum excess lives in the silence" |
| `angular_resolution.py` | the bounds K ≳ 64 and K ≳ 256 (a second-order estimate valid only at the cosine's flat points) |
| `lock_to_kuramoto.py` | "the leak is necessary for synchronisation" |
| `indivisibility_consequences.py` | reading the uncertainty relation off frequency estimation |
| `close_two_holes.py` | multiplicativity from lattice orthogonality (`two_channel_derivation.py`'s claim) |
| `single_act_metric_v1_superseded.py` | "the differentiation count obeys the parallelogram law" |

