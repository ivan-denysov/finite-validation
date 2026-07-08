#!/usr/bin/env python3
"""
single_act_metric.py

From the single-act metric to the Tsirelson bound, and the exclusion of the PR-box.

AXIOM (named, load-bearing). The two tick-patterns of an entangled pair are born
in ONE undivided act. The differentiation count between patterns therefore behaves
as a METRIC on the act's pattern space (parallelogram law / Gram structure):
distances D(x,y) are symmetric, vanish iff the patterns are identical, and satisfy
the triangle inequality.

CONSEQUENCE 1 (Tsirelson). A metric with the parallelogram law embeds in an inner-
product space; settings become unit vectors and E(a,b) = cos(theta_ab). The CHSH
functional over unit vectors attains its maximum 2*sqrt(2).

CONSEQUENCE 2 (PR-box excluded). The Popescu-Rohrlich box requires
    D(a,b) = D(a,b') = D(a',b) = 0  and  D(a',b') = 1.
But D = 0 means the patterns are identical. Identity is transitive: from a = b,
a = b' and a' = b it follows that a' = b and b' = a, hence D(a',b') = D(b,a) =
D(a,b) = 0, contradicting the required value 1. The PR-box is inconsistent with a
metric arising from one act. It is the COUNT axiom that forbids it.

NEGATIVE RESULT (stated honestly). Relationality plus no-signalling ALONE do not
endow D with a metric structure, and do not forbid PR-boxes; the PR-box is
no-signalling. The single-act axiom carries the load and must be defended, not
merely asserted.

Status: Consequence 1 -- derived from the axiom (Tsirelson's theorem is taken
mathematics and is consistent with it). Consequence 2 -- derived. The axiom
itself -- postulate, named.

Standalone: python3 single_act_metric.py    (deterministic)
"""
import numpy as np
from itertools import product


def chsh_from_angles(a, ap, b, bp):
    e = lambda x, y: np.cos(x - y)
    return abs(e(a, b) - e(a, bp) + e(ap, b) + e(ap, bp))


def max_chsh_unit_vectors():
    """CHSH at the analytic optimum, given E = cos(angle) (unit-vector settings)."""
    a, ap, b, bp = 0.0, np.pi / 2, np.pi / 4, 3 * np.pi / 4
    return chsh_from_angles(a, ap, b, bp)


def pr_box_metric_contradiction():
    """
    Check the transitivity argument symbolically over a tiny pattern space.
    D(x,y) = 0  <=>  x == y. Enumerate label assignments consistent with
    D(a,b)=D(a,bp)=D(ap,b)=0 and test whether D(ap,bp)=1 is achievable.
    """
    labels = range(3)  # any finite set suffices; identity is what matters
    achievable = []
    for a, ap, b, bp in product(labels, repeat=4):
        if a == b and a == bp and ap == b:          # the three D = 0 constraints
            d_apbp = 0 if ap == bp else 1
            achievable.append(d_apbp)
    return set(achievable)


if __name__ == "__main__":
    print("1) Tsirelson from the single-act metric (E = cos):")
    s = max_chsh_unit_vectors()
    print(f"   CHSH at the optimal settings = {s:.6f}")
    print(f"   2*sqrt(2)                    = {2*np.sqrt(2):.6f}")
    print()

    print("2) PR-box against metric transitivity:")
    vals = pr_box_metric_contradiction()
    print(f"   Values of D(a',b') consistent with the three D=0 constraints: {sorted(vals)}")
    if vals == {0}:
        print("   The PR-box requires D(a',b') = 1. Not achievable. PR-box EXCLUDED.")
    else:
        print("   WARNING: transitivity argument failed; re-examine.")
    print()

    print("3) Honest negative result:")
    print("   A PR-box is no-signalling. Hence no-signalling alone cannot exclude it.")
    print("   The exclusion above uses the single-act metric axiom, which is the")
    print("   load-bearing postulate of the derivation. [Status: postulate, named.]")
