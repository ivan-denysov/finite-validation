#!/usr/bin/env python3
"""
single_act_vector.py   (supersedes single_act_metric.py)

Where the Tsirelson bound really comes from, and where it does not.

WHAT WE FIRST GOT WRONG, and record as a lesson.
    An earlier version of this argument said: "the differentiation count D, coming
    from one act, obeys the parallelogram law; a metric with the parallelogram law
    is the metric of an inner-product space; hence E = cos and CHSH <= 2*sqrt(2)."
    Two things are wrong with that.

    (i) D is not a distance. For +-1 tick-patterns the count of differentiations is
        the SQUARE of the Euclidean distance, up to scale:
            ||p_a - p_b||^2 = 4*N*D(a,b),
        so sqrt(D) is the norm, and the inner-product structure of {+-1}^N is
        present already: E = <p_a,p_b>/N = 1 - 2D. An identity, not an axiom.

    (ii) Worse: the parallelogram law does NOT separate 2 from 2*sqrt(2). A local
        hidden-variable model represents its answers as +-1-valued functions
        A_a(lam), B_b(lam) -- unit vectors of L^2(lam). The parallelogram law holds
        for them, and Cauchy-Schwarz bounds their CHSH by 2*sqrt(2) as well. Their
        real bound is 2, and it comes from a POINTWISE fact:
            |B_b(lam) - B_b'(lam)| + |B_b(lam) + B_b'(lam)| = 2   for every lam,
        because the values are +-1. Integrating gives Bell's 2.

WHAT ACTUALLY CARRIES THE DERIVATION.
    Tsirelson's vector model: the settings of one act are represented by
    UNCONSTRAINED unit vectors u_a, v_b of a real inner-product space, with
        E(a,b) = <u_a, v_b>.
    The word that does the work is "unconstrained": not pointwise-+-1 records
    carried apart, but directions established in one act. Then

        S = |<u_a, v_b - v_b'> + <u_a', v_b + v_b'>|
          <= ||v_b - v_b'|| + ||v_b + v_b'||          (Cauchy-Schwarz)
          <= 2*sqrt(2)                                 (parallelogram + concavity)

    where the parallelogram law is now a THEOREM about inner-product spaces, not a
    hypothesis about D. The bound is attained at 0, pi/2 against pi/4, 3pi/4.

    In the picture's own terms the licence to drop the pointwise +-1 constraint is
    exactly what indivisibility of the act and value-indefiniteness (Kochen-Specker)
    buy: there is no pre-assigned sign to be carried, and a local sign-readout of
    pre-distributed data lands on exactly 2 (see local_readout_arcsin.py).

PR-BOX.
    In the vector model the box demands E(a,b)=E(a,b')=E(a',b)=+1 and E(a',b')=-1.
    For unit vectors E=+1 forces coincidence, and coincidence is transitive:
    u_a=v_b, u_a=v_b', u_a'=v_b give v_b'=v_b and u_a'=v_b, so E(a',b')=+1, not -1.
    The box is excluded by the SAME axiom that gives the bound -- not by
    no-signalling (the box is no-signalling) and not by the parallelogram law
    (the local model satisfies it).

STATUS. The vector axiom is a postulate, named. If it fails, the bound reverts
to 2 and PR-boxes are not excluded.

Standalone: python3 single_act_vector.py    (seeded)
"""
import numpy as np


def hamming_is_squared_euclidean(n=1000, seed=0):
    rng = np.random.default_rng(seed)
    x = rng.choice([-1, 1], n)
    y = rng.choice([-1, 1], n)
    d = np.mean(x != y)
    return d, float(np.sum((x - y) ** 2)), 4 * n * d, float(np.dot(x, y)), n * (1 - 2 * d)


def classical_parallelogram(m=200_000, seed=1):
    """A local +-1 model also has unit vectors and obeys the parallelogram law."""
    rng = np.random.default_rng(seed)
    b, bp = rng.choice([-1, 1], m), rng.choice([-1, 1], m)
    ip = lambda u, v: float(np.mean(u * v))
    par = ip(b - bp, b - bp) + ip(b + bp, b + bp)
    cs = np.sqrt(ip(b - bp, b - bp)) + np.sqrt(ip(b + bp, b + bp))
    pointwise = np.unique(np.abs(b - bp) + np.abs(b + bp))
    return par, cs, pointwise


