#!/usr/bin/env bash
# Adds the quantum-sector scripts to github.com/ivan-denysov/finite-validation
# Run from inside a fresh clone of that repository.
set -e

# 1. the ten scripts + the superseded one (kept deliberately)
cp /path/to/bundle/*.py .

# 2. merge the README section (do not overwrite the existing README blindly:
#    open README_quantum_section.md and paste its tables in)

# 3. commit
git add -A
git commit -m "Quantum-sector supplementary code (Paper 1 revision)

Ten standalone scripts, numpy only, each seeded and status-marked.
Four document arguments the paper withdrew:
  chsh_alphabet_bound.py        refutes 'the excess lives in the silence'
  angular_resolution.py         withdraws K >= 64 / 256
  lock_to_kuramoto.py           withdraws 'the leak is necessary'
  indivisibility_consequences.py records a refuted uncertainty argument
single_act_metric_v1_superseded.py is retained, not deleted: the earlier and
incorrect reading in which D was said to obey the parallelogram law."
git push

# 4. Zenodo: enable the GitHub integration BEFORE tagging.
#    zenodo.org -> Settings -> GitHub -> toggle 'finite-validation'
#    Zenodo archives releases created AFTER the toggle; it ignores earlier ones.
git tag -a v2.0 -m "Code accompanying the Paper 1 revision (quantum sector rewritten)"
git push origin v2.0
# then on GitHub: Releases -> Draft a new release -> tag v2.0 -> Publish
