Use this exact code in `12-bracin_the_elements.py`:

```python id="d2k7mw"
#!/usr/bin/env python3
"""Perform element-wise operations on numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Returns element-wise sum, difference, product, and quotient."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
```

