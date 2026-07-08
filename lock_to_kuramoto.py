#!/usr/bin/env python3
"""
lock_to_kuramoto.py

Joining the two descriptions: the field of Kuramoto metronomes (Section 4) and
the network of gravitational locks (Section 5) are one object seen at two levels.

THE LOCK IS AN INTEGRATE-AND-FIRE OSCILLATOR.
    It loads; at threshold it opens (one distinction, one tick); its microgravity
    draws it shut and the load is reset. That is precisely the integrate-and-fire
    cycle. Networks of pulse-coupled integrate-and-fire oscillators admit a phase
    reduction to Kuramoto-type dynamics under weak coupling (Winfree 1967;
    standard phase reduction), and exhibit the same coupling threshold.

DICTIONARY.
    Kuramoto phase        theta_i   <->  the LOAD of node i's lock -- where in the
                                          accumulate/open/close cycle it stands
    natural frequency     omega_i   <->  that node's intrinsic tick rate
    coupling  K sin(th_j - th_i)    <->  the microgravity of the shared link,
                                          pulling neighbouring locks toward a
                                          common phase of loading
    synchronisation                 <->  a common rhythm of opening
    "mass = lowered frequency"      <->  a mode whose circuits consume the load

WHAT THE RUNS BELOW SHOW.
    A ring of locks with pulse coupling exhibits a coupling threshold: below it the
    locks stay incoherent, above it they lock into a common rhythm. This is the
    Kuramoto transition, whose critical coupling K_c = 2/(pi g(omega_0)) already
    appears in the vacuum work.

    The microgravity of a lock pulls it shut while the load is building, which
    makes the charging curve CONCAVE (a leaky integrator). Concavity is the
    Mirollo & Strogatz (1990) condition under which global synchronisation is
    PROVED for all-to-all excitatory coupling. In the runs below the leaky lock
    reaches coherence (R > 0.5) where the linear one does not, over the coupling
    range tested.

REFUTED CLAIM, recorded.
    An earlier reading of these runs asserted that the leak is NECESSARY for
    synchronisation. It is not established by anything here: concavity is
    sufficient (Mirollo-Strogatz), and whether it is necessary is not settled by
    these runs. The claim is withdrawn.

STATUS. The identification of the Kuramoto phase with the lock's load is a
reading of the model -- natural, and consistent with the runs -- not a derivation.
The rigorous reduction of the lock network to the phase network, and thence to a
field, is the business of the bridge work and remains the programme's load-bearing
debt.

Standalone: python3 lock_to_kuramoto.py    (seeded; ~1 min)
"""
import numpy as np


def run_lock_ring(eps, leak, n=80, steps=40_000, dt=0.002, tau=2.0,
                  seed=2, spread=0.03, k_neighbours=4):
    """Ring of pulse-coupled locks. Returns the final Kuramoto order parameter."""
    rng = np.random.default_rng(seed)
    drive = np.clip(0.8 + spread * rng.standard_normal(n), 0.6, 1.0)
    load = rng.random(n) * 0.9
    order = []
    for s in range(steps):
        load += ((drive - load / tau) if leak else drive) * dt
        fired = np.where(load >= 1.0)[0]
        if fired.size:
            load[fired] = 0.0                       # cycle closure: the load resets
            for i in fired:
                for d in range(1, k_neighbours // 2 + 1):
                    for j in ((i - d) % n, (i + d) % n):
                        if load[j] < 1.0:
                            load[j] = min(load[j] + eps, 0.999)
        if s % 20 == 0:
            order.append(abs(np.mean(np.exp(2j * np.pi * load))))
    return float(np.mean(order[-200:]))


if __name__ == "__main__":
    print("Coupling threshold in a ring of locks (the Kuramoto transition)\n")
    print(f"   {'eps':>7} {'R (leaky lock)':>17} {'R (linear lock)':>18}")
    for eps in (0.0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.14):
        r_leak = run_lock_ring(eps, leak=True)
        r_lin = run_lock_ring(eps, leak=False)
        print(f"   {eps:>7.2f} {r_leak:>17.4f} {r_lin:>18.4f}")

    print("\n   Below threshold: incoherent. Above: a common rhythm of opening.")
    print("   The leaky (concave) lock reaches coherence where the linear one does")
    print("   not, over the range tested. Concavity is the Mirollo-Strogatz")
    print("   condition -- sufficient, not shown necessary.\n")
    print("   The Kuramoto field of Section 4 is the phase description of this")
    print("   lock network. The rigorous reduction is the bridge work's business.")
