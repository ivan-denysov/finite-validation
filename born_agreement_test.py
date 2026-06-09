"""
Ivan asks: show the number that is >0 and <1 (the correlation/agreement of two
particles linked through a quantum link). Is it the Born rule, or not?

Ivan's position to test: Born is NOT fundamental; 2sqrt2 came out statistically
from geometry (linear path in normal particles vs path along the edges of the
inverted figure-eight). The agreement of two particles through a quantum link is
a survival condition (without it causal linkage breaks).

We compute the agreement for two observers measuring through ONE quantum link
at relative angle theta, the textbook quantum prediction, and display the
"between 0 and 1" number explicitly. Then we ask honestly: is it Born, and is
Born 'derived' or just 'fitted'.
"""
import numpy as np

print("="*68)
print("The agreement of two measurements through one quantum link")
print("="*68)
print("""
Two parties measure the same entangled link at settings differing by angle theta.
Quantum mechanics predicts the probability that their binary outcomes AGREE:
    P_agree(theta) = cos^2(theta/2)        (for the standard singlet/triplet setup)
This is the Born rule applied to the overlap of the two measurement directions.
It is a number strictly between 0 and 1 for intermediate angles.
""")
print(f"{'theta(deg)':>10} {'P_agree=cos^2(theta/2)':>24} {'note':>20}")
print("-"*56)
for deg in [0,30,45,60,90,120,135,180]:
    th=np.deg2rad(deg)
    P=np.cos(th/2)**2
    note=""
    if deg==0: note="always agree (=1)"
    elif deg==180: note="never agree (=0)"
    elif deg==90: note="half (=0.5)"
    else: note="between 0 and 1"
    print(f"{deg:>10} {P:>24.4f} {note:>20}")

print("""
THERE IS the number Ivan asks for: e.g. theta=60deg -> P_agree = 0.75; theta=90 ->
0.5; theta=120 -> 0.25. Strictly between 0 and 1. This IS what 'something less
than 1, more than 0' looks like operationally: the probability that two linked
measurements agree.
""")

print("="*68)
print("Is this 'Born', and is Born derived or fitted?")
print("="*68)
print("""
- The number cos^2(theta/2) IS the Born rule: probability = |projection|^2 =
  |<psi|phi>|^2. So the 'between 0 and 1' value is exactly Born. Mathematics for
  it EXISTS and is standard.

- BUT: does Born EXPLAIN why it is the SQUARE (cos^2) and not, say, |cos| or
  cos^4? No. Born POSITS probability = amplitude squared. It works, it is not
  derived from deeper principles within standard QM. (Gleason's theorem derives
  Born GIVEN the Hilbert-space + non-contextuality assumptions, but that is
  assuming the very structure in question.) This matches Ivan's instinct: the
  square is fitted/posited, not explained.
""")

# Test Ivan's geometric claim: is cos^2 the 'edge-of-figure-eight' vs 'linear'?
print("="*68)
print("Ivan's geometry claim: linear (normal) vs path-along-edges (quantum)")
print("="*68)
print("""
Classical/linear correlation (signs +-1, linear): E_classical(theta) = 1 - theta/90
(a straight line from +1 at 0deg to -1 at 180deg) -- the 'linear path' picture.
Quantum correlation: E_quantum(theta) = cos(theta) -- a curved (projection) law.
Compare the AGREEMENT probabilities.
""")
print(f"{'theta':>6} {'linear E':>10} {'quantum cos':>12} {'P_agree quantum':>16}")
print("-"*46)
for deg in [0,30,45,60,90,135,180]:
    th=np.deg2rad(deg)
    lin = 1 - deg/90.0          # linear ramp +1 -> -1 over 0..180
    q   = np.cos(th)
    Pag = np.cos(th/2)**2
    print(f"{deg:>6} {lin:>10.3f} {q:>12.3f} {Pag:>16.3f}")
print("""
READ:
- The classical/linear law (straight ramp) and the quantum law (cosine) AGREE at
  the endpoints (0,90,180) but DIFFER in between -- exactly where the 'between 0
  and 1' lives. The quantum curve is the cosine (projection); the classical is the
  straight line (sign/linear). This is consistent with Ivan's 'linear vs path-
  along-edges' intuition: the quantum value follows a curved (projection/cosine)
  law, the classical a straight (linear) one. The gap between them at intermediate
  angles is the genuinely quantum part.
""")

print("="*68)
print("HONEST VERDICT (answering Ivan directly)")
print("="*68)
print("""
1. YES, there is a number strictly between 0 and 1: the agreement probability
   cos^2(theta/2). At 60deg it is 0.75; at 90deg, 0.5; at 120deg, 0.25.

2. That number IS the Born rule (probability = squared projection). So
   mathematics for it EXISTS -- Ivan's 'no math' is too strong; the correct
   statement is 'the math exists (Born) but is POSITED, not derived'.

3. Ivan's deeper instinct is defensible: standard QM does NOT explain WHY the
   square. So 'Born is not fundamental / it is fitted' is a legitimate FOUNDATIONS
   position (this is exactly the Valentini line: Born is emergent, not axiomatic).

4. Ivan's geometry claim (linear in normal vs curved/cosine through the quantum
   link) matches the actual classical-vs-quantum correlation laws: straight ramp
   vs cosine. The intermediate-angle gap is where quantumness sits.

   => The honest framing: the 'between 0 and 1' number is the agreement
      probability; standard QM computes it via Born (squared projection) but does
      not derive the square; UFI's position is that this value reflects a
      synchronisation/survival condition through the quantum link, and that the
      squared form is fitted rather than fundamental (Valentini-aligned). Whether
      UFI can DERIVE the value from the synchronisation condition is OPEN -- not
      shown here.
""")
