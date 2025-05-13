import matplotlib.pyplot as plt
import numpy as np
from scipy import odr


# === Define the Gaussian model for ODR ===
def gauss_model(beta, x):
    """Gaussian function for fitting."""
    amp, cen, sigma = beta
    return amp * np.exp(-((x - cen) ** 2) / (2 * sigma**2))


# === Define Jacobian (derivatives wrt parameters) ===
def compute_jacobian(x, beta):
    """Computes the Jacobian matrix of the model with respect to parameters."""
    amp, cen, sigma = beta
    d_amp = np.exp(-((x - cen) ** 2) / (2 * sigma**2))
    d_cen = amp * d_amp * (x - cen) / (sigma**2)
    d_sigma = amp * d_amp * ((x - cen) ** 2) / (sigma**3)
    return np.vstack((d_amp, d_cen, d_sigma)).T  # shape (n_points, 3)


# === Generate noisy synthetic data ===
np.random.seed(0)
true_params = [1.0, 5.0, 1.0]
x_true = np.linspace(0, 10, 100)
y_true = gauss_model(true_params, x_true)

x_err = 0.2
y_err = 0.1
x_noisy = x_true + np.random.normal(0, x_err, size=x_true.shape)
y_noisy = y_true + np.random.normal(0, y_err, size=y_true.shape)

# === Fit with ODR ===
model = odr.Model(gauss_model)
data = odr.RealData(x_noisy, y_noisy, sx=x_err, sy=y_err)
beta0 = [0.5, 4.0, 2.0]  # Initial guesses
odr_obj = odr.ODR(data, model, beta0=beta0)
output = odr_obj.run()

fitted_params = output.beta
cov_beta = output.cov_beta

# Print fitted parameters
print("Fitted parameters:")
for name, val in zip(["amp", "cen", "sigma"], fitted_params):
    print(f"{name}: {val:.4f}")

# === Compute the ±3sigma confidence band ===
x_pred = np.linspace(0, 10, 300)
y_pred = gauss_model(fitted_params, x_pred)

# Propagate uncertainties using Jacobian and covariance matrix
std_devs = []
for xi in x_pred:
    J = compute_jacobian(np.array([xi]), fitted_params)[0]
    var = np.dot(J, np.dot(cov_beta, J.T))
    std_devs.append(np.sqrt(var))

std_devs = np.array(std_devs)
confidence_band = 3 * std_devs  # 3sigma band

# === Plot fit with 99% confidence band ===
plt.figure(figsize=(8, 5))
plt.fill_between(
    x_pred,
    y_pred - confidence_band,
    y_pred + confidence_band,
    color="lightblue",
    alpha=0.5,
    label="99% Confidence Band",
)
plt.plot(x_pred, y_pred, "r--", label="ODR Best Fit")
plt.errorbar(x_noisy, y_noisy, xerr=x_err, yerr=y_err, fmt="o", label="Noisy Data")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("ODR Fit with 99% Confidence Band (±3sigma)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()

# === Plot residuals ===
residuals = y_noisy - gauss_model(fitted_params, x_noisy)
plt.figure(figsize=(8, 4))
plt.axhline(0, linestyle="--", color="black")
plt.scatter(x_noisy, residuals, s=15, color="purple", label="Residuals")
plt.xlabel("X")
plt.ylabel("Residuals")
plt.legend()
plt.title("Residuals after ODR Fit")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
