"""
Is there a real bridge between the GEOMETRIC PATH LENGTH (corner->centre->corner
= 2sqrt2 in a 2x2 square) and the VALUE OF THE CHSH SUM S = 2sqrt2?
Or is it strictly a numerical coincidence?

We test honestly. S is a sum of FOUR correlations, each a statistical average of
products of +-1 outcomes at relative angles. The "path length" is a single
geometric quantity. We check whether S can be WRITTEN as a path length under any
natural identification, or whether the cos45 in each is a different cos45.
"""
import numpy as np

print("="*68)
print("1. Where 2sqrt2 comes from in CHSH (the real thing)")
print("="*68)
def E(x,y): return -np.cos(x-y)
def chsh(a,ap,b,bp): return E(a,b)-E(a,bp)+E(ap,b)+E(ap,bp)
d=np.pi/180
S = chsh(0, 90*d, 45*d, 135*d)
print(f"S = E(a,b)-E(a,b')+E(a',b)+E(a',b') = {abs(S):.5f}")
print("Structure: 4 correlation terms, each = -cos(angle between settings).")
print("Maximised when each |term| = cos45 = 0.7071, four of them => 4*0.7071 = 2sqrt2.")
print("=> the 2sqrt2 here = 4 x cos(45deg between MEASUREMENT SETTINGS).")
print("   The '45deg' is the optimal angle between Alice/Bob analyzer settings.")
print("   It is DIMENSIONLESS (a correlation value), not a length.")

print()
print("="*68)
print("2. Where 2sqrt2 comes from in the figure-eight path")
print("="*68)
leg = np.hypot(1,1)  # corner (-1,1) to centre (0,0) in side-2 square
print(f"path = corner->centre->corner = 2 x sqrt(1^2+1^2) = {2*leg:.5f}")
print("Structure: 2 legs, each = sqrt2 = diagonal-half of a side-2 square.")
print("=> the 2sqrt2 here = 2 x sqrt2 (a LENGTH in a square of side 2).")
print("   The 'sqrt2' is the diagonal/side ratio. It has units of LENGTH.")

print()
print("="*68)
print("3. Are the two cos45 / sqrt2 the SAME object? (the crux)")
print("="*68)
print("""
CHSH:   2sqrt2 = 4 * cos(45deg)   [45deg = angle between settings; dimensionless]
Path:   2sqrt2 = 2 * sqrt(2)      [sqrt2 = diagonal/side; a length ratio]

4*cos45 = 4*(1/sqrt2) = 4/sqrt2 = 2sqrt2.
2*sqrt2 = 2sqrt2.
Numerically equal. But the DECOMPOSITION differs:
  - CHSH:  FOUR terms x cos45     (4 x 0.7071)
  - Path:  TWO legs x sqrt2       (2 x 1.4142)
The factor structure is 4x0.707 vs 2x1.414. Same product, different factors.
""")
# test: can we map "4 terms" to "2 legs"? 
print("Can '4 correlation terms' be identified with '2 path legs'? Test:")
print(f"  CHSH: 4 terms of magnitude cos45={np.cos(45*d):.4f}")
print(f"  Path: 2 legs of magnitude sqrt2={np.sqrt(2):.4f}")
print(f"  2 legs of sqrt2 = {2*np.sqrt(2):.4f}; 4 terms of cos45 = {4*np.cos(45*d):.4f}")
print("""
  To equate them you must set 2 = 4 (terms vs legs) AND sqrt2 = cos45*2.
  cos45*2 = 1.4142 = sqrt2 -- OK numerically, but this REQUIRES asserting
  '2 legs carry the weight of 4 correlation terms', which is not derived;
  it is imposed to make the totals match.
""")

print("="*68)
print("4. Scale test: is the path length even well-defined as 'S'?")
print("="*68)
print("""
S is dimensionless and bounded: |S| <= 2 (classical), <= 2sqrt2 (quantum),
<= 4 (algebraic max). A path length scales with the square's side: side s gives
2*s/sqrt2... no: side s gives legs s*sqrt2/... -> path = s*sqrt2 per leg pair.
For side=2, path=2sqrt2. For side=4, path=4sqrt2 > 4 = algebraic max of S.
So 'path length' can exceed the algebraic maximum of S (4) while S cannot.
=> path length and S obey DIFFERENT bounds. They are not the same quantity.
""")
side=4
print(f"  side=4 -> path = {side*np.sqrt(2):.3f}, but S can never exceed 4 (algebraic).")
print(f"  {side*np.sqrt(2):.3f} > 4  => path is NOT bounded like S. Different objects.")

print()
print("="*68)
print("HONEST VERDICT")
print("="*68)
print("""
NO physical bridge found between 'path length' and 'value of S':
  - S is dimensionless, a sum of 4 statistical correlations, bounded by 4.
  - path length is a geometric length, scales with the square's side, unbounded.
  - they coincide ONLY at side=2, and only because 4*cos45 = 2*sqrt2 numerically.
  - the decomposition differs (4 terms vs 2 legs); equating them imposes a
    weighting that is not derived.

CONCLUSION: the figure-eight reproduces the NUMBER 2sqrt2 but does NOT represent
the CHSH functional S. The path length is not S. So:
  - the 'sqrt2 = sign->projection upgrade' part is REAL (it is the genuine
    classical-vs-quantum statistics: linear ramp vs cosine), and the '2 from
    binarity' is a genuine theorem;
  - but the FIGURE-EIGHT PATH itself is a visual image of sqrt2, not a physical
    representation of S. Its length has no established physical meaning as a
    correlation value.

=> Variant 3 fails (as suspected). The honest move is Variant 2: keep the real
   content (2 = binarity theorem; sqrt2 = sign-vs-projection statistics) and
   explicitly say the figure-eight is a geometric IMAGE of the sqrt2 factor, not
   a physical path whose length equals S. State that the length<->S link is not
   established and is not claimed.
""")
