import numpy as np


def fit_function(x, A, B, C, D, k, mu, omega, phi, sigma):
    return (
        A * np.exp(-k * x) * np.sin(omega * x + phi)
        + B * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
        + C * np.log(x + 1)
        + D * np.sin(0.3 * x)
    )
