# quantumxy

Python scripts for a 1D quantum spin-1/2 xy chain with periodic condition.
It contains the code for the Hamiltonian, its magnetization and correlation.
The scripts are written for the purpose of assignment.

## Functions
```generate_Hamiltonian(N, J, h)``` : Function generating Hamiltonian using basis\
```generate_Hamiltonian_with_Pauli_matrices(N, J, h)``` : Function generating Hamiltonian using Pauli matrices\
```compute_magnetization(state, basis)``` : Function computing magnetization\
```compute_correlation(state, basis, r)``` : Function computing correlation\
$N$ is the system size. $J$ is the coupling strength. $h$ is the magnetic field. $r$ is the degree of neighboring sites.
If $r=1$, it considers the neareset neighbors.

## Setup
In order to install, follow the below commands in the package directory.\
```python3 setup.py build```\
```python3 setup.py install --user```\
To use, ```import quantumxy.quantumxy```.
