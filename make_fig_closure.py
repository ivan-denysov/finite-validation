import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

r = np.array([0.0, 0.001, 0.002, 0.005, 0.01, 0.02, 0.03, 0.05, 0.08])
closure_step = np.array([29,30,41,47,84,102,195,921,4000])

fig, ax = plt.subplots(figsize=(7,4.5))
ax.plot(r, closure_step, '-o', color='#1f3a5f', linewidth=1.8, markersize=5)
ax.axhline(y=4000, color='gray', linestyle='--', linewidth=1.2)
ax.annotate('no closure\n(censored at T=4000)', xy=(0.08,4000), xytext=(0.046,3500),
            fontsize=9, ha='left', va='top',
            arrowprops=dict(arrowstyle='->', lw=0.8, color='gray'))
ax.plot(0.08,4000, marker='o', markersize=7, color='#1f3a5f')
ax.set_title('Role of the randomness generator: it postpones and removes cycle closure',
             fontsize=11.5, pad=12)
ax.set_xlabel('randomness-generator strength  r', fontsize=11)
ax.set_ylabel('cycle-closure step\n(larger = world resists repeating)', fontsize=10.5)
ax.grid(True, linestyle=':', linewidth=0.6, alpha=0.6)
ax.set_xlim(-0.002,0.085); ax.set_ylim(0,4200)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig_rng_cycle_closure.pdf', bbox_inches='tight')
plt.savefig('/mnt/user-data/outputs/fig_rng_cycle_closure.png', dpi=150, bbox_inches='tight')
print("linear saved")

# лог-вариант для supplementary
fig2, ax2 = plt.subplots(figsize=(7,4.5))
ax2.plot(r, closure_step, '-o', color='#1f3a5f', linewidth=1.8, markersize=5)
ax2.axhline(y=4000, color='gray', linestyle='--', linewidth=1.2)
ax2.plot(0.08,4000, marker='o', markersize=7, color='#1f3a5f')
ax2.set_yscale('log')
ax2.annotate('no closure (censored, T=4000)', xy=(0.08,4000), xytext=(0.03,4300),
             fontsize=9, ha='left', color='gray')
ax2.set_title('Cycle closure vs generator strength (log scale)', fontsize=11.5, pad=12)
ax2.set_xlabel('randomness-generator strength  r', fontsize=11)
ax2.set_ylabel('cycle-closure step (log)', fontsize=10.5)
ax2.grid(True, which="both", linestyle=':', linewidth=0.6, alpha=0.6)
ax2.set_xlim(-0.002,0.085)
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig_rng_cycle_closure_log.pdf', bbox_inches='tight')
plt.savefig('/mnt/user-data/outputs/fig_rng_cycle_closure_log.png', dpi=150, bbox_inches='tight')
print("log saved")
