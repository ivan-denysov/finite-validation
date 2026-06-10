"""
HOLE (b), second attempt: can the COMBINATION LAW (sum vs product) be DERIVED
rather than imported, by going to second order where they differ?

First order: sum and product both give 1+2phi. Indistinguishable.
Second order: product = 1+2phi+phi^2 ; sum = 1+2phi. They split at O(phi^2).

Strategy: find a regime/observable sensitive to O(phi^2) and check which law
matches GR. If product matches GR's known second-order results and sum fails,
the multiplicative law is SELECTED BY DATA — a derivation, not an import.

We use the standard PPN expansion. GR's metric to second order (isotropic):
  g_tt = -(1 - 2U + 2 beta U^2 + ...)   with beta_GR = 1
  g_rr =  (1 + 2 gamma U + ...)          with gamma_GR = 1
where U = GM/(rc^2) = phi.
Key GR facts to test against:
  - light bending uses (gamma+1)/2 -> full value needs gamma=1 (the SPACE channel)
  - perihelion / strong-field uses beta at second order
  - the COMBINATION that reproduces GR's g_tt to O(U^2) fixes beta.
"""
import numpy as np

phi = np.linspace(0, 0.3, 7)  # push toward strong field so phi^2 matters

print("phi      sum=1+2phi     product=(1+phi)^2   GR g_tt-like 1+2phi+2*beta*phi^2(beta=1)")
print("-"*82)
for p in phi:
    s = 1 + 2*p
    pr = (1+p)**2                 # = 1 + 2p + p^2
    gr = 1 + 2*p + 2*1.0*p**2     # GR beta=1 form: 1 + 2U + 2 beta U^2
    print(f"{p:.2f}   {s:.6f}      {pr:.6f}           {gr:.6f}")

print("""
READ-OUT:
  product = 1 + 2phi + phi^2.
  GR (beta=1) time part to second order = 1 + 2phi + 2 phi^2.
  sum = 1 + 2phi (no second-order term at all).

  So at O(phi^2):
    - sum is WRONG (misses the term entirely) -> sum is excluded by GR. GOOD: rules one out.
    - product gives coefficient 1; GR gives coefficient 2. product is CLOSER than sum
      but still OFF by a factor 2 at second order.

  => Going to second order DOES exclude the additive law (good — that was half the worry),
     but a naive single product (1+phi)^2 does NOT reproduce GR's second-order coefficient.
     GR's 2 phi^2 needs BOTH channels contributing at second order, i.e. the SAME
     two-channel structure compounding — consistent with 'product', but the exact
     coefficient is a genuine second-order check the bare model has not earned yet.
""")

print("="*72)
print("Sharper: does the TWO-CHANNEL product reproduce GR's gamma and beta?")
print("="*72)
print("""
GR light bending coefficient is (1+gamma)/2 of the Newtonian value, times 2 ->
the measured 1.750'' requires gamma = 1. In our model:
  - time channel alone (Einstein 1911) = the '1' (Newtonian-like, 0.875'')
  - adding the space channel doubles it -> our space channel plays the role of gamma=1.
So at FIRST order our two-channel product is equivalent to setting gamma=1: MATCHES GR.

At SECOND order GR has an independent parameter beta (perihelion advance).
beta is NOT fixed by the bending. Our model, as it stands, predicts the second-order
coefficient from the SAME single deficit compounding -> it makes a DEFINITE prediction
(coefficient 1 from (1+phi)^2), which DISAGREES with GR's beta=1 (coefficient 2).
""")

# Quantify the discrepancy as a testable number: perihelion-like second order
phi_merc = 2.96e-8   # ~ GM_sun/(r c^2) at Mercury (order of magnitude)
coeff_model = 1.0    # from (1+phi)^2
coeff_GR    = 2.0    # GR beta=1
print(f"  second-order term, model:  {coeff_model} * phi^2 = {coeff_model*phi_merc**2:.3e}")
print(f"  second-order term, GR:     {coeff_GR} * phi^2 = {coeff_GR*phi_merc**2:.3e}")
print(f"  ratio model/GR at 2nd order = {coeff_model/coeff_GR:.2f}  -> model UNDERSHOOTS by 2x")

print("""
HONEST VERDICT ON HOLE (b), attempt 2:
  WIN: the additive law is now EXCLUDED — second order kills 'sum'. So 'they
       combine non-additively' is no longer an import; it is forced by GR's
       known second-order structure (perihelion exists, sum predicts none).
  LOSS: the bare single-product (1+phi)^2 gives second-order coefficient 1,
       but GR needs 2 (beta=1). So 'multiplicative' in the crude form is also
       not exactly right — the true second-order structure has TWO compounding
       contributions, coefficient 2, which our model motivates but does not yet
       compute from first principles.

  NET STATUS for 5.2.0(ii): 'non-additive composition' is now DERIVED (second
  order excludes the sum). The EXACT composition law (and the precise c^2 vs
  any other power at higher order) is CONSTRAINED to be product-like but its
  second-order coefficient is an OPEN, TESTABLE prediction where the bare model
  currently undershoots GR by 2x. This is a falsifiable handle, not a hand-wave.
""")
