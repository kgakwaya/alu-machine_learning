#!/usr/bin/env python3
"""Module that performs a same convolution on grayscale images."""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """Performs a same convolution on grayscale images.

    Args:
        images: numpy.ndarray of shape (m, h, w) containing multiple
            grayscale images.
            m is the number of images.
            h is the height in pixels of the images.
            w is the width in pixels of the images.
        kernel: numpy.ndarray of shape (kh, kw) containing the kernel
            for the convolution.
            kh is the height of the kernel.
            kw is the width of the kernel.

    Returns:
        numpy.ndarray containing the convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    if kh % 2 == 0:
        ph_top = kh // 2
        ph_bottom = kh // 2 - 1
    else:
        ph_top = kh // 2
        ph_bottom = kh // 2

    if kw % 2 == 0:
        pw_left = kw // 2
        pw_right = kw // 2 - 1
    else:
        pw_left = kw // 2
        pw_right = kw // 2

    padded = np.pad(
        images,
        ((0, 0), (ph_top, ph_bottom), (pw_left, pw_right)),
        mode='constant',
        constant_values=0
    )

    convolved = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            image_slice = padded[:, i:i + kh, j:j + kw]
            convolved[:, i, j] = np.sum(
                image_slice * kernel, axis=(1, 2)
            )

    return convolved
