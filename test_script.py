#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################
### TEST VALIDATION 2 ###
#########################

import unittest
import numpy as np
from hubbado_test2 import MatrixGenerator


class TestMatrix(unittest.TestCase):
    def test_prime_list(self):
        width = 5
        height = 3
        seq_type = 'prime'
        # operation is just relevant for set the number of needed elements
        operation = 'sum'
        list_ = MatrixGenerator(width, height, seq_type, operation).prime_list()
        self.assertEqual(list_, [2, 3, 5, 7, 11])
        self.assertEqual(len(list_), max(width, height))

    def test_fibonacci_list(self):
        width = 6
        height = 5
        seq_type = 'fibonacci'
        # operation is just relevant for set the number of needed elements
        operation = 'pers'
        list_ = MatrixGenerator(width, height, seq_type, operation).fibonacci_list()
        self.assertEqual(list_, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(len(list_), width + height)

    def test_Matrix_sum(self):
        width = 3
        height = 3
        seq_type = 'prime'
        operation = 'sum'
        matrix = MatrixGenerator(width, height, seq_type, operation).build_matrix()
        self.assertEqual(matrix.tolist(), [[4, 5, 7], [5, 6, 8], [7, 8, 10]])

    def test_Matrix_pers(self):
        width = 3
        height = 4
        seq_type = 'prime'
        # operation is just relevant for set the number of needed elements
        operation = 'pers'
        matrix = MatrixGenerator(width, height, seq_type, operation).build_matrix()
        self.assertEqual(matrix.tolist(), [[3, 5, 7], [5, 7, 11], [7, 11, 13], [11, 13, 17]])

    def test_Matrix_prod(self):
        width = 5
        height = 6
        seq_type = 'fibonacci'
        # operation is just relevant for set the number of needed elements
        operation = 'prod'
        matrix = MatrixGenerator(width, height, seq_type, operation).build_matrix()
        self.assertEqual(matrix.tolist(), [[0, 0, 0, 0, 0], [0, 1, 1, 2, 3], [0, 1, 1, 2, 3], [0, 2, 2, 4, 6], [0, 3, 3, 6, 9], [0, 5, 5, 10, 15]])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
