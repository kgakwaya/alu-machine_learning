#!/usr/bin/env python3
"""Concatenate matrices along a given axis (recursive implementation)."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis or returns None."""
    if type(mat1) != type(mat2):
        return None

    if isinstance(mat1, list):
        if axis == 0:
            return mat1 + mat2
        return [
            cat_matrices(m1, m2, axis - 1)
            for m1, m2 in zip(mat1, mat2)
        ]

    return mat1
