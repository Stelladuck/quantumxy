import unittest
import inspect
import itertools
import numpy as np

from quantumxy.quantumxy import *

# Usage: python -m unittest test.test
# Must be executed at the toppest project directory

class test(unittest.TestCase):
	def setUp(self):
		self.gfb = generate_full_basis
		self.gHb = generate_Hamiltonian
		self.gHp = generate_Hamiltonian_with_Pauli_matrices
	def test_Generate_full_basis(self):
		assert self.gfb(3) == [(1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0), (0, 1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
		print(f'{inspect.stack()[0][3]}() gives proper value.')
	def test_Equivalence_of_Hamiltonians(self):
		assert np.allclose(self.gHb(generate_full_basis(3), 1, 1), self.gHp(3, 1, 1))
		print(f'{inspect.stack()[0][3]}() gives proper value.')
	def test_Compute_magnetization(self):
		assert np.allclose(compute_magnetization(np.array([1., 0., 0., 0., 0., 0., 0., 0.]) , generate_full_basis(3)), 1.0)
		print(f'{inspect.stack()[0][3]}() gives proper value.')
	def test_Compute_correlation(self):
		assert np.allclose(compute_correlation(np.array([1., 0., 0., 0., 0., 0., 0., 0.]) , generate_full_basis(3), 1), 1.0)
		print(f'{inspect.stack()[0][3]}() gives proper value.')
