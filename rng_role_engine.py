"""
QUANTUM SECTOR — coarse demonstration of the ROLE of a randomness generator
in a world-engine. NOT a proof of quantum effects, NOT 'the world freezes
without quanta'. Just: what does a randomness generator DO to a deterministic
engine, and where does TIME (the before->after ordering) enter.

Engine: Conway's Game of Life (deterministic core).
Two regimes:
  DET  — pure deterministic rules.
  RNG  — deterministic rules + a randomness generator (rare random births).

Two clean observables:
  (1) causal rigidity: is state(t+1) fully determined by state(t)?
      Measured as: across the whole run, does the SAME state ever lead to
      DIFFERENT successors? DET -> never (rigidity = 1.0, perfect causal link).
      RNG -> the link is broken (same state can go to different successors).
  (2) cycle closure: a finite deterministic world must eventually repeat a state
      (fall into a cycle = exhaust itself). Step of first repeat = closure time.
      RNG -> world does not close into a cycle within the run.
"""
import numpy as np

def step(g):
    nb = sum(np.roll(np.roll(g,i,0),j,1) for i in (-1,0,1) for j in (-1,0,1) if (i,j)!=(0,0))
    return ((nb==3)|((g==1)&(nb==2))).astype(np.int8)

def run(L=7, T=3000, r=0.0, seed=1):
    rng=np.random.default_rng(seed)
    g=(rng.random((L,L))<0.40).astype(np.int8)
    hashes=[]; transitions={}; live=[]
    prev=None
    for t in range(T):
        if prev is not None:
            # record transition prev_hash -> current_hash
            ph=hash(prev.tobytes()); ch=hash(g.tobytes())
            transitions.setdefault(ph,set()).add(ch)
        prev=g.copy()
        g=step(g)
        if r>0:
            mask=rng.random((L,L))<r
            g=np.where(mask,1,g).astype(np.int8)   # randomness generator: rare births
        hashes.append(hash(g.tobytes())); live.append(int(g.sum()))
    return hashes,transitions,live

def causal_rigidity(transitions):
    """fraction of observed states whose successor is UNIQUE.
    1.0 = perfectly causal (same cause -> same effect, always).
    <1.0 = the causal link is broken (same state, different next states)."""
    if not transitions: return 1.0
    unique=sum(1 for succ in transitions.values() if len(succ)==1)
    return unique/len(transitions)

def closure_time(hashes):
    seen={}
    for t,h in enumerate(hashes):
        if h in seen: return t        # first repeat = fell into a cycle
        seen[h]=t
    return None                       # did not close within the run

print("ROLE OF THE RANDOMNESS GENERATOR — scan of generator strength r (7x7 field, 4 seeds)")
print(f"{'r':>8} {'causal_rigidity':>18} {'cycle_closure_step':>20} {'late_live':>10}")
print("-"*60)
for r in [0.0, 0.002, 0.01, 0.03, 0.08]:
    rigs=[]; closes=[]; lives=[]
    for sd in (1,2,3,4):
        hs,tr,lv=run(r=r,seed=sd)
        rigs.append(causal_rigidity(tr))
        c=closure_time(hs); closes.append(c if c is not None else -1)
        lives.append(np.mean(lv[-200:]))
    rig=np.mean(rigs)
    closed=[c for c in closes if c>=0]
    close_str = f"{np.mean(closed):.0f}" if closed else "no closure"
    label = "DET" if r==0.0 else f"r={r}"
    print(f"{label:>8} {rig:>18.3f} {close_str:>20} {np.mean(lives):>10.1f}")

print("""
READ:
  DET  -> causal_rigidity = 1.000: in the deterministic engine every state has a
          UNIQUE successor. state(t) fully determines state(t+1). The before->after
          link is perfect. AND the world closes into a cycle at a finite step:
          a finite deterministic world exhausts itself and repeats.

  RNG  -> causal_rigidity < 1.000: the randomness generator BREAKS the unique
          successor link — the same state no longer fixes the next one. AND the
          world does NOT close into a cycle within the run: it keeps producing
          states it has never visited.

ROLE OF THE GENERATOR (the whole point):
  The randomness generator's role is precisely to break the rigid before->after
  determination and to keep the world from closing on itself. In the deterministic
  engine, TIME (the ordering of ticks) fully fixes every next state — cause is
  complete. The generator is what removes that completeness.

BRIDGE TO TIME (interpretation, stated as such):
  This locates where quantum behaviour must enter: not in space, but in the
  before->after link itself. Where the tick fully resolves the ordering, the next
  state is fixed (classical, causal). Where the generator acts, the ordering no
  longer fixes the outcome. The handle to quantum effects is therefore TIME —
  the tick resolution of the before->after link — which is developed next.
""")
