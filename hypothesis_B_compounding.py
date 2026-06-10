"""
Hypothesis B: does completing the SECOND-ORDER compounding of the two channels
move beta from 1/2 to exactly 1 — WITHOUT tuning?

Rule of honesty: I do NOT insert a term chosen to give beta=1. I give the
compounding an INDEPENDENT meaning and compute whatever it yields. If it lands on
1, that's a result. If it lands on 0.83 or 1.4, I report that.

The independent meaning:
  First order: a deficit perturbs each channel once. The signal sees a background
  shifted by phi in time and phi in space.
  Second order: the signal that is ALREADY slowed propagates through a lattice that
  is ITSELF already shifted. So the time channel acts on the (already space-shifted)
  signal and vice versa. This is the cross-term that a single bare product
  (1+phi)(1+phi) MISSES, because that product treats the two shifts as acting on the
  UNPERTURBED signal independently. Real metric propagation compounds them.

We model three explicit composition laws and read off the second-order coefficient,
then convert to beta and to Mercury arcsec/century. The GR target is the
EXPONENTIAL/metric compounding, which is the physically motivated one — NOT chosen
to hit beta=1, but because exp is what 'apply the same fractional shift repeatedly
along the path' gives in the continuum limit.
"""
import numpy as np

# ---- the three candidate laws for the effective metric factor n(phi) ----
# We expand each to second order and read coefficient of phi^2.
# GR time-sector g_tt = 1 + 2phi + 2 phi^2  -> target second-order coeff = 2 (beta=1)

phi = 1e-3
laws = {
    "additive            n=1+2phi":          (1 + 2*phi,                0.0),
    "bare product        n=(1+phi)^2":       ((1+phi)**2,               1.0),
    "compounded (exp)    n=exp(2phi)":       (np.exp(2*phi),            2.0),
}
print("law                                 n(phi)        2nd-order coeff (analytic)")
print("-"*74)
for name,(val,coeff) in laws.items():
    # numerically extract 2nd-order coeff: (n - 1 - 2phi)/phi^2
    num_coeff = (val - 1 - 2*phi)/phi**2
    print(f"{name:<35} {val:.8f}   {coeff:.2f}  (num {num_coeff:.3f})")

print("""
KEY POINT (no tuning):
  - additive  -> 2nd-order coeff 0  -> beta would be ... (no term) -> wrong (no precession)
  - bare product (1+phi)^2 = 1 + 2phi + 1*phi^2 -> coeff 1 -> beta=1/2 (our REV3 value)
  - compounded exp(2phi) = 1 + 2phi + 2phi^2 + ... -> coeff 2 -> beta=1 EXACTLY

  Why exp is the RIGHT completion, not a fudge:
  'apply the same fractional shift phi to the signal at every step ALONG ITS PATH'
  compounds multiplicatively step by step: (1+phi/N)^N -> exp(phi) as N->inf.
  The bare product (1+phi)^2 is the N=2 truncation (two channels, one application
  each, acting on the UNPERTURBED signal). The continuum path-compounding is exp.
  GR's metric is exactly the exponentiated (continuum) version. So:
    bare two-channel  = first non-trivial truncation -> beta=1/2
    full path-compounded = continuum limit          -> beta=1
""")

# ---- convert each to Mercury perihelion ----
G,M,c = 6.674e-11,1.989e30,2.998e8
a,e   = 5.7909e10,0.2056
T     = 87.969*86400; cy=100*365.25*86400
n_orbits = cy/T; arcsec=180/np.pi*3600
base = 6*np.pi*G*M/(a*(1-e**2)*c**2)
def adv(beta,gamma=1.0): return base*((2+2*gamma-beta)/3)*n_orbits*arcsec

print("Mercury perihelion advance (gamma=1 throughout):")
for label,beta in [("bare product  beta=1/2",0.5),
                   ("compounded exp beta=1",1.0)]:
    print(f"  {label:<26} -> {adv(beta):6.2f} arcsec/century   (observed 42.98)")

print("""
VERDICT ON HYPOTHESIS B:
  YES — completing the compounding moves beta 1/2 -> 1 EXACTLY, and Mercury goes
  50.1 -> 42.99 arcsec/century, matching observation. AND this is NOT a tuned fix:
  exp is the continuum limit of 'the same fractional shift applied along the whole
  path', of which the bare two-channel product is the leading (N=2) truncation.

  So the honest statement becomes very strong:
    * FIRST order: the two-channel structure gives the 1.750'' bending (gamma=1).
      The truncation level is invisible here — N=2 and N=inf agree at first order.
    * SECOND order: the truncation MATTERS. The bare N=2 product predicts beta=1/2
      (Mercury 50''/cy, FALSIFIED). The path-compounded continuum predicts beta=1
      (Mercury 43''/cy, CONFIRMED).
    * Therefore the model makes a SHARP, FALSIFIABLE claim: the deficit must
      compound along the path (exp), not act as a one-shot two-channel product.
      Mercury SELECTS the compounded law over the bare product.

  This is far better than either 'we recover GR' or 'we are falsified':
  the model has a real internal fork (truncated vs compounded), and DATA picks the
  branch. That is a genuine post-diction with risk — exactly the bear we wanted.

  CAVEAT to state plainly: we have not DERIVED that the compounding must be the
  exponential/continuum form from the Section-4 lattice alone; we have shown that
  IF the single-step shift is phi and it applies along the path, the continuum
  limit is exp, which gives beta=1. The lattice makes this natural (a signal really
  does traverse many links), but the step-to-continuum passage is an added,
  physically-motivated assumption. Status: motivated + data-selected, not a lattice
  theorem. Still a falsifiable, passing prediction.
""")
