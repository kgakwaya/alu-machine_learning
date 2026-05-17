#!/usr/bin/env python3

def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Returns a new matrix if possible, otherwise None.
    """

    def shape(m):
        if not isinstance(m, list):
            return ()
        if len(m) == 0:
            return (0,)
        base = shape(m[0])
        for x in m:
            if shape(x) != base:
                return None
        return (len(m),) + base

    def concat(a, b, ax):
        if ax == 0:
            return a + b
        return [concat(a[i], b[i], ax - 1) for i in range(len(a))]

    s1 = shape(mat1)
    s2 = shape(mat2)

    if s1 is None or s2 is None:
        return None
    if len(s1) != len(s2):
        return None
    if axis < 0 or axis >= len(s1):
        return None

    for i in range(len(s1)):
        if i != axis and s1[i] != s2[i]:
            return None

    return concat(mat1, mat2, axis)
