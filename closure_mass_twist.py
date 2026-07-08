#!/usr/bin/env python3
"""
closure_mass_twist.py

Closure does double duty: it makes a mode massive, and it closes its ribbon.

THE CLOSED MODE. A closed configuration requires a cycle in the network; in a
simple graph the minimal cycle has three nodes, hence three locks. A localised
packet circulating on that cycle opens and closes each lock as it passes.

TWO COUNTS, and they are different.

  (1) CIRCUITS. The packet goes round; each circuit fires one distinction per lock.
      This count runs even when the mode does not translate. It is the internal
      clock, and it is de Broglie's rest-frame oscillation:

          omega_0 = m c^2 / hbar,      T_0 = 2*pi*hbar / (m c^2).

      Rest mass is the rate of this count.

  (2) REASSEMBLIES. The whole loop is re-established on neighbouring nodes. This
      count runs only when the mode translates; it is the per-lock delay that
      makes v < c. It carries momentum.

Boosting the rest clock turns its phase into the de Broglie wave: omega = gamma*
omega_0 and k = gamma*omega_0*v/c^2 = p/hbar, so lambda = h/p. Verified below.
The relation E^2 = (m c^2)^2 + (p c)^2 states that the two counts combine as the
legs of a right triangle. That combination is NOT derived here; it follows from
the Lorentz factor already recovered in Section 3 of the main text, in the
standard way.

WHY A STEADY CIRCULATION WILL NOT DO. If the loop were filled by a steady flow,
its locks would stand permanently open, no distinction would fire inside, and a
particle at rest would have no internal tick -- hence no rest mass. The
circulating excitation must therefore be a localised packet, not a continuous
fill. (The near-timelessness of the loop's own extension is a separate matter: it
is the strong tick-slowing that constitutes gravity and the straightening of the
occupied segment.)

CONSEQUENCE FOR STATISTICS. The belt-trick Z_2 -- the one that carries spin -- exists
only where the ties are HELD (see twist_parity.py; free one end and any twist slides
off). Closure is what supplies held ties, and it is also what supplies circuits:

    massive  = a closed mode: it sits on its nodes, the same ties persist while its
               packet circulates, and the network holds their far ends. A 2*pi
               rotation traps a full twist -> the fermionic option exists.

    massless = a transfer: received, passed on; at every step the links are new.
               Nothing is held -> nothing can hold a twist ->
               THE PICTURE SUPPLIES NO FERMIONIC OPTION. Exchange sign +1 only.

    massless => boson follows on a further premise, named in the text: in three
    dimensions the exchange sign is +-1, and this picture offers no route to -1
    other than a trapped twist. Massive particles may be fermions or bosons; WHICH
    PARITY A GIVEN ONE CARRIES IS NOT DERIVED. Bosons need not be massless: W, Z and
    the Higgs are closed modes whose held ties carry an even twist.

    Numerical support already exists, and it is the negative half: the electron
    work's dynamical test recomputed the links afresh at every step and the
    two-valuedness vanished. That run IS the massless regime. The positive half --
    that a tie WITH memory carries the twist -- is owed.

Refutation conditions, stated: (a) a fundamental massless fermion would be a thing
this picture cannot accommodate -- the Weyl equation is consistent and standard
theory admits one; (b) in the Standard Model all fermions are massless above the
electroweak transition, and this picture cannot accommodate them there either. Both
tensions are theoretical; every observed massless fundamental particle (photon,
gluon, and the graviton if it exists) is a boson.

WITHDRAWN. An earlier version of this file grounded the claim in "the framing parity
of a closed ribbon", which is the Moebius Z_2 and not the belt-trick Z_2. Corrected.

Standalone: python3 closure_mass_twist.py     (deterministic)
"""
import numpy as np

HBAR = 1.054571817e-34
C = 2.99792458e8


def rest_clock(mass_kg):
    """de Broglie internal clock of a mode at rest."""
    omega0 = mass_kg * C ** 2 / HBAR
    return omega0, 2 * np.pi / omega0


def boosted_clock(mass_kg, beta):
    """Boost the rest clock; return (omega, k, lambda_from_k, lambda_de_Broglie)."""
    gamma = 1.0 / np.sqrt(1.0 - beta ** 2)
    omega0, _ = rest_clock(mass_kg)
    omega = gamma * omega0
    k = gamma * omega0 * beta / C
    p = gamma * mass_kg * beta * C
    return omega, k, 2 * np.pi / k, 2 * np.pi * HBAR / p


if __name__ == "__main__":
    print("1) The circuit clock at rest (count 1)\n")
    for name, m in (("electron", 9.1093837e-31),
                    ("muon", 1.883531e-28),
                    ("proton", 1.67262192e-27)):
        w0, t0 = rest_clock(m)
        print(f"   {name:9s}: omega_0 = {w0:.4e} rad/s,  period = {t0:.4e} s")
    print("\n   photon: no closure -> no circuits -> no rest clock -> massless.")
    print("   (its frequency is set by the source, not by a self-circuit)")

    print("\n2) Boosting the rest clock reproduces the de Broglie wave\n")
    m = 9.1093837e-31
    print(f"   {'v/c':>6} {'2*pi/k':>16} {'h/p':>16} {'rel. error':>12}")
    for beta in (0.1, 0.5, 0.9):
        _, _, lam_k, lam_db = boosted_clock(m, beta)
        print(f"   {beta:>6.2f} {lam_k:>16.6e} {lam_db:>16.6e} "
              f"{abs(lam_k - lam_db) / lam_db:>12.2e}")

    print("\n3) Closure does double duty\n")
    print("   circuits   -> rest mass                 (count 1, runs at rest)")
    print("   reassembly -> momentum, v < c           (count 2, runs on translation)")
    print("   held ties  -> a twist can be trapped    (statistics)")
    print("   => massless: links renewed each step, nothing held, NO FERMIONIC")
    print("      OPTION supplied; boson on the named completeness premise.")
    print("   => massive: circuits and held ties both; which parity is NOT derived.")
    print("\n   Minimal closure in a simple graph: 3 nodes, 3 locks,")
    print("   hence 3 distinctions per circuit.")
