"""
Can the SIDE = 2 be obtained INDEPENDENTLY of Bell's answer?
If yes, the figure-eight (side x sqrt2) derives 2sqrt2 from first principles.
If the '2' can only come from assuming the Bell bound, it stays a picture.

Candidate: 2 = (2 outcomes) x (2 parties)? or 2 = max of a sum of signs?
We test by DERIVING the classical CHSH bound from scratch and watching where
the '2' actually comes from.
"""
import numpy as np
import itertools

print("="*66)
print("Derive the classical CHSH bound from binarity alone")
print("="*66)
print("""
CHSH: S = E(a,b) - E(a,b') + E(a',b) + E(a',b').
Local hidden variables: each party's outcome is a predetermined sign +-1 for
each setting. Alice has A,A' in {+-1}; Bob has B,B' in {+-1}.
Then S_lhv = A*B - A*B' + A'*B + A'*B' = A(B-B') + A'(B+B').
Since B,B' in {+-1}: one of (B-B'),(B+B') is 0 and the other is +-2.
So S_lhv = +-2 * (a sign) -> |S_lhv| <= 2, EXACTLY.
""")
# brute-force confirm over all sign assignments
vals=set()
for A,Ap,B,Bp in itertools.product([-1,1],repeat=4):
    S = A*B - A*Bp + Ap*B + Ap*Bp
    vals.add(S)
print(f"  all possible S over +-1 assignments: {sorted(vals)}")
print(f"  max |S| = {max(abs(v) for v in vals)}")
print("""
WHERE DOES THE 2 COME FROM?
  The '2' is the value of (B+B') or (B-B') when both are signs: +-1 +-(+-1) hits
  +-2. So 2 = the maximum of a SUM OF TWO SIGNS. That is binarity: two parties'
  binary answers add to at most 2. The 2 is NOT borrowed from a separately-known
  Bell answer -- it FALLS OUT of '4 terms of +-1 products collapse to 2 signs',
  i.e. of the 2-settings-x-2-outcomes structure.
""")

print("="*66)
print("So: is side=2 independent of the Bell answer?")
print("="*66)
print("""
  YES, partially -- and this is the honest, important distinction:

  The classical bound 2 is itself DERIVED from binarity (sum of two +-1 signs
  maxes at 2). It is not a free input; it is forced by '2 settings, outcomes +-1'.
  So using side=2 is NOT circular against Bell's EXPERIMENT -- it is using the
  classical (LHV) bound, which is a theorem of binarity, not an empirical number.

  THEN the quantum value is side x sqrt2 = 2 x sqrt2:
    - side 2   = classical bound = max sum of two binary signs (DERIVED, binarity)
    - x sqrt2  = the corner->centre->corner (diagonal) leg of the loop, i.e. the
                 upgrade from SIGN (+-1, the side) to PROJECTION (cos45, the diagonal)

  What is STILL assumed (the remaining gap, stated honestly):
    that the quantum upgrade is exactly the DIAGONAL (sqrt2) and not some other
    factor. Geometrically: why does going quantum take the path corner->centre->
    corner (diagonal) rather than along the side? The figure-eight ASSERTS this
    (signal runs the loop's diagonal legs), it does not derive that the quantum
    path must be the diagonal. Tsirelson's theorem proves sqrt2 is the max from
    quantum (Hilbert-space) structure; our picture matches it but does not replace
    that proof.
""")

print("="*66)
print("VERDICT (honest, no stretching)")
print("="*66)
print("""
  PROGRESS: the side '2' is NOT a circular insertion of Bell's empirical answer.
  It is the classical CHSH bound, which is itself a THEOREM of binarity (sum of
  two +-1 signs <= 2). Confirmed by brute force above. So one of the two factors
  is genuinely derived from first principles (binarity).

  REMAINING GAP: the factor sqrt2 (sign -> projection, side -> diagonal). The
  figure-eight picture POSITS the diagonal path; Tsirelson PROVES sqrt2 from
  Hilbert-space geometry. Our construction is consistent with that proof but is
  not an independent derivation of WHY the quantum upgrade is exactly the diagonal.

  NET STATUS of '2sqrt2 from the figure-eight':
    side 2      -> DERIVED (binarity: max sum of two signs)
    x sqrt2     -> MOTIVATED geometric picture (diagonal leg), matching Tsirelson,
                   not an independent proof that the quantum factor must be sqrt2.
  => stronger than 'pure coincidence': half of it (the 2) is now first-principles.
     The honest claim: 2sqrt2 = (binarity bound 2) x (diagonal upgrade sqrt2),
     where the upgrade is a geometric picture consistent with Tsirelson's theorem.
""")