def chsh_vector_model():
    th = [0.0, np.pi / 2, np.pi / 4, 3 * np.pi / 4]
    u = [np.array([np.cos(t), np.sin(t)]) for t in th]
    return abs(u[0] @ u[2] - u[0] @ u[3] + u[1] @ u[2] + u[1] @ u[3])




def components_bound(alphabet, n_dim):
    """Max CHSH over normalised vectors whose components lie in `alphabet`."""
    import itertools
    vs = [np.array(v, float) for v in itertools.product(alphabet, repeat=n_dim) if any(v)]
    vs = [v / np.linalg.norm(v) for v in vs]
    best = 0.0
    for a, ap, b, bp in itertools.product(vs, repeat=4):
        s = abs(a @ b + a @ bp + ap @ b - ap @ bp)
        best = max(best, s)
    return best


def native_directions_2d():
    """Directions (degrees) of the ternary vectors in the transverse plane."""
    import itertools
    vs = [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=2) if any(v)]
    return sorted({round(np.degrees(np.arctan2(v[1], v[0])) % 360, 6) for v in vs})


if __name__ == "__main__":
    d, e2, four_nd, ip, n1m2d = hamming_is_squared_euclidean()
    print("1) The count is a SQUARED distance, and E is an inner product\n")
    print(f"   D = {d:.4f}")
    print(f"   ||x-y||^2 = {e2:.0f}     4*N*D = {four_nd:.0f}     equal: {abs(e2-four_nd)<1e-9}")
    print(f"   <x,y> = {ip:.0f}          N(1-2D) = {n1m2d:.0f}     equal: {abs(ip-n1m2d)<1e-9}")

    par, cs, pw = classical_parallelogram()
    print("\n2) The parallelogram law does NOT separate classical from quantum\n")
    print(f"   local +-1 model:  ||B-B'||^2 + ||B+B'||^2 = {par:.4f}   (= 4: parallelogram holds)")
    print(f"   Cauchy-Schwarz bound on its CHSH        = {cs:.4f}   (<= 2sqrt2 = {2*np.sqrt(2):.4f})")
    print(f"   but pointwise |B-B'| + |B+B'| = {pw}  -> CHSH <= 2 (Bell)")
    print("   => the pointwise +-1 constraint, not the geometry, costs the classical")
    print("      model its sqrt(2).")

    print("\n3) The vector model attains the bound\n")
    print(f"   unconstrained unit vectors: CHSH = {chsh_vector_model():.6f} = 2sqrt2")

    print("\n4) PR-box excluded by the same axiom\n")
    print("   E=+1 forces coincidence; coincidence is transitive; the box's four")
    print("   demands are inconsistent. Not by no-signalling, which it respects.")
    print("\n5) What 'unconstrained' minimally means: a zero component\n")
    for n in (2, 3):
        b1 = components_bound((-1, 1), n)
        b3 = components_bound((-1, 0, 1), n)
        print(f"   dim {n}: components in {{-1,+1}}  -> max CHSH = {b1:.6f}")
        print(f"          components in {{-1,0,+1}} -> max CHSH = {b3:.6f}"
              f"{'  = 2sqrt2' if abs(b3 - 2*np.sqrt(2)) < 1e-9 else ''}")
    print("\n   Reason: with +-1 components, |b_i+b'_i| + |b_i-b'_i| = 2 at every")
    print("   component -- Bell's own pointwise identity -- so CHSH <= 2 identically.")
    print("   One zero component breaks it. Silence in OUTCOMES lifts nothing;")
    print("   a zero in a SETTING's representation is part of the licence that does.")

    print("\n6) The act's minimal dictionary is the 45-degree grid\n")
    print(f"   ternary directions in the transverse plane: {native_directions_2d()}")
    print(f"   max CHSH over exactly those eight: {components_bound((-1,0,1),2):.6f} = 2sqrt2")
    print("   The saturating configuration is not chosen; it is native.")

