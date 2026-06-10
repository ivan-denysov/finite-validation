"""
Closing the two holes the reviewer found in 5.2.0, HONESTLY.
Hole (a): why must the deficit touch BOTH L and tau, not just tau?
Hole (b): why do the two effects MULTIPLY, not add?

Ground rule: no assertion. Each claim must follow from the Section 4
definition of a tick, or be marked as an extra assumption. We will SEE which.

SECTION 4 DEFINITIONS (verbatim from the draft, not new):
  - A tick = a signal crossing ONE link.
  - tau  = duration of that crossing (TIME aspect).
  - L    = the link length the signal reaches in that crossing (SPACE aspect).
  - c    = L / tau  is the lattice invariant (cannot be outrun from within).
  - A mass deficit = a local SLOWING of the tick.
"""
import numpy as np

print("="*72)
print("HOLE (a): does 'slowing the tick' touch tau only, or L and tau both?")
print("="*72)
print("""
The reviewer's alternative model: deficit changes tau, L is DEFINED via L=c*tau,
c untouched -> ONE channel. We must ask what 'slowing the tick' MEANS in Sec 4.

A tick is one object: 'signal crosses one link'. It is not 'a clock ticking in
place'. It has irreducibly BOTH a duration (tau) and a span (L) — that is what a
'crossing' is. So 'slow the tick' is ambiguous between THREE distinct operations:

  OP1  lengthen duration, keep span:   tau->tau(1+e), L fixed  => c drops by ~e
  OP2  shrink span, keep duration:     L->L(1-e),     tau fixed => c drops by ~e
  OP3  both, keep c:                   tau->tau(1+e), L->L(1+e) => c fixed
""")
e = 0.1
L0, tau0 = 1.0, 1.0; c0 = L0/tau0
for name, (L,tau) in {
    "OP1 (tau only)": (L0,        tau0*(1+e)),
    "OP2 (L only)":   (L0*(1-e),  tau0),
    "OP3 (both)":     (L0*(1+e),  tau0*(1+e)),
}.items():
    print(f"  {name:<16} c_local = {L/tau:.4f}  (baseline {c0:.4f})")

print("""
KEY OBSERVATION (this is the real argument, and it is NOT what 5.2.0 said):
  OP1 and OP2 each CHANGE local c. But Section 4 states c is the lattice invariant,
  preserved locally as the signal speed. So OP1 and OP2 are FORBIDDEN by Section 4 —
  they would let an observer detect a local change in c, i.e. outrun the lattice.
  ONLY OP3 preserves c. Therefore 'slowing the tick while respecting Sec 4' is
  forced to be OP3 = both aspects shift together.

  => This DOES close hole (a): the deficit must touch both, because touching one
     alone violates c-invariance. The reviewer's one-channel model (tau only,
     L:=c*tau) is exactly OP1 in disguise IF it lets c stay by REDEFINING L after —
     but then the *physical span the signal reached* changed, which IS the space
     channel. Relabeling does not remove the second shift; it renames it.

  HONEST CAVEAT: this works ONLY if 'mass slows the tick' is read as 'lengthens
  the crossing' (a property of the crossing), not 'lowers an in-place oscillator
  frequency' (a property of a clock). Section 4's tick IS a crossing, so we are
  entitled to it — but this reading is a COMMITMENT we must state, not hide.
""")

print("="*72)
print("HOLE (b): why MULTIPLY (factor 2 / power 2), not ADD?")
print("="*72)
print("""
The observable for light bending is the effective refractive index n felt by a
null ray. A null ray's path is governed by the LINE ELEMENT, which combines the
time part and the space part as a PRODUCT of factors (ds^2 = g_tt dt^2 + g_rr dr^2;
for the optical analogy n = sqrt(g_rr/g_tt), a RATIO/PRODUCT, not a sum).

So the multiplicative combination is NOT derived from 'orthogonality'. It comes
from how a propagating signal samples the metric: it traverses time AND space,
and the traversal composes multiplicatively (a signal delayed by factor (1+phi)
in time and slowed by factor (1+phi) in reach is delayed OVERALL by the product).
Test: compose two independent fractional delays and check first-order doubling.
""")
phi = 1e-6
add   = 1 + phi + phi            # if effects added
mult  = (1+phi)*(1+phi)          # if effects compose multiplicatively
print(f"  added:        n = {add:.10f}  -> bending coeff {add-1:.3e}")
print(f"  multiplied:   n = {mult:.10f} -> bending coeff {mult-1:.3e}")
print(f"  difference is O(phi^2) = {mult-add:.3e}  (negligible at first order)")
print("""
UNCOMFORTABLE TRUTH: at first order, ADD and MULTIPLY give the SAME doubling
(both 2*phi). So the factor 2 does NOT distinguish 'product' from 'sum' — BOTH
give 2. The reviewer's worry is even sharper than stated: the factor-2 evidence
under-determines the combination law. What actually picks 'product' is the
metric/line-element structure (composition of a delay along a path), which is an
ASSUMPTION imported from how signals propagate — defensible, but imported.

For E=mc^2 the situation differs: there c enters as TWO conversions (rate->velocity
and reach->velocity). If those two conversions are applied in SEQUENCE to the same
deficit, they compose multiplicatively (c*c) by construction of 'apply twice'. That
is cleaner than the bending case — but it rests on there being exactly two distinct
conversions, which is hole (a) again.
""")

print("="*72)
print("HONEST VERDICT")
print("="*72)
print("""
HOLE (a): CLOSED, conditionally. Given Section 4's tick = a CROSSING (span+duration)
  and c = local invariant, slowing the tick must move both aspects (OP3); moving one
  alone violates c-invariance. This is a genuine derivation FROM Sec 4 — but it
  commits to reading 'mass slows the tick' as 'lengthens the crossing', which must
  be stated as the model's reading, not smuggled.

HOLE (b): NOT closed by the factor 2. Add and multiply both give 2 at first order,
  so the deflection number cannot select the combination law. 'Product' is justified
  by line-element/path-composition structure (imported), not by orthogonality and
  not by the factor 2. For E=mc^2, 'apply two conversions in sequence' gives c*c more
  cleanly, but only modulo hole (a)'s 'exactly two conversions'.

NET: equality + 'both aspects move' = DERIVABLE from Sec 4 under one stated reading.
  The MULTIPLICATIVE law (hence that the structure is c^2 and not 2c, etc.) is NOT
  derived from the lattice; it is imported from signal/path composition. So the honest
  status is: 'two equal channels' is derived (modulo the crossing-reading); 'they
  compose multiplicatively' is a motivated import, not a lattice theorem.
""")
