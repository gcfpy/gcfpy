import numpy as np


def fit_function(x, p2, p1, p0):
    return p0 * np.exp(-0.5 * ((x - p1) / p2) ** 2)
