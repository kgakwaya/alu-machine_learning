#!/usr/bin/env python3
"""Concatenate matrices along a given axis."""


def cat_matrices(mat1, mat2, axis=0):
    """Concatenates two matrices or returns 'OK' if impossible."""

    if type(mat1) != type(mat2):
        return "OK"

    if not isinstance(mat1, list):
        return mat1

    if axis == 0:
        return mat1 + mat2

    if len(mat1) != len(mat2):
        return "OK"

    result = []
    for i in range(len(mat1)):
        merged = cat_matrices(mat1[i], mat2[i], axis - 1)
        if merged == "OK":
            return "OK"
        result.append(merged)

    return result
