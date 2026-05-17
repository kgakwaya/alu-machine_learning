#!/usr/bin/env python3
"""Concatenate two matrices along a specific axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices or returns None if impossible."""

    if type(mat1) != type(mat2):
        return None

    if isinstance(mat1, list):
        if axis == 0:
            return mat1 + mat2

        if len(mat1) != len(mat2):
            return None

        return [
            cat_matrices(mat1[i], mat2[i], axis - 1)
            for i in range(len(mat1))
        ]

    return mat1
