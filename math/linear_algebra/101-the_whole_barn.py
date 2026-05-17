#!/usr/bin/env python3
"""Recursively add two matrices."""


def add_matrices(mat1, mat2):
    """Returns element-wise sum of two matrices or None if shapes differ."""

    # If types mismatch → invalid
    if type(mat1) != type(mat2):
        return None

    # Base case: numbers
    if not isinstance(mat1, list):
        return mat1 + mat2

    # Must have same length
    if len(mat1) != len(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        added = add_matrices(mat1[i], mat2[i])

        if added is None:
            return None

        result.append(added)

    return result
