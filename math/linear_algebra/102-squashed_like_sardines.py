#!/usr/bin/env python3

def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a given axis.
    Returns a new matrix or None if invalid.
    """

    def get_shape(m):
        """Returns shape of matrix, or None if irregular."""
        if not isinstance(m, list):
            return ()
        if len(m) == 0:
            return (0,)
        first_shape = get_shape(m[0])
        if first_shape is None:
            return None
        for item in m:
            if get_shape(item) != first_shape:
                return None
        return (len(m),) + first_shape

    def concat(a, b, ax):
        if ax == 0:
            return a + b
        return [
            concat(a[i], b[i], ax - 1)
            for i in range(len(a))
        ]

    shape1 = get_shape(mat1)
    shape2 = get_shape(mat2)

    if shape1 is None or shape2 is None:
        return None

    if len(shape1) != len(shape2):
        return None

    if axis < 0 or axis >= len(shape1):
        return None

    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None

    return concat(mat1, mat2, axis)
