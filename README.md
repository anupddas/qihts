# Quantum-Inspired Hazelnut Tree Search (QIHTS)

## Overview

This repository presents the implementation and experimental evaluation of a Quantum-Inspired Hazelnut Tree Search (QIHTS) algorithm, an enhanced variant of the classical Hazelnut Tree Search (HTS) metaheuristic optimization algorithm.

The work focuses on introducing quantum-inspired diversification and exploration mechanisms into HTS and evaluating their effect on convergence behavior and optimization performance across standard benchmark functions.

The repository contains the reference implementation of HTS, the proposed QIHTS algorithm, experimental comparisons, and supporting research material.

---

## Publication

DOI: https://doi.org/10.1109/GCON65540.2025.11173289
Published in: 2025 IEEE Guwahati Subsection Conference (GCON) | https://ieeexplore.ieee.org/xpl/conhome/11173281/proceeding

## Research Objective

The main objectives of this project are:

* To implement the classical Hazelnut Tree Search (HTS) algorithm
* To design a Quantum-Inspired HTS (QIHTS) variant
* To introduce probabilistic and chaos-driven diversification strategies
* To evaluate convergence performance on standard optimization benchmarks
* To compare solution quality and optimization efficiency

---

## Hazelnut Tree Search (HTS)

HTS is a population-based metaheuristic optimization algorithm inspired by tree growth behavior and seed dispersion mechanisms in nature. The algorithm primarily consists of:

* Growth phase (local exploitation)
* Fruit scattering phase (local exploration)
* Root spreading phase (global exploration)

These mechanisms balance exploration and exploitation in the search space.

---

## Quantum-Inspired Hazelnut Tree Search (QIHTS)

QIHTS extends HTS by incorporating quantum-inspired concepts such as:

* Probabilistic state transitions
* Quantum-inspired solution blending
* Chaos-driven diversification
* Adaptive exploration behavior

The goal is to improve convergence stability and avoid premature local minima.

---

## Technology Stack

**Programming Language**

* Python

**Libraries**

* NumPy
* Matplotlib
* Scientific computing utilities

**Tools**

* Python runtime environment
* Jupyter (analysis)
* GitHub for version control

---

## Experimental Evaluation

The comparison focuses on:

* Minimum cost convergence
* Stability of optimization
* Iteration performance
* Exploration capability
* Behavior on high dimensional problems

Performance comparison plots are included in the repository.

---

## Results Summary

General experimental observations:

* QIHTS shows improved diversification capability
* Better avoidance of premature convergence observed in some benchmarks
* Comparable computational complexity
* Improved stability in high dimensional search spaces

Detailed numerical comparisons are available in the research paper.

---

## Limitations

Current limitations of the study include:

* Experiments limited to selected benchmark functions
* No real-world engineering optimization tasks included
* No parallel implementation yet
* Parameter sensitivity not fully explored

---

## Future Work

Possible improvements include:

* Testing on real engineering optimization problems
* Parallel implementation
* Hybrid quantum-classical optimization extensions
* Parameter sensitivity analysis
* Comparison with other metaheuristics (PSO, GA, DE)
* Statistical validation across multiple runs

---

## Research Contribution

This project contributes:

* A quantum-inspired extension of HTS
* Comparative experimental evaluation
* Implementation framework for further research
* Benchmark validation of proposed modifications

---

## Author

Anup Das  
B.Tech Computer Science Engineering

Dr. Ningrinla Marchang
Professor, Dept. Computer Science & Engineering, North Eastern Regional Institute of Science and Technology

GitHub:
https://github.com/anupddas

---

## Citation

If you use this work, please cite the associated paper provided in this repository.

## Disclaimer

This repository is intended for academic and research purposes. Performance results depend on parameter settings and benchmark characteristics.

---

## Contact

For questions or research collaboration:

Use GitHub Issues.

---

## Project Status

Research Prototype
Active experimentation and evaluation ongoing.
