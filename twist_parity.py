#!/usr/bin/env python3
"""
twist_parity.py

The double cover, and which Z_2 actually carries spin.

TWO DISTINCT Z_2's, AND AN EARLIER VERSION OF THIS FILE CONFUSED THEM.

  (A) MOEBIUS PARITY: the number of HALF-twists of a closed band, mod 2. Odd makes
      a Moebius band (non-orientable, one edge); even an ordinary annulus. A real
      topological invariant -- and NOT the one that carries spin.

  (B) THE BELT-TRICK CLASS: rotate one end of a ribbon by 2*pi and you insert one
      FULL twist, i.e. TWO half-twists. With the far end HELD, no isotopy removes
      it; 4*pi inserts two full twists and those it does remove. This is
      pi_1(SO(3)) = Z_2, the double cover -- taken mathematics (Staley 2010).

  A 2*pi rotation adds half-twists two at a time, so it NEVER changes the Moebius
  parity. (A) cannot detect (B). It is (B) that carries spin, and (B) exists only
  where the ties are HELD.

WHAT THIS MEANS FOR THE PICTURE.
  Free one end and the belt trick evaporates: any twist slides off, every
  configuration is isotopic to the untwisted one, and the exchange sign can only
  be +1. So the relevant question is not "is the ribbon closed?" but "are its ties
  held long enough to hold a twist?" -- that is, do the links have MEMORY.

    massive  = a closed mode. It sits on its nodes; the same ties persist while its
               packet circulates, and the network holds their far ends. A 2*pi
               rotation traps a full twist. The fermionic option exists.

    massless = a transfer. Received, passed on; at every step the links are new.
               Nothing is held, so nothing can hold a twist. THE PICTURE SUPPLIES
               NO FERMIONIC OPTION. The exchange sign can only be +1.

  That massless therefore implies BOSON follows on a further premise, named in the
  text: in three dimensions the exchange sign is +-1, and this picture offers no
  route to -1 other than a trapped twist. Grant the picture is complete about
  statistics and the implication holds; refuse it, and the narrower structural
  statement above remains -- itself falsifiable, since a fundamental massless
  fermion would be a thing this picture cannot accommodate.

  Spin-to-statistics is Finkelstein-Rubinstein (1968): the exchange of two
  identical solitons is homotopic to a 2*pi rotation of one. Taken theorem; its
  premise (a soliton whose configuration space carries the two-valuedness of 3D
  rotations) is NOT established by the programme -- the bridge exhibits only a
  one-dimensional kink, which has no rotation group for the double cover to act on.

WITHDRAWN. An earlier version of this file stated that "a closed ribbon's half-twist
parity" is the belt trick, and derived massless => boson from the absence of a
closed ribbon. Both are corrected above.

Standalone: python3 twist_parity.py   (deterministic)
"""
import numpy as np


def unit_quaternion(axis, angle):
    """Quaternion (w, x, y, z) for a rotation by `angle` about `axis`."""
    a = np.asarray(axis, dtype=float)
    a = a / np.linalg.norm(a)
    return np.concatenate([[np.cos(angle / 2.0)], np.sin(angle / 2.0) * a])


def rotation_sign(angle, axis=(0, 0, 1), tol=1e-9):
    """Sign carried by the double cover after rotating by `angle`."""
    w = unit_quaternion(axis, angle)[0]
    if abs(w) < tol:
        return 0
    return int(np.sign(w))


if __name__ == "__main__":
    print("1) Double cover (Dirac belt): sign after rotation by n*pi\n")
    for n in (0, 1, 2, 3, 4):
        s = rotation_sign(n * np.pi)
        note = ""
        if n == 2:
            note = "   <- 2*pi returns -1 (fermionic)"
        if n == 4:
            note = "   <- 4*pi returns +1 (identity)"
        print(f"   {n}*pi : sign = {s:+d}{note}")

    print("\n2) Which Z_2 carries spin\n")
    print("   Moebius parity (half-twists mod 2): a real invariant, but a 2*pi")
    print("      rotation adds half-twists two at a time and never changes it.")
    print("   Belt-trick class (full twists mod 2): pi_1(SO(3)) = Z_2. It exists")
    print("      only where the far end is HELD. Free the end and any twist")
    print("      slides off; the class collapses.")

    print("\n3) Consequences for the network picture\n")
    print("   massive  -> a closed mode sits; its ties are held -> a twist is trapped")
    print("            -> the fermionic option exists; which parity is NOT derived")
    print("   massless -> a transfer; its links are renewed each step -> nothing held")
    print("            -> NO FERMIONIC OPTION IS SUPPLIED; exchange sign +1 only")
    print("            -> massless => boson, on the named premise that this picture")
    print("               is complete about statistics")
    print()
    print("   Statistics follows from spin by Finkelstein-Rubinstein (1968):")
    print("   exchange of two identical solitons ~ 2*pi rotation of one.")
    print("   [taken theorem; applies to solitons of a field description]")
