"""
Does the bare two-channel model's beta ~ 1/2 survive REAL Mercury data?
GR predicts 42.98 arcsec/century anomalous perihelion advance; observed matches.

PPN perihelion advance per orbit (standard form):
    delta_phi = (6 pi G M) / (a (1 - e^2) c^2)  * [ (2 + 2 gamma - beta) / 3 ]
For GR: gamma = 1, beta = 1  -> bracket = (2 + 2 - 1)/3 = 3/3 = 1  -> full 42.98"/cy.

Our model (from hole_b_second_order.py):
  - first order light bending requires gamma = 1 (the space channel) -> we KEEP gamma = 1.
  - second-order time-sector coefficient comes out as ~1/2 of GR's -> beta ~ 1/2.
Plug our (gamma=1, beta=1/2) into the SAME PPN formula and compare to 42.98"/cy.
"""
import numpy as np

# Mercury / Sun constants (SI)
G    = 6.674e-11
M    = 1.989e30          # solar mass, kg
c    = 2.998e8
a    = 5.7909e10         # Mercury semi-major axis, m
e    = 0.2056            # eccentricity
T    = 87.969*86400      # orbital period, s
cy   = 100*365.25*86400  # century, s

# orbits per century
n_orbits = cy / T
arcsec_per_rad = 180/np.pi*3600

# base coefficient (per orbit), without the PPN bracket
base = 6*np.pi*G*M / (a*(1-e**2)*c**2)   # radians per orbit

def advance(gamma, beta):
    bracket = (2 + 2*gamma - beta)/3
    per_orbit = base*bracket
    return per_orbit*n_orbits*arcsec_per_rad

gr   = advance(1.0, 1.0)
ours = advance(1.0, 0.5)
print(f"GR   (gamma=1, beta=1):    {gr:6.2f} arcsec/century   [observed ~42.98]")
print(f"Ours (gamma=1, beta=1/2):  {ours:6.2f} arcsec/century")
print(f"ratio ours/GR = {ours/gr:.3f}")
print(f"difference    = {ours-gr:+.2f} arcsec/century")
print(f"GR bracket = {(2+2*1-1)/3:.3f} ; our bracket = {(2+2*1-0.5)/3:.3f}")

print("""
READ-OUT (perihelion):
  The PPN bracket is (2 + 2 gamma - beta)/3. With gamma=1 fixed by light bending:
    GR:   (2 + 2 - 1)/3   = 1.000
    Ours: (2 + 2 - 0.5)/3 = 1.167
  So our beta=1/2 does NOT undershoot the perihelion — it OVERSHOOTS by ~17%.
  Predicted ~50.1 vs observed 42.98 arcsec/century. A ~7 arcsec/century EXCESS.

  This is the bear. It is a clean, ~17% deviation in a quantity measured to
  ~0.1% precision. The bare model, taken literally, is FALSIFIED by Mercury at
  many sigma. That is exactly the kind of sharp risk a foundations referee
  respects — but we must report it as a REAL tension, not dress it up.
""")

print("="*64)
print("Shapiro delay — the SAME parameters, independent test")
print("="*64)
print("""
Shapiro time delay depends on (1 + gamma)/2. It is a gamma-test, NOT a beta-test.
  GR:   gamma = 1 -> coefficient (1+1)/2 = 1.
  Ours: gamma = 1 (kept, from first-order bending) -> coefficient 1. SAME as GR.
So Shapiro does NOT discriminate our model from GR: we pass it trivially because
we kept gamma=1. The discriminating test is perihelion (beta), not Shapiro.
""")
gamma = 1.0
print(f"  Shapiro coefficient (1+gamma)/2: ours = {(1+gamma)/2:.3f}, GR = 1.000 -> identical")

print("""
HONEST STRATEGIC READ-OUT:
  1. gamma is FIXED to 1 by first-order light bending -> we pass bending and
     Shapiro automatically (both are gamma-tests). No risk there, no new info.
  2. The ONLY discriminating classical test is the perihelion (beta). Our bare
     beta=1/2 predicts ~50"/cy vs observed 43"/cy: a ~17% EXCESS, robustly
     falsified. (Note: earlier we said 'undershoot by 2x' looking at the raw g_tt
     coefficient; inside the full PPN orbit formula with gamma=1 held, the sign
     flips to an OVERSHOOT. Worth stating carefully in the paper — the raw
     coefficient and the observable advance are not the same thing.)
  3. So the falsifiable handle is REAL and SHARP. Two honest options for the paper:
       (A) Report beta=1/2 as a clean failure of the BARE model and frame the
           paper's open problem as 'what second-order completion restores beta=1'.
       (B) Investigate whether the missing second-order compounding (the factor we
           know is absent) is exactly what would move 1/2 -> 1. If it plausibly
           does, the handle becomes 'model predicts beta=1 ONLY IF channels compound
           twice; first-order is silent on this; perihelion is the test'.
  Either way: do NOT hide it. The deviation is the most scientifically valuable
  line in the paper precisely because it can lose.
""")
