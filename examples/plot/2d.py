import matplotlib.pyplot as plt
import numpy as np
from lmfit import Model

# -----------------------------------------------
# Generate synthetic 2D Gaussian data
# -----------------------------------------------
np.random.seed(0)
n_points = 50

x = np.linspace(-5, 5, n_points)
y = np.linspace(-5, 5, n_points)
xv, yv = np.meshgrid(x, y)


def gaussian_2d(x, y, A, x0, y0, sigma_x, sigma_y, offset):
    """
    2D Gaussian function.
    """
    return (
        A
        * np.exp(-((x - x0) ** 2 / (2 * sigma_x**2) + (y - y0) ** 2 / (2 * sigma_y**2)))
        + offset
    )


# True data (without noise)
z_true = gaussian_2d(xv, yv, A=5, x0=0, y0=0, sigma_x=1, sigma_y=2, offset=1)

# Add Gaussian noise
noise = np.random.normal(0, 0.2, size=z_true.shape)
z_noisy = z_true + noise

# Flatten data for fitting
data_x = xv.ravel()
data_y = yv.ravel()
data_z = z_noisy.ravel()

# -----------------------------------------------
# Define and fit the model using lmfit
# -----------------------------------------------
model = Model(gaussian_2d, independent_vars=["x", "y"])

params = model.make_params(
    A=4,  # initial guess for amplitude
    x0=0,  # initial guess for x center
    y0=0,  # initial guess for y center
    sigma_x=1,
    sigma_y=1,
    offset=0.5,
)

# Fit noisy data
result = model.fit(data_z, params, x=data_x, y=data_y)

# Best fit reshaped for visualization
fit_z = result.best_fit.reshape(n_points, n_points)

# -----------------------------------------------
# Plot results
# -----------------------------------------------

# 2D contour plot
plt.figure(figsize=(8, 6))
plt.contourf(xv, yv, z_noisy, levels=50, cmap="viridis")
plt.colorbar(label="Z (noisy data)")
plt.contour(xv, yv, fit_z, levels=10, colors="white", linewidths=1)
plt.title("2D Gaussian Fit - Contour Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()

# 3D surface plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(xv, yv, fit_z, cmap="plasma", alpha=0.9)
ax.scatter(xv, yv, z_noisy, color="black", s=5, label="Noisy Data")
ax.set_title("2D Gaussian Fit - 3D Surface")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.tight_layout()
plt.show()

# -----------------------------------------------
# Display fit report
# -----------------------------------------------
print(result.fit_report())
