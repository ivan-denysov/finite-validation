import numpy as np, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

NAVY="#1f3a5f"; RED="#d1495b"; GREY="#b8bcc2"

fig, ax = plt.subplots(figsize=(5.6,5.8))

# квадрат сторона 2
ax.add_patch(Rectangle((-1,-1),2,2, fill=False, edgecolor=NAVY, linewidth=1.6, zorder=2))

# лежачая восьмёрка (Gerono), как контекст — бледная
t=np.linspace(0,2*np.pi,1500)
ax.plot(0.96*np.sin(t), 0.62*np.sin(t)*np.cos(t), color=GREY, lw=1.0, zorder=1)

# ПУТЬ строго от углов через центр = 2sqrt2.
# верхняя петля пути: (-1,1) -> (0,0) -> (1,1)
ax.plot([-1,0,1],[1,0,1], color=RED, lw=2.6, zorder=4, solid_capstyle="round")
# стрелки направления вдоль пути
for (x1,y1,x2,y2) in [(-1,1,-0.5,0.5),(0,0,0.5,0.5)]:
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",
                 mutation_scale=13,color=RED,lw=0,zorder=5))

# центр
ax.plot(0,0,"o",color=NAVY,ms=7,zorder=6)
ax.annotate("closure point (t \u2248 0)", xy=(0,0), xytext=(0.12,-0.16),
            fontsize=9, color=NAVY, va="top")

# углы пути
for (x,y) in [(-1,1),(1,1)]:
    ax.plot(x,y,"o",color=RED,ms=5.5,zorder=6)

# подписи плеч sqrt2
ax.text(-0.56,0.52,r"$\sqrt{2}$",color=RED,fontsize=12,ha="right",va="center")
ax.text(0.56,0.52,r"$\sqrt{2}$",color=RED,fontsize=12,ha="left",va="center")

# верх: результат
ax.text(0,1.32,r"one loop:  corner $\to$ centre $\to$ corner $= 2\sqrt{2}\approx 2.828$",
        fontsize=10.5, ha="center", color="#222")
# низ: сторона
ax.text(0,-1.22,"side = 2  (binarity bound, derived)",
        fontsize=9.5, ha="center", color=NAVY, va="top")

ax.set_aspect("equal"); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.5,1.55); ax.axis("off")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/fig_figure_eight_2x2.pdf", bbox_inches="tight")
plt.savefig("/mnt/user-data/outputs/fig_figure_eight_2x2.png", dpi=150, bbox_inches="tight")
leg=math.dist((-1,1),(0,0))
print(f"плечо={leg:.5f} (=sqrt2), путь={2*leg:.5f} (=2sqrt2={2*math.sqrt(2):.5f}) OK")
