#!/usr/bin/env python3
"""
born_from_count.py

Where the Born value comes from, and what is still owed.

THE CLAIM. For a two-outcome projective measurement the Born probability is not an
independent postulate: it is the differentiation fraction of the count.

    E(a,b) = cos(theta)        [from the single-act metric, see single_act_metric.py]
    E      = 1 - 2D            [identity, see correlation_identity.py]
    =>  D  = (1 - cos theta)/2 = sin^2(theta/2)

which is exactly the Born value. The SQUARE in Born's rule is the half-angle
identity of the projection -- the same structure that makes the correlation a
cosine. "Probability" here is a normalised COUNT of differentiations, not an extra
primitive.

NOT CIRCULAR: E = cos(theta) came from a counting axiom, not from probability;
D = (1-E)/2 is an identity.

DIMENSION 2 vs DIMENSION >= 3.

  In dim 2 every rank-1 projector has exactly one orthogonal partner, so the only
  constraint on a frame function is mu(n) + mu(-n) = 1. Many non-Born measures
  satisfy it -- e.g. mu(n) = (1 + n_z^3)/2. Gleason's theorem therefore cannot
  single out Born in dim 2. This is standard, and is demonstrated below.

  In dim >= 3 each ray belongs to infinitely many orthogonal triples; additivity
  across all of them overconstrains the frame function and forces mu(P) = tr(rho P).
  That is Gleason (1957). Busch (2003) extends the result to effects (POVMs), and
  reaches dim 2 as well.

DIVISION OF LABOUR.

    dim 2 (qubit)   -> direct count: D = sin^2(theta/2)     [derived in the picture]
    dim >= 3        -> Gleason: mu(P) = tr(rho P)           [taken theorem]
    POVMs           -> Busch                                 [taken theorem]

  The two cover exactly each other's blind spots. Additivity, which Gleason
  requires, is not an extra assumption here: D is a count, and counts are additive
  over disjoint sets of ticks. Note also that non-contextuality of the MEASURE
  (Gleason's premise) is a different statement from non-contextuality of VALUES
  (which Kochen-Specker forbids); there is no conflict.

WHAT REMAINS OWED. The axiom supplies an inner product on the pattern space of the
act. Born's rule concerns the Hilbert space of the system. Identifying the two is
natural but is not proved here. That isomorphism is the residual debt -- narrower
than "the Born rule is postulated", and named.

Standalone: python3 born_from_count.py    (seeded)
"""
import numpy as np


def born_value_from_count(theta):
    """D = (1 - cos theta)/2, the differentiation fraction."""
    return (1.0 - np.cos(theta)) / 2.0


def bloch(theta, phi=0.0):
    return np.array([np.sin(theta) * np.cos(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(theta)])


def random_orthonormal_basis(seed):
    rng = np.random.default_rng(seed)
    q, _ = np.linalg.qr(rng.standard_normal((3, 3)))
    return [q[:, i] for i in range(3)]


if __name__ == "__main__":
    print("1) The Born value is the differentiation fraction\n")
    print(f"   {'theta(deg)':>10} {'D=(1-cos)/2':>14} {'sin^2(theta/2)':>16} {'equal':>7}")
    for deg in (0, 45, 60, 90, 120, 180):
        th = np.radians(deg)
        d = born_value_from_count(th)
        s2 = np.sin(th / 2) ** 2
        print(f"   {deg:>10} {d:>14.8f} {s2:>16.8f} {str(abs(d - s2) < 1e-12):>7}")

    print("\n2) Why Gleason cannot reach dimension 2\n")
    mu_born = lambda n: (1 + n[2]) / 2
    mu_other = lambda n: (1 + n[2] ** 3) / 2      # also a valid dim-2 frame function
    print(f"   {'theta(deg)':>10} {'Born(n)+Born(-n)':>20} {'other(n)+other(-n)':>22}")
    for deg in (0, 30, 60, 90, 120):
        n = bloch(np.radians(deg))
        print(f"   {deg:>10} {mu_born(n) + mu_born(-n):>20.6f} "
              f"{mu_other(n) + mu_other(-n):>22.6f}")
    print("   Both satisfy the ONLY dim-2 constraint -> Born is not singled out.")

    print("\n3) Why dimension >= 3 forces Born\n")
    psi = np.array([1.0, 0.0, 0.0])
    mu_born3 = lambda v: abs(np.dot(psi, v)) ** 2
    mu_quartic = lambda v: abs(np.dot(psi, v)) ** 4
    print(f"   {'basis':>6} {'sum of Born':>14} {'sum of |.|^4':>16}")
    for s in range(5):
        b = random_orthonormal_basis(s)
        print(f"   {s:>6} {sum(mu_born3(v) for v in b):>14.6f} "
              f"{sum(mu_quartic(v) for v in b):>16.6f}")
    print("   Additivity over every orthogonal triple holds only for Born.")

    print("\n4) Division of labour\n")
    print("   dim 2      -> direct count   D = sin^2(theta/2)   [derived]")
    print("   dim >= 3   -> Gleason        mu(P) = tr(rho P)     [taken]")
    print("   POVMs      -> Busch (2003)                          [taken]")
    print("\n5) Residual debt: pattern space of the act  <-->  Hilbert space of the")
    print("   system. Natural, not proved. [named]")
