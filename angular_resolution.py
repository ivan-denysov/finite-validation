#!/usr/bin/env python3
"""
angular_resolution.py

If the comparison at the lock resolves directions only on a grid, what residual does
the picture predict against the exact cosine -- and where can it be looked for?

SETUP. Grid spacing g radians; K = 2*pi/g directions per full turn. The measured
correlation is the cosine of the nearest grid angle:

    residual(theta) = | cos(theta_grid) - cos(theta) |

FIRST ORDER, NOT SECOND. Expanding,

    residual(theta)  ~=  |sin(theta)| * g/2,      max over theta = g/2 = pi/K,

attained near theta = pi/2. A WITHDRAWN earlier estimate used the second-order form
(g/2)^2/2, which is valid only near theta = 0 and theta = pi, where the cosine is
flat. The bounds K >= 64 (at 1e-3) and K >= 256 (at 1e-4) followed from that error
and are withdrawn. The correct bound is K >~ pi/eps for agreement at level eps --
an order of magnitude tighter.

THE SIGNATURE, AND WHERE IT CANNOT BE SEEN. The residual vanishes identically ON
the grid angles and peaks one half-step away. But the minimal dictionary of the act
-- settings in the transverse plane with components in {-1,0,+1} -- has exactly
eight directions, at 0, 45, ..., 315 degrees, and the CHSH-optimal settings
(0, pi/2 against pi/4, 3pi/4) all lie on that grid. Hence:

    the residual is EXACTLY ZERO at the CHSH optimum,

and S = 2*sqrt(2) exactly for any resolution containing that grid. A precision Bell
test at the optimal angles carries no information about K whatsoever. The handle is
a scan of E(theta) at GENERIC angles, where the residual is periodic and
phase-locked to the grid -- a shape, not a noise floor.

Status: the first-order form and the zeros are derived; the scale of K is not
predicted. What would break the picture is a residual of the wrong shape.

Standalone: python3 angular_resolution.py    (deterministic)
"""
import itertools
import numpy as np


def residual(theta, g):
    """|cos(nearest grid angle) - cos(theta)| for a grid of spacing g."""
    return np.abs(np.cos(np.round(theta / g) * g) - np.cos(theta))


def max_residual(g, n=200_001):
    th = np.linspace(0.0, np.pi, n)
    r = residual(th, g)
    i = int(np.argmax(r))
    return float(r[i]), float(th[i])


def native_directions():
    """Directions of the ternary vectors in the transverse plane, in degrees."""
    vecs = [np.array(p, float) for p in itertools.product((-1, 0, 1), repeat=2) if any(p)]
    return sorted({round(np.degrees(np.arctan2(v[1], v[0])) % 360, 6) for v in vecs})


if __name__ == "__main__":
    print("1) The residual is FIRST order in the grid spacing\n")
    print(f"   {'g (rad)':>9} {'max residual':>14} {'g/2':>12} {'(g/2)^2/2':>13} {'argmax/pi':>11}")
    for g in (0.2, 0.1, 0.05, 0.02, 0.01):
        r, a = max_residual(g)
        print(f"   {g:>9.3f} {r:>14.4e} {g/2:>12.4e} {(g/2)**2/2:>13.4e} {a/np.pi:>11.3f}")
    print("\n   max residual = g/2 = pi/K, near theta = pi/2. The second-order form")
    print("   (g/2)^2/2 is off by an order and holds only at the cosine's flat points.\n")

    print("2) Correct bounds on K\n")
    for eps in (1e-3, 1e-4):
        print(f"   agreement at {eps:.0e}  ->  g <~ {2*eps:.2e} rad  ->  K >~ {np.pi/eps:.3g}")
    print("   (the withdrawn numbers were 64 and 256)\n")

    print("3) The native directions of the act's minimal dictionary\n")
    print(f"   {native_directions()}")
    print("   -- the 45-degree grid, and it contains the CHSH-optimal settings.\n")

    print("4) The residual at the CHSH optimum\n")
    g = np.pi / 4
    opt = np.array([0.0, np.pi / 2, np.pi / 4, 3 * np.pi / 4])
    print(f"   {'pair':>7} {'theta (deg)':>12} {'residual':>12}")
    for i, j in ((0, 2), (0, 3), (1, 2), (1, 3)):
        th = abs(opt[i] - opt[j])
        print(f"   {f'{i}-{j}':>7} {np.degrees(th):>12.1f} {residual(th, g):>12.2e}")
    r, a = max_residual(g)
    print(f"\n   exactly zero at every optimal pair; the maximum on this grid is"
          f" {r:.4f} at {np.degrees(a):.2f} deg,")
    print("   one half-step (22.5 deg) from a native angle.\n")
    print("   => a precision Bell test at the optimal angles can neither confirm nor")
    print("      refute the discreteness of the act. Scan E(theta) at generic angles.")
