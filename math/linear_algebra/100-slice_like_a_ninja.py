#!/usr/bin/env python3
"""Slice a numpy.ndarray along specific axes."""


def np_slice(matrix, axes=None):
    """Returns a sliced numpy.ndarray."""

    if axes is None:
        axes = {}

    slc = [slice(None)] * matrix.ndim

    for axis, values in axes.items():
        slc[axis] = slice(*values)

    return matrix[tuple(slc)]
