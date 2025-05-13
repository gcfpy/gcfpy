import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model, Parameters

# === Generate synthetic data ===
np.random.seed(42)
X = np.tile(np.linspace(0, 10, 50), 4)
Y_values = np.repeat([0, 10, 20, 40], 50)
true_a = 2

Z = true_a * X + Y_values + np.random.normal(0, 0.7, size=X.shape)


def fit_func(x, y, a):
    """Model function: Z = a * X + Y."""
    return a * x + y


model = Model(fit_func, independent_vars=["x", "y"])

# === Define initial parameters ===
params = Parameters()
params.add("a", value=0.5, min=0, max=10)

# === Perform the fit ===
result = model.fit(Z, params, x=X, y=Y_values)

print(result.fit_report())

Y_uniques = np.unique(Y_values)
plt.figure(figsize=(8, 5))

# Plot data points and fit per Y
for y_val in Y_uniques:
    mask = Y_values == y_val
    plt.scatter(X[mask], Z[mask], s=10, label=f"Data Y={y_val}")
    plt.plot(X[mask], result.best_fit[mask], label=f"Fit Y={y_val}")

plt.xlabel("X")
plt.ylabel("Z")
plt.legend()
plt.title("Global Fit: Z = a * X + Y (Y fixed)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
