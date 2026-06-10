# Physics from Finite Validation — code and figures
 
Reproducibility repository for the preprint:
 
**Physics from Finite Validation: Classical Recovery and the Quantum Boundary**
United Field Initiative (UFI) · [ufi.observer](https://ufi.observer) · ORCID 0009-0000-3163-4426
DOI: [10.5281/zenodo.20628369](https://doi.org/10.5281/zenodo.20628369)
 
This repository contains every simulation run and figure-generating script used in the paper. The scripts are deliberately small, self-contained, and dependency-light so that any reader can reproduce the results.
 
## Requirements
 
- Python 3.10+
- `numpy`, `matplotlib`
```
pip install numpy matplotlib
```
 
## Scripts → paper map
 
### Classical sector (§4)
 
| Script | Section | What it does |
| --- | --- | --- |
| `calibrate_gr.py` | §4.2 | Gravitational time dilation: the model's leading term coincides with weak-field GR; calibration constant A = 1.0000, no fitting. |
| `two_channel_derivation.py` | §4.3 | Light deflection as two equal channels (0.875″ + 0.875″ = 1.750″); factor 2 not inserted by hand. |
| `hypothesis_B_compounding.py` | §4.3 | Perihelion fork: path-compounded law (1+φ/N)^N → exp(φ) gives β=1 → 42.99″/century (observed 42.98). |
| `beta_mercury_test.py` | §4.3 | The bare two-channel product (β=1/2) predicts ~50″/century — excluded as the composition law. |
| `hole_b_second_order.py` | §4.3 | Second-order analysis showing the additive law is excluded and the composition is product-like. |
| `close_two_holes.py` | §4.3 | Status audit of the two-channel assumptions (equal channels derived; multiplicative composition imported). |
| `emc2_energy_derivation.py` | §4.3 | E = mc² as a two-channel structural analogy (postulated, not derived); dimensional and electron-rest-energy consistency check. |
 
### Quantum sector (§5)
 
| Script | Section | What it does |
| --- | --- | --- |
| `rng_role_engine.py` | §5.2 | Game-of-Life run: a deterministic world closes into a cycle; a randomness generator postpones / removes closure. |
| `make_fig_closure.py` | §5.2 (Fig.) | Generates `fig_rng_cycle_closure.pdf` (linear) and the log-scale variant. |
| `cirelson_geometry_test.py` | §5.4 | Where 2√2 comes from (4·cos45°); checks the square-diagonal coincidence vs the genuine ratio √2. |
| `figure_eight_square.py` | §5.4 | Figure-eight in a 2×2 square; verifies the corner→centre→corner path = 2√2 exactly. |
| `side_two_independent.py` | §5.4 | The classical bound 2 is a theorem of binarity (exhaustive enumeration of ±1 assignments). |
| `sqrt2_from_closure.py` | §5.4 | The √2 factor from the closure-point path (Pythagoras) under Alice–Bob symmetry. |
| `path_vs_S_test.py` | §5.4 | Checks that the figure-eight is a geometric image of √2, not a path length equal to the CHSH value S. |
| `make_fig_eight.py` | §5.4 (Fig.) | Generates `fig_figure_eight_2x2.pdf`. |
| `born_agreement_test.py` | §5.6 | The "between 0 and 1" number = cos²(θ/2) = Born; the math exists but the square is posited, not derived. |
| `make_fig_structure.py` | §5.7 (Fig.) | Generates `fig_three_element_structure.pdf` (observable event = triple; state = pair, value indefiniteness). |
| `games_rng_role_ORIGINAL.py` | §5.2 | Original early run kept for provenance (superseded by `rng_role_engine.py`). |
 
## Figures
 
| File | Section |
| --- | --- |
| `fig_rng_cycle_closure.pdf` / `.png` | §5.2 — cycle closure vs generator strength |
| `fig_rng_cycle_closure_log.pdf` | §5.2 — log-scale variant (supplementary) |
| `fig_figure_eight_2x2.pdf` / `.png` | §5.4 — figure-eight, corner→centre→corner = 2√2 |
| `fig_three_element_structure.pdf` / `.png` | §5.7 — observable event (triple) and state (pair) |
 
## How to run
 
Each script is standalone:
 
```
python3 figure_eight_square.py
python3 side_two_independent.py
python3 born_agreement_test.py
python3 hypothesis_B_compounding.py
python3 beta_mercury_test.py
python3 calibrate_gr.py
# figure generators write PDFs/PNGs to the current directory:
python3 make_fig_eight.py
python3 make_fig_closure.py
python3 make_fig_structure.py
```
 
## Status note
 
Per the paper's status discipline, these runs are **illustrations and consistency checks**, not independent confirmations. The classical bound 2 is genuinely derived (binarity); the perihelion advance survives a falsifiable test (the bare product β=1/2 is excluded, the path-compounded law β=1 matches Mercury, the branch selected by data); the Tsirelson factor 2√2 is reconstructed under an explicit closure-point hypothesis; E = mc² is postulated by analogy; the Born value is reproduced but reinterpreted, not derived. See the paper's Section 3 (Status and Scope) and the per-section status notes.
 
## Citation
 
If you use this material, please cite the preprint (DOI [10.5281/zenodo.20628369](https://doi.org/10.5281/zenodo.20628369)) and this repository.
 
## License
 
Code released under the MIT License. Figures © United Field Initiative, CC BY 4.0.
