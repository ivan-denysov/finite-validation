#!/usr/bin/env python3
"""
correlation_identity.py

The identity underlying the count reading of correlation.

Outcomes at the lock level form a ternary alphabet {-1, 0, +1} (see the
half-difference construction: zero is of two kinds — no meeting, or a meeting of
equal potentials). Define, over ALL ticks (no postselection):

    N        = total ticks
    N_agree  = ticks where the two patterns agree      (product +1)
    N_diff   = ticks where they differentiate          (product -1)
    N_silent = ticks with a zero on either side        (product  0)

    D = N_diff / N      (differentiation fraction)
    s = N_silent / N    (silence fraction)

Then the correlation, defined as the mean product over ALL ticks, satisfies

    E = <A*B> = (N_agree - N_diff)/N = 1 - 2D - s.                        (exact)

When silence is absent (s = 0, pure binary alphabet) this reduces to the
familiar E = 1 - 2D.

WHY THE NORMALISATION MATTERS. Restricting the average to "meetings" (ticks with
a nonzero product) is POSTSELECTION and reproduces the detection loophole:
postselected correlations can exceed the CHSH bound of 2 even for local models.
The identity above avoids this by averaging over all ticks.

LEVELS. The ternary alphabet is a lock-level (micro) structure. The detector
outcome of a Bell run is a single Sigma-act, binary by construction (validation
closes or it does not); hence at the run level every trial yields +-1, s = 0, and
the comparison against the CHSH bound is legitimate. See local_readout_arcsin.py
for why the micro->macro readout cannot be local.

Status: identity [exact]; verified numerically below.

Standalone: python3 correlation_identity.py    (seed fixed)
"""
import numpy as np


def check_identity(n=200_000, p_zero=0.30, seed=0):
    rng = np.random.default_rng(seed)
    p = [(1 - p_zero) / 2, p_zero, (1 - p_zero) / 2]
    a = rng.choice([-1, 0, 1], size=n, p=p)
    b = rng.choice([-1, 0, 1], size=n, p=p)
    prod = a * b

    e_direct = prod.mean()                       # mean over ALL ticks
    n_diff = np.sum(prod == -1)
    n_silent = np.sum(prod == 0)
    d = n_diff / n
    s = n_silent / n
    e_formula = 1 - 2 * d - s
    return e_direct, e_formula, d, s


def check_binary_limit(n=200_000, seed=1):
    rng = np.random.default_rng(seed)
    a = rng.choice([-1, 1], size=n)
    b = rng.choice([-1, 1], size=n)
    prod = a * b
    d = np.mean(prod == -1)
    return prod.mean(), 1 - 2 * d


if __name__ == "__main__":
    e_direct, e_formula, d, s = check_identity()
    print("Ternary tick-patterns, correlation over ALL ticks (no postselection):")
    print(f"  E = <A*B>      = {e_direct: .8f}")
    print(f"  1 - 2D - s     = {e_formula: .8f}")
    print(f"  |difference|   = {abs(e_direct - e_formula):.2e}")
    print(f"  (D = {d:.4f}, s = {s:.4f})")
    print()

    e_bin, e_bin_formula = check_binary_limit()
    print("Binary limit (s = 0):")
    print(f"  E = <A*B>      = {e_bin: .8f}")
    print(f"  1 - 2D         = {e_bin_formula: .8f}")
    print(f"  |difference|   = {abs(e_bin - e_bin_formula):.2e}")
    print()
    print("Identity confirmed to machine precision in both regimes.")
