"""
Does Ivan's geometric picture DERIVE 2sqrt2, or is it a numerical coincidence?

Picture (Ivan): t=0 quantum link = a CLOSED CIRCLE (finite outside, infinite inside).
Two normal particles tear it into a LOOP; the signal runs along one EDGE of the
loop. With sides 2x2, that edge/diagonal = 2sqrt2 = half the figure-eight.

Honest test: 2sqrt2 is a REAL number in physics (Tsirelson bound). The question
is whether this geometry REPRODUCES the actual CHSH structure or merely lands on
the same number by shape-coincidence. We check against the genuine quantum
correlation E(a,b) = -cos(theta), which is WHERE 2sqrt2 truly comes from.
"""
import numpy as np

print("="*68)
print("STEP 1 — where 2sqrt2 ACTUALLY comes from (ground truth)")
print("="*68)
# CHSH: S = E(a,b)-E(a,b')+E(a',b)+E(a',b'),  E(x,y) = -cos(x-y) for the singlet
def E(x,y): return -np.cos(x-y)
def chsh(a,ap,b,bp): return E(a,b)-E(a,bp)+E(ap,b)+E(ap,bp)
# optimal quantum angles: a=0, a'=90, b=45, b'=135 (degrees)
d=np.pi/180
a,ap,b,bp = 0*d, 90*d, 45*d, 135*d
S = chsh(a,ap,b,bp)
print(f"  optimal angles 0/90 vs 45/135 -> S = {S:.5f}  (= 2*sqrt2 = {2*np.sqrt(2):.5f})")
print("  => the 45-degree spacing is the source. 2sqrt2 = 4*cos(45) = 4/sqrt2.")
print("     The '2' under the root is NOT a 2x2 side; it is 1/cos45 from the angle.")

print("="*68)
print("STEP 2 — does the '2x2 loop, diagonal = 2sqrt2' give the SAME for the right reason?")
print("="*68)
# Ivan's diagonal: square side s -> diagonal = s*sqrt2. For s=2 -> 2sqrt2.
for s in [1,2,3]:
    print(f"  square side s={s}:  diagonal = s*sqrt2 = {s*np.sqrt(2):.4f}")
print("""
  The diagonal of a 2x2 square is 2sqrt2 — TRUE, but it equals the Tsirelson
  value ONLY for the specific side s=2. The bound 2sqrt2 does NOT come from a
  side-length 2; it comes from 4*cos(45). To make 'diagonal' match, you must
  CHOOSE s=2 by hand. So the square picture reproduces the NUMBER only if its
  size is fixed to the answer.
""")

print("="*68)
print("STEP 3 — is there an INDEPENDENT reason the square is 2x2?")
print("="*68)
print("""
  Candidate (from notes): 2x2 = (2 outcomes) x (2 parties: Alice, Bob) = binarity.
  Test whether that '2x2' is the SAME 2x2 whose diagonal is the bound.

  CHSH structure: 2 parties, each with 2 settings, each setting 2 outcomes.
  The number of correlation terms summed is 4 = 2x2 (settings combos). The
  classical bound is 2; the quantum bound is 2sqrt2. The factor between them is
  sqrt2 — and sqrt2 is exactly the diagonal/side ratio of ANY square, regardless
  of size. THAT is the only size-independent geometric fact here.
""")
ratio = (2*np.sqrt(2))/2
print(f"  quantum/classical ratio = 2sqrt2 / 2 = sqrt2 = {ratio:.5f}")
print(f"  square diagonal/side ratio = sqrt2 = {np.sqrt(2):.5f}  -> SAME ratio")
print("""
  HONEST FINDING:
  The size-independent, non-coincidental geometric fact is the RATIO sqrt2, NOT
  the absolute value 2sqrt2. The quantum bound exceeds the classical bound by
  exactly the diagonal-to-side ratio of a square (sqrt2). This does NOT depend on
  choosing s=2 by hand — it holds for any square. So:

    * 'diagonal of a 2x2 square = 2sqrt2' : coincidence (needs s=2 chosen to fit).
    * 'quantum bound / classical bound = sqrt2 = diagonal/side' : NOT a coincidence
      in VALUE — it is the genuine geometric statement, because the classical
      bound is the 'side' (sum of signs, +-1, linear) and the quantum bound is
      the 'diagonal' (cos45 projection). sqrt2 is the projection factor.
""")

print("="*68)
print("VERDICT")
print("="*68)
print("""
  The defensible, non-coincidental claim is about the RATIO, not the number:

    classical bound = 2      (answers are SIGNS +-1: the 'side', linear sum)
    quantum bound   = 2*sqrt2 (answers are PROJECTIONS cos(theta): the 'diagonal')
    ratio = sqrt2 = diagonal/side of a square.

  Geometric reading (motivated, NOT a derivation of the value): going from a
  world of signs to a world of projections multiplies the achievable correlation
  by exactly the square's diagonal/side ratio, sqrt2. The '2x2' is the count of
  CHSH terms (2 parties x 2 settings); the sqrt2 is the sign->projection upgrade.

  What stays a COINCIDENCE: that the absolute number 2sqrt2 equals the diagonal of
  a side-2 square. The side length 2 is the classical bound, not an input geometry,
  so 'half a figure-eight through a 2x2 curved space' reproduces the number only
  if its size is set to the classical bound by hand.

  STATUS: ratio sqrt2 as sign->projection (diagonal/side) = motivated geometric
  reading, consistent with the real CHSH source (cos45). Loop/figure-eight path
  giving the ABSOLUTE 2sqrt2 = still a coincidence of form, exactly as the old
  note warned. The honest, publishable version is the RATIO statement.
""")
