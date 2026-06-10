"""
E = mc^2 from synchronisation energy — honest derivation attempt.
Two routes compared. Question: does c^2 fall out of ENERGY, or only out of dimensions?

Model setup (UFI / Kuramoto foundation):
  - field has mean tick frequency Omega (ticks per unit time)
  - a node desynchronised by frequency deficit delta = Omega - omega_node
  - mass is DEFINED as that deficit:  m ~ delta            (Section 5.2.4)
  - the limit c enters as the conversion between "tick units" and "space units":
      one tick advances a signal by one link of length L:  c = L / tau = L * Omega
    i.e. c is how many spatial units one unit of tick-time buys.

We do NOT assume the answer. We compute each candidate energy and read off
what power of c appears, and WHY.
"""

import numpy as np

# ---- model constants (arbitrary natural units; we track c's POWER, not its value)
Omega = 1.0          # field mean frequency (ticks / time)
L     = 1.0          # link length (space / tick-step)
# conversion: c = spatial distance covered per unit tick-time
c = L * Omega        # = 1 in these units, but we keep it symbolic in the algebra below
# We'll re-introduce c explicitly by carrying units, not by setting it.

print("="*70)
print("ROUTE A — synchronisation (coupling) energy, cos-bonds")
print("="*70)
"""
Kuramoto coupling energy of one node against the field:
    U(phi) = -K * cos(phi)         phi = phase offset of node vs field
Small-offset expansion:
    U(phi) ~ -K + (K/2) phi^2      -> quadratic in the PHASE offset
The phase offset accumulated over one tick from a frequency deficit delta:
    phi = delta * tau = delta / Omega
So:
    U_sync = (K/2) (delta/Omega)^2
This is quadratic in delta (good — mass-like, ~ delta^2) but the prefactor is
K/(2 Omega^2). For this to read as m c^2 we would need K/Omega^2 to BE c^2,
which is a CHOICE of coupling, not a result. c does not fall out; it is inserted
through K. => heuristic, not derived.
"""
K = 1.0
for delta in [0.1, 0.2, 0.5]:
    phi = delta / Omega
    U_sync = 0.5 * K * phi**2
    print(f"  delta={delta:>4}:  U_sync = {U_sync:.5f}   (~ delta^2, prefactor K/(2 Omega^2))")
print("  Verdict A: quadratic in delta, but c enters only via the chosen K. NOT a c^2 derivation.\n")

print("="*70)
print("ROUTE B — kinetic energy of the desync, two channels")
print("="*70)
"""
Here we take the desync deficit delta and ask for its ENERGY as a transported
quantity, using the TWO channels that already gave the two halves of light
deflection (Section 5.2.3) and the c^2 in the heuristic (5.2.5):

  channel TIME : the deficit delta is a rate (ticks/time). Converting a rate
                 into a velocity uses c once:   v_eff = delta * L = delta * (c/Omega)
                 With Omega absorbed into the definition of the deficit (delta in
                 units of Omega), v_eff = delta_hat * c.   [one factor of c]

  channel SPACE: the SAME deficit also displaces the signal spatially per tick,
                 a second, independent factor:  displacement rate = delta_hat * c.
                 [second factor of c]

Energy as the product of mass (=deficit) carried across BOTH channels:
     E = m * (channel_time) * (channel_space) = m * c * c = m c^2
The key test: are the two channels INDEPENDENT (genuine product) or the SAME
factor counted twice (illegitimate)? We test numerically whether treating them
as one channel (E ~ m c) vs two (E ~ m c^2) matches the electron.
"""
MeV = 1.0
m_e = 0.5110  # electron 'mass' as desync, in MeV/c^2 (we test which power of c restores MeV)
# In natural units c=1 we can't see the power. Re-instate SI to test the POWER of c.
c_SI = 2.998e8           # m/s
m_e_kg = 9.109e-31       # kg
J_per_MeV = 1.602e-13

E_one_c  = m_e_kg * c_SI        # if energy were m*c   (one channel)
E_two_c  = m_e_kg * c_SI**2     # if energy were m*c^2 (two channels)
print(f"  one channel  E=m c   = {E_one_c:.3e} J  = {E_one_c/J_per_MeV:.3e} MeV")
print(f"  two channels E=m c^2 = {E_two_c:.3e} J  = {E_two_c/J_per_MeV:.4f} MeV")
print(f"  electron rest energy (target)        = 0.5110 MeV")
print("  Verdict B: the electron is matched ONLY by m c^2 (two channels).")
print("  The two-channel structure is what selects the SECOND power of c.\n")

print("="*70)
print("HONEST READ-OUT")
print("="*70)
print("""
Route A (coupling energy): gives the right SHAPE (energy quadratic in the
  desync) but c^2 does NOT emerge — it is hidden inside the coupling K. So A
  supports 'energy ~ desync^2' but cannot claim to derive c^2.

Route B (two-channel transport): the SECOND power of c is forced by matching
  the electron — one channel undershoots by a factor c (~3e8). The two-channel
  structure (time + space), the SAME structure that produced both halves of
  light deflection, is what selects c^2. This is the strongest version, but it
  rests on the two channels being INDEPENDENT. That independence is exactly the
  postulate behind the 1.750'' deflection. So B is as solid as 5.2.3 is — no more.

CONCLUSION: c^2 is recovered as a STRUCTURE (two independent channels), not as a
  number derived from dynamics. Quadratic-in-desync is genuinely derivable
  (Route A). The leap from 'quadratic energy' to 'c^2 specifically' is carried
  by the two-channel postulate, not by the Kuramoto dynamics alone.
  => Correct status: STRUCTURAL recovery of the c^2 form, resting on the same
     two-channel postulate as light deflection. NOT an independent derivation.
""")
