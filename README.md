# quantumxy

Python scripts for a 1D quantum spin-1/2 xy chain with periodic condition.
It contains the code for the Hamiltonian, its magnetization and correlation.
The scripts are written for the purpose of assignment.

## Functions
```generate_Hamiltonian(N, J, h)``` : 
```generate_Hamiltonian_with_Pauli_matrices(N, J, h)``` : 
```compute_magnetization(state, basis)``` :
```compute_correlation(state, basis, r)``` :
N is the system size. J is the coupling strength. h is the magnetic field.

## Setup
In order to install, follow the below commands in the package directory.
```python3 setup.py build```
```python3 setup.py install --user```
To use, ```import quantumxy.quantumxy```.
