#!/usr/bin/env python3
"""Concatenate matrices along a given axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices or returns None if impossible."""

    # If types differ, cannot concatenate
    if type(mat1) != type(mat2):
        return None

    # If we are at scalar level
    if not isinstance(mat1, list):
        return mat1

    # axis 0: direct concatenation
    if axis == 0:
        return mat1 + mat2

    # must have same length to go deeper
    if len(mat1) != len(mat2):
        return None

    # recursive step
    result = []
    for i in range(len(mat1)):
        merged = cat_matrices(mat1[i], mat2[i], axis - 1)
        if merged is None:
            return None
        result.append(merged)

    return result
