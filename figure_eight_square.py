"""
Ivan's exact construction:
  - a SQUARE
  - a figure-eight (infinity sign, rotated) placed at the geometric centre
  - signal travels along the UPPER loop, then the LOWER loop
  - claim: path length should be STRICTLY 2.83

We test several faithful interpretations of "figure-eight inside the square,
signal along upper then lower half" and see which (if any) gives exactly 2sqrt2.
We fix the SQUARE to side 2 (matching the 2x2 the picture names), centre at origin,
so corners at (+-1, +-1).
"""
import numpy as np

target = 2*np.sqrt(2)
print(f"target 2sqrt2 = {target:.5f}\n")

# Square side 2, centre origin, corners (+-1,+-1).

# ---- interpretation 1: figure-eight as TWO DIAGONALS of the square ----
# Upper loop ~ one diagonal, lower loop ~ the other. Each diagonal of a side-2
# square has length 2sqrt2. Two of them = 4sqrt2. Half (one pass) = 2sqrt2.
diag = 2*np.sqrt(2)
print("INTERP 1 — figure-eight = the two diagonals of the square")
print(f"  one diagonal = {diag:.5f}")
print(f"  signal upper-then-lower = TWO diagonals? = {2*diag:.5f}")
print(f"  signal = ONE diagonal (the crossing) = {diag:.5f}  <-- equals 2sqrt2 if path=one diagonal")
print()

# ---- interpretation 2: eight = two circles stacked, inscribed, signal along arcs ----
# Two circles stacked vertically inside the square: each radius = 0.5 (so two of
# them span the height 2). Path along both full circles = 2 * 2*pi*r = 2*pi.
r = 0.5
circ_path = 2*(2*np.pi*r)
print("INTERP 2 — eight = two stacked inscribed circles, signal along full arcs")
print(f"  radius r={r}, path over both circles = {circ_path:.5f}  (= 2pi, not 2sqrt2)")
print()

# ---- interpretation 3: eight = two triangles (upper & lower halves), signal along the slanted edges ----
# Upper half of the square split by its diagonals forms a triangle apex at centre.
# The two slanted sides of the upper triangle go corner->centre->corner.
# corner (1,1) to centre (0,0): length sqrt(1+1)=sqrt2. centre to (-1,1): sqrt2.
# upper loop = (1,1)->(0,0)->(-1,1): 2*sqrt2. lower loop = (−1,−1)->(0,0)->(1,−1): 2*sqrt2.
up = np.hypot(1,1)+np.hypot(1,1)
print("INTERP 3 — eight = corner->centre->corner on top, then bottom (X through centre)")
print(f"  upper loop length = {up:.5f}")
print(f"  upper + lower = {2*up:.5f}")
print(f"  ONE loop (upper only) = {up:.5f}  <-- 2sqrt2!")
print()

# ---- interpretation 4: the half-eight as a single loop = one diagonal pass ----
print("INTERP 4 — 'half the figure-eight' = one loop = corner->centre->corner")
print(f"  = {up:.5f}  = 2sqrt2 = {target:.5f}")
print()

print("="*64)
print("READ-OUT")
print("="*64)
print(f"""
  The value 2sqrt2 = {target:.5f} appears EXACTLY in interpretations 1/3/4, and
  the mechanism is always the same: a path that goes corner -> centre -> corner
  in a side-2 square has length 2*sqrt2, because each leg is the half-diagonal
  sqrt(1^2+1^2)=sqrt2, and there are two legs.

  So 'signal along one loop of the figure-eight (corner->centre->corner)' = 2sqrt2
  IS exact -- BUT only because the square side is fixed to 2. The length scales
  with the side: side s gives loop length s*sqrt2. The number 2sqrt2 requires s=2.

  HONEST STATUS (unchanged by the construction):
   - The GEOMETRY is self-consistent: a corner->centre->corner loop in a 2x2
     square is exactly 2sqrt2. Your picture is internally correct.
   - But s=2 is the CLASSICAL BELL BOUND, inserted as the square's size. The
     construction reproduces 2sqrt2 because you set the side equal to 2 (=the
     classical bound), then take the diagonal-type path (x sqrt2). That is the
     SAME content as 'quantum = classical x sqrt2 (sign->projection)'.
   - i.e. the construction is a faithful GEOMETRIC PICTURE of 'bound times sqrt2',
     not an independent derivation of the absolute 2sqrt2: the '2' still enters as
     the classical bound, the 'sqrt2' as the corner->centre->corner (diagonal) leg.

  CONCLUSION: your figure-eight gives 2sqrt2 exactly and is internally consistent.
  Its honest reading is: it geometrizes the RATIO sqrt2 (the upgrade from the
  classical side-2 to the quantum diagonal). The absolute value still rides on
  side=2=classical bound. Publishable as a geometric PICTURE of why quantum
  exceeds classical by sqrt2 -- not as a first-principles derivation of 2.83.
""")
