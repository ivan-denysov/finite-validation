Physics from Finite Validation — code and figures
Reproducibility repository for the preprint:
Physics from Finite Validation: Classical Recovery and the Quantum Boundary (Tsirelson, Born, and Quantum Gravity)
United Field Initiative (UFI) · ufi.observer · ORCID 0009-0000-3163-4426
This repository contains every simulation run and figure-generating script used in the paper. The scripts are deliberately small, self-contained, and dependency-light so that any reader can reproduce the results.
Requirements

Python 3.10+
numpy, matplotlib

bashpip install numpy matplotlib
Scripts → paper map
ScriptSectionWhat it doesrng_role_engine.py§6.2Game-of-Life run: deterministic world closes into a cycle; a randomness generator postpones / removes closure.make_fig_closure.py§6.2 (Fig.)Generates fig_rng_cycle_closure.pdf (linear) and the log-scale variant.cirelson_geometry_test.py§6.4Where 2√2 actually comes from (4·cos45°); checks the square-diagonal coincidence vs the genuine ratio √2.figure_eight_square.py§6.4Figure-eight in a 2×2 square; verifies the corner→centre→corner path = 2√2 exactly.side_two_independent.py§6.4Shows the classical bound 2 is a theorem of binarity (exhaustive enumeration of ±1 assignments).sqrt2_from_closure.py§6.4Derives the √2 factor from the closure-point path (Pythagoras) under Alice–Bob symmetry.make_fig_eight.py§6.4 (Fig.)Generates fig_figure_eight_2x2.pdf.born_agreement_test.py§6.6The "between 0 and 1" number = cos²(θ/2) = Born; shows the math exists but the square is posited (linear vs cosine correlation laws).make_fig_structure.py§6.7 (Fig.)Generates fig_three_element_structure.pdf (observable event = triple; state = pair, value indefiniteness).games_rng_role_ORIGINAL.py§6.2Original early run kept for provenance (superseded by rng_role_engine.py).
Figures
FileSectionfig_rng_cycle_closure.pdf / .png§6.2 — cycle closure vs generator strengthfig_rng_cycle_closure_log.pdf§6.2 — log-scale variant (supplementary)fig_figure_eight_2x2.pdf / .png§6.4 — figure-eight, corner→centre→corner = 2√2fig_three_element_structure.pdf / .png§6.7 — observable event (triple) and state (pair)
How to run
Each script is standalone:
bashcd code
python3 figure_eight_square.py
python3 side_two_independent.py
python3 born_agreement_test.py
# figure generators write PDFs/PNGs to the current directory:
python3 make_fig_eight.py
python3 make_fig_closure.py
python3 make_fig_structure.py
Status note
Per the paper's status discipline: these runs are illustrations and consistency checks, not independent confirmations. The classical bound 2 is genuinely derived (binarity); the Tsirelson factor 2√2 is reconstructed under an explicit closure-point hypothesis; the Born value is reproduced but reinterpreted, not derived. See the paper's Section 3 (Status and Scope) and the per-section status notes.
Citation
If you use this material, please cite the preprint (DOI to be added upon deposit) and this repository.
License
Code released under the MIT License. Figures © United Field Initiative, CC BY 4.0.
