#!/usr/bin/env python3
"""
local_readout_arcsin.py

The load-bearing negative result: quantum correlations cannot arise from LOCAL
READOUT of pre-distributed micro-data. The comparison of tick-patterns must occur
WITHIN the single act (at the lock).

Setup. Suppose each party holds its own accumulated micro-pattern, the two
patterns being correlated at the micro level with correlation rho, and each party
reports the SIGN of its own aggregate. For jointly Gaussian aggregates the sign
correlation obeys the arcsin law (Grothendieck's identity):

    E_macro = (2/pi) * arcsin(rho).

Consequence at the CHSH-optimal angles. Take the quantum micro-correlations
rho = cos(theta) at the standard optimal settings. Because arcsin(1/sqrt(2)) =
pi/4 exactly, every bracket becomes

    E = (2/pi) * (pi/4) = 1/2   exactly,

and therefore

    CHSH = |1/2 - (-1/2) + 1/2 + 1/2| = 2   exactly.

Local sign readout saturates the classical bound and cannot exceed it. Whereas an
in-act comparison, where the patterns meet and E = cos(theta) directly, gives
CHSH = 2*sqrt(2).

Interpretation. The model's requirement that pattern comparison happen inside a
single act at the lock is therefore not an assumption of convenience: it is FORCED
by Bell. Any scheme in which the parties merely read out locally held data --
however richly correlated -- lands exactly on 2.

Status: derived (Grothendieck / arcsin law is standard mathematics, cited as
support); the exactness at the CHSH angles follows from arcsin(1/sqrt 2) = pi/4.
Numerically verified below.

Standalone: python3 local_readout_arcsin.py     (seed fixed)
"""
import numpy as np


def sign_correlation(rho, n=400_000, seed=1):
    """Empirical sign correlation of two jointly Gaussian variables."""
    rng = np.random.default_rng(seed)
    z1 = rng.standard_normal(n)
    z2 = rho * z1 + np.sqrt(max(0.0, 1 - rho ** 2)) * rng.standard_normal(n)
    return np.mean(np.sign(z1) * np.sign(z2))


def chsh(e):
    return abs(e[0] - e[1] + e[2] + e[3])


if __name__ == "__main__":
    print("1) Arcsin law: sign correlation vs underlying correlation rho\n")
    print(f"{'rho':>8} {'measured':>12} {'(2/pi)arcsin(rho)':>20}")
    for rho in (0.2, 0.5, 1 / np.sqrt(2), 0.9):
        meas = sign_correlation(rho)
        theory = (2 / np.pi) * np.arcsin(rho)
        print(f"{rho:>8.4f} {meas:>12.4f} {theory:>20.4f}")

    print("\n2) CHSH at the optimal angles, two readout schemes\n")
    angles = [(0.0, np.pi / 4), (0.0, 3 * np.pi / 4),
              (np.pi / 2, np.pi / 4), (np.pi / 2, 3 * np.pi / 4)]
    rho = [np.cos(a - b) for a, b in angles]

    e_in_act = rho                                        # comparison inside the act
    e_local = [(2 / np.pi) * np.arcsin(r) for r in rho]   # local sign readout

    print(f"  in-act comparison, E = cos(theta):        CHSH = {chsh(e_in_act):.6f}"
          f"   (= 2*sqrt(2) = {2*np.sqrt(2):.6f})")
    print(f"  local sign readout, E = (2/pi)arcsin:     CHSH = {chsh(e_local):.6f}"
          f"   (= 2 exactly)")
    print()
    print("  Exactness: arcsin(1/sqrt(2)) = pi/4, so each bracket is exactly 1/2,")
    print("  and the four brackets sum to exactly 2 -- the classical bound.")
    print()
    print("CONCLUSION: local readout of pre-distributed micro-data yields exactly the")
    print("classical bound. Quantum correlations require in-act comparison at the lock.")
    print("[Status: derived; the arcsin law is taken mathematics.]")
