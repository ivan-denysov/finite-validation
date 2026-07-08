#!/usr/bin/env python3
"""
indivisibility_consequences.py

Three consequences of one fact: the act of validation is indivisible by the tick.

(1) THE ZENO EFFECT.
    A Sigma-act is the closing of a validation cycle. Closing the cycle closes the
    lock and returns its load to zero. Between acts the load accumulates and the
    chance the lock has flipped is the differentiation fraction

        D = sin^2(theta/2),      theta = accumulated phase,

    which is QUADRATIC in theta at short times -- the half-angle identity again.
    That quadratic is exactly what makes Zeno possible; an exponential (linear)
    law would forbid it. With N interrupting acts in a total time T, the survival
    probability is (1 - sin^2(theta_N/2))^N with theta_N = omega*T/N, which tends
    to 1 as N grows: observation freezes the system.

    Status: derived, given D = sin^2(theta/2) [derived elsewhere] and cycle
    closure [the definition of Sigma]. Nothing new is postulated.

(2) THE STANDARD QUANTUM LIMIT.
    Estimating theta by counting N_d differentiations out of N ticks is a binomial
    problem: Var(D_hat) = D(1-D)/N. With D = sin^2(theta/2) one has
    D(1-D) = sin^2(theta)/4 and dD/dtheta = sin(theta)/2, so the two sines cancel:

        sigma_theta = 1 / sqrt(N),     independent of theta.

    This is the standard quantum limit, obtained here purely by counting.

    Status: derived; verified numerically below.

(3) COMPLEMENTARITY AND THE EXISTENCE OF A BOUND.
    Position is established by ONE act; momentum is a COUNT of reassemblies and
    needs a baseline of many. One act is not many acts, so a single act cannot
    answer both questions. This is complementarity, and it follows from
    indivisibility -- not from a disturbance caused by the apparatus.

    Quantitatively: a region of phase space smaller than one act contains no act,
    hence no answer, so Delta_x * Delta_p >= S_0, the action of one act. In this
    picture hbar IS the area of one act in phase space.

    NOT derived: the value of hbar (S_0 = hbar is a calibration), and the factor
    1/2 in the textbook relation, which comes from Cauchy-Schwarz on a commutator
    in a Hilbert space -- the isomorphism debt.

REFUTED ARGUMENT, recorded as a lesson.
    An earlier attempt read the uncertainty relation off the claim that "a rate
    cannot be estimated without a baseline of ticks", i.e. sigma_omega * T ~ 1.
    A direct test refutes this as stated: the estimation error of a frequency
    beats the Fourier resolution limit (Cramer-Rao), so sigma_omega * T falls with
    the number of samples. The argument is not used.

Standalone: python3 indivisibility_consequences.py    (seeded)
"""
import numpy as np


def survival_under_interruption(n_acts, omega=1.0, total_time=np.pi):
    """Survival probability after n_acts interrupting Sigma-acts."""
    theta = omega * total_time / n_acts
    p_flip_each = np.sin(theta / 2) ** 2
    return (1 - p_flip_each) ** n_acts


def sigma_theta_simulated(n_ticks, theta, trials=400, seed=0):
    """Estimate theta by counting differentiations; return the spread."""
    rng = np.random.default_rng(seed)
    d = np.sin(theta / 2) ** 2
    est = []
    for _ in range(trials):
        n_d = rng.binomial(n_ticks, d)
        d_hat = np.clip(n_d / n_ticks, 1e-9, 1 - 1e-9)
        est.append(2 * np.arcsin(np.sqrt(d_hat)))
    return float(np.std(est))


if __name__ == "__main__":
    print("1) The Zeno effect: survival after N interrupting acts (T = pi)\n")
    print(f"   {'N':>8} {'survival':>12}")
    for n in (1, 2, 5, 10, 100, 1000, 10000):
        print(f"   {n:>8} {survival_under_interruption(n):>12.6f}")
    ns = np.array([10, 100, 1000, 10000, 100000])
    loss = 1 - np.array([survival_under_interruption(n) for n in ns])
    slope = np.polyfit(np.log(ns), np.log(loss), 1)[0]
    print(f"\n   loss (1 - survival) scales as N^({slope:.3f})   [theory: N^(-1)]")
    print("   Observation freezes the transition.\n")

    print("2) The standard quantum limit from counting differentiations\n")
    print(f"   {'N ticks':>9} {'theta':>8} {'sigma_theta':>13} {'1/sqrt(N)':>12} {'ratio':>8}")
    for n in (100, 1000, 10000):
        for th in (np.pi / 3, np.pi / 2):
            s = sigma_theta_simulated(n, th)
            print(f"   {n:>9} {th:>8.4f} {s:>13.5f} {1/np.sqrt(n):>12.5f} "
                  f"{s*np.sqrt(n):>8.4f}")
    print("\n   sigma_theta * sqrt(N) = 1, independent of theta. [derived]\n")

    print("3) Complementarity and the bound\n")
    print("   one act, one question -> complementarity          [derived]")
    print("   phase space is not cut finer than one act:")
    print("       Delta_x * Delta_p >= S_0,   hbar = area of one act")
    print("                                                      [derived; hbar calibrated]")
    print("   the factor 1/2, and the value of hbar              [not derived]")
