import itertools
import numpy as np
import copy
import pandas as pd
from functools import reduce

from scipy import linalg

# Function generating full basis
def generate_full_basis(N):
    return list(itertools.product([1,0], repeat = N))

# Function generating Hamiltonian using basis
def generate_Hamiltonian(basis, J, h):
    M = len(basis) # Number of basis
    N = len(basis[0]) # Number of sites
    H = np.zeros((M,M)) # Initialization of Hamiltonian
    # Update Hamiltonian
    for i in range(M):
        for j in range(N):
            if j < N - 1:
                # Update flipping terms
                swapped = list(copy.copy(basis[i]))
                if swapped[j] != swapped[j+1]:
                    swapped[j], swapped[j+1] = swapped[j+1], swapped[j]
                    H[i][basis.index(tuple(swapped))] += J
                elif swapped[j] == swapped[j+1]:
                    H[i][basis.index(tuple(swapped))] = 0
            elif j == N - 1: 
                # Periodic boundary condition
                swapped = list(copy.copy(basis[i]))
                if swapped[j] != swapped[0]:
                    swapped[j],swapped[0] = swapped[0],swapped[j]
                    H[i][basis.index(tuple(swapped))] += J
                elif swapped[j] == swapped[0]:
                    H[i][basis.index(tuple(swapped))] = 0
        # Update external field terms
        H[i][i] += h*(basis[i].count(1) - basis[i].count(0))
    return -H

# Function generating permutation for list
def rotate(l, n):
    return l[n:] + l[:n]

# Function generating Hamiltonian using Pauli matrices
def generate_Hamiltonian_with_Pauli_matrices(N, J, h):
    Id = np.array([[1,0], [0,1]])
    Sp = np.array([[0,1], [0,0]])
    Sm = np.array([[0,0], [1,0]])
    Sz = np.array([[1,0],[0,-1]])
    
    # vector of operators: [σᶻ, σᶻ, id, ...]
    fst_term_ops = [Id]*N
    fst_term_ops[0] = Sp
    fst_term_ops[1] = Sm
    
    fst_term_conj = [Id]*N
    fst_term_conj[0] = Sm
    fst_term_conj[1] = Sp
    
    # vector of operators: [σˣ, id, ...]
    snd_term_ops = [Id]*N
    snd_term_ops[0] = Sz
    
    H = np.zeros((2**N, 2**N))
    
    for i in range(N):
        # tensor multiply all operators
        H += J*reduce(np.kron, fst_term_ops)
        H += J*reduce(np.kron, fst_term_conj)
        # cyclic shift the operators
        fst_term_ops = rotate(fst_term_ops,-1)
        fst_term_conj = rotate(fst_term_conj,-1)
    
    for i in range(N):
        H += h*reduce(np.kron, snd_term_ops)
        snd_term_ops = rotate(snd_term_ops,-1)
    
    return -H

