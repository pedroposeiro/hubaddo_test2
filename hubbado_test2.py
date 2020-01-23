#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################
### SECOND TEST ###
###################

import sys
import numpy as np


if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

class MatrixGenerator:
    ''' This program takes the width and height from the user and in response
        displays width*height table, such that the content of cell (a,b) is
        the sum, product or a+b+1 of a-th and b-th prime or fibonacci number.
        Both operation (sum, product and a+b+1) and number sequence (prime or
        fibonacci numbers) are set by the user as well.
    '''
    def __init__(self, width, height, seq_type, operation):
        '''width: Width of the matrix
           heigth: Height of the matrix
           seq_type: Sequence type (e.g. prime, fibonacci)
           operation: Operation (e.g. sum [X(a)+X(b)],
                                      prod [X(a)*X(b)],
                                      pres [X(a+b+1)])
                      where a-th and b-th prime/fibonacci number for cells (a,b)
        '''
        self.width = width
        self.height = height
        self.seq_type = seq_type
        self.operation = operation
        self.build_matrix()

    def prime_list(self):
        '''Get a list of n prime numbers
        '''
        # Initial conditions
        primes_list = []
        val = 1

        while True:
            val += 1
            if val > 1:
                for i in range(2, int(val ** 0.5) + 1):
                    if val % i == 0:
                        break
                else:
                    primes_list.append(val)

            # Loop stops when we got all needed elements for the operations
            if (self.operation == 'sum' or self.operation == 'prod') \
                and len(primes_list) > max(self.width-1, self.height-1):
                break
            elif self.operation == 'pers' and len(primes_list) > \
                 self.width + self.height - 1:
                break

        print("Prime list: \n", primes_list)
        return primes_list

    def fibonacci_list(self):
        '''Get a list of n Fibonacci numbers
        '''
        # Initial conditions
        n1 = 0
        n2 = 1
        count = 0
        fibonacci_list = []

        # Set the length of the list needed for the operation
        if self.operation == 'sum' or self.operation == 'prod':
            length = max(self.width-1, self.height-1)
        elif self.operation == 'pers':
            length = self.width + self.height - 1


        if length == 0:
            fibonacci_list.append(n1)
        elif length == 1:
            fibonacci_list.append(n2)
        else:
            while count <= length:
                fibonacci_list.append(n1)
                nt = n1 + n2
                n1 = n2
                n2 = nt
                count += 1

        print("Fibonacci list: \n", fibonacci_list)
        return fibonacci_list

    def build_matrix(self):
        '''Execute the sum of a-th and b-th prime number for cells (a,b)
           and build the Matrix n*n
        '''

        if self.seq_type == 'prime':
            seq_list = self.prime_list()
        elif self.seq_type == 'fibonacci':
            seq_list = self.fibonacci_list()

        if self.operation == 'sum':
            matrix_opt = np.array([[seq_list[i] + seq_list[j] \
                                  for j in range(self.width)] \
                                  for i in range(self.height)])
        elif self.operation == 'prod':
            matrix_opt = np.array([[seq_list[i] * seq_list[j] \
                                  for j in range(self.width)] \
                                  for i in range(self.height)])
        elif self.operation == 'pers':
            matrix_opt = np.array([[seq_list[i + j + 1] \
                                  for j in range(self.width)] \
                                  for i in range(self.height)])

        print("Matrix: \n", matrix_opt)
        return matrix_opt

if __name__ == '__main__':
    while True:
        try:
            width = int(input("Please enter the matrix width: "))
            break
        except ValueError:
            print("- Insert a valid number")

    while True:
        try:
            height = int(input("Please enter the matrix heigth: "))
            break
        except ValueError:
            print("- Insert a valid number")

    while True:
        try:
            seq_type = input("Please enter the Sequence Type (e.g. prime, fibonacci): ")
            if seq_type in ['prime', 'fibonacci']:
                break
            else:
                raise ValueError("- Wrong Sequence Type selection. Select \
                                between prime and fibonacci.")
        except ValueError as e:
            print(e)

    while True:
        try:
            operation = str(input("Please enter the desirable operation (e.g. sum, prod, pers): "))
            if operation in ['sum', 'prod', 'pers']:
                break
            else:
                raise ValueError('- Wrong operation selection. Select between sum, prod and pers.')
        except ValueError as e:
            print(e)

    MatrixGenerator(width, height, seq_type, operation)
