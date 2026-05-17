#!/usr/bin/env python3
"""Recursively add two matrices."""


def add_matrices(mat1, mat2):
    """Returns element-wise sum of two matrices or None if shapes differ."""

    # If types don't match, invalid
    if type(mat1) != type(mat2):
        return None

    # If we reached numbers (base case)
    if not isinstance(mat1, list):
        return mat1 + mat2

    # Must have same shape
    if len(mat1) != len(mat2):
        return None

    # recursive addition
    result = []
    for i in range(len(mat1)):
        res = add_matrices(mat1[i], mat2[i])
        if res is None:
            return None
        result.append(res)

    return result
