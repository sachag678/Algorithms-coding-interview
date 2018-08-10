"""Cracking the Coding Interview: Chapter 1 problem 1.8."""
import numpy as np


def zero_matrix(mat):
    """Check if for zero elements, gets the indices and then sets the rows and cols to zero."""
    row, col = np.where(mat == 0)
    print(row, col)
    mat[row, :] = 0
    mat[:, col] = 0

    return mat

if __name__ == '__main__':
    mat = np.ones((3, 3))
    mat[0][0] = 0
    mat[2][1] = 0
    print(mat)
    print(zero_matrix(mat))
