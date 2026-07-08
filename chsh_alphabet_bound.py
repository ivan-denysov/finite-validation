#!/usr/bin/env python3
"""
chsh_alphabet_bound.py

Question: does enlarging the outcome alphabet from binary {-1,+1} to ternary
{-1,0,+1} ("silence") raise the CHSH bound for local models?

Method: exhaustive enumeration of ALL deterministic local strategies (the extreme
points of the local polytope). The CHSH maximum over convex mixtures equals the
maximum over extreme points, so enumeration is a proof, not a sample.

Result: max CHSH = 2 for BOTH alphabets.

Status: REJECTED — the claim "the quantum excess 2 -> 2*sqrt(2) lives in the
silence (sparsity of questions)" is false. Zeros dilute |E|; they never lift the
bound. The excess requires (i) values not pre-assigned (Kochen-Specker /
value-indefiniteness) and (ii) the single-act metric structure on the
differentiation count. See single_act_metric.py.

Note: the general theorem is stronger than this enumeration. For ANY local
hidden-variable model with outcomes in the interval [-1,+1], CHSH <= 2. The
ternary alphabet is a subset of [-1,+1], hence bounded. The enumeration below
merely exhibits it.

Standalone: python3 chsh_alphabet_bound.py   (no seed needed; deterministic)
"""
import itertools


def chsh(e_ab, e_abp, e_apb, e_apbp):
    return abs(e_ab - e_abp + e_apb + e_apbp)


def max_chsh_over_deterministic(alphabet):
    """Enumerate all deterministic local strategies A(a),A(a'),B(b),B(b')."""
    best = 0.0
    best_arg = None
    for a0, a1, b0, b1 in itertools.product(alphabet, repeat=4):
        s = chsh(a0 * b0, a0 * b1, a1 * b0, a1 * b1)
        if s > best:
            best, best_arg = s, (a0, a1, b0, b1)
    return best, best_arg


if __name__ == "__main__":
    for name, alphabet in [("binary  {-1,+1}", (-1, 1)),
                           ("ternary {-1,0,+1}", (-1, 0, 1))]:
        n = len(alphabet) ** 4
        best, arg = max_chsh_over_deterministic(alphabet)
        print(f"{name}: {n:>3} deterministic strategies, max CHSH = {best}")
        print(f"   attained at A(a),A(a'),B(b),B(b') = {arg}")

    print()
    print("Both alphabets: max CHSH = 2. Silence does not lift the classical bound.")
    print("Quantum value 2*sqrt(2) = 2.8284... is unreachable by any local")
    print("assignment, ternary or not. [Status: rejected claim, documented.]")
