Use this exact code in `13-cats_got_your_tongue.py`:

```python id="k4v9xp"
#!/usr/bin/env python3
"""Concatenate two matrices using numpy."""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Returns the concatenation of two matrices."""
    return np.concatenate((mat1, mat2), axis=axis)
```

