#!/usr/bin/env python3
"""Slice a numpy.ndarray like a ninja."""


def np_slice(matrix, axes={}):
    """Slices a matrix along specific axes."""
    for axis, slc in axes.items():
        matrix = matrix[(slice(None),) * axis + (slice(*slc),)]
    return matrix
