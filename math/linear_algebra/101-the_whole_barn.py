#!/usr/bin/env python3
"""Add two matrices recursively."""


def add_matrices(mat1, mat2):
    """Returns the element-wise sum of two matrices or None if shapes differ."""
    if type(mat1) != type(mat2):
        return None

    if isinstance(mat1, list):
        if len(mat1) != len(mat2):
            return None
        return [add_matrices(m1, m2) for m1, m2 in zip(mat1, mat2)]

    return mat1 + mat2
