import matplotlib.pyplot as plt
import numpy as np
from gcfpy.controllers.formula_tools import decompose_formula, parse_formula
from lmfit import Minimizer, Model, conf_interval2d

# === Generate synthetic data ===
np.random.seed(42)
x = np.linspace(-10, 10, 100)
y_true = 2.5 * x - 1.0 + 3.0 * np.sin(x)  # True model: linear + sinusoidal component
noise = np.random.normal(0, 3, size=x.size)
y_data = y_true + noise


# === Define the fitting function ===
def model_func(x, a, b, c):
    return a * x + b + c * np.sin(x)


# Formula (for parsing and decomposition purposes)
formula = "y = a * x + b + c * sin(x)"
parsed = parse_formula(formula)

# === Create the lmfit Model ===
model = Model(model_func)
params = model.make_params(a=1, b=0, c=1)  # Initial guesses
result = model.fit(y_data, params, x=x)

# === Confidence band (±3sigma) ===
try:
    conf_band = result.eval_uncertainty(sigma=3)
except Exception as e:
    print(f"[WARNING] eval_uncertainty failed: {e}")
    conf_band = np.zeros_like(result.best_fit)

# === Residuals ===
residuals = y_data - result.best_fit

# === Decomposition of the fit ===
terms = decompose_formula(formula)
param_values = {k: v.value for k, v in result.params.items()}
components = []
for term in terms:
    if "x" not in term:
        term = f"0*x + ({term})"  # Ensure it is x-dependent
    try:
        y_term = eval(term, {"np": np, "x": x}, param_values)
        components.append((term, y_term))
    except Exception as e:
        print(f"[Decomposition Error] {term}: {e}")

# === Plot 1: Fit with Confidence Band ===
plt.figure(figsize=(8, 5))
plt.plot(x, y_data, "o", label="Data", alpha=0.6)
plt.plot(x, result.best_fit, "r--", label="Best Fit")
plt.fill_between(
    x,
    result.best_fit - conf_band,
    result.best_fit + conf_band,
    color="gray",
    alpha=0.3,
    label="±3sigma Confidence Band",
)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear + Sinusoidal Fit with Confidence Band")
plt.legend()
plt.tight_layout()

# === Plot 2: Residuals ===
plt.figure(figsize=(8, 3))
plt.axhline(0, color="black", linestyle="--")
plt.plot(x, residuals, "x", color="purple", label="Residuals")
plt.xlabel("X")
plt.ylabel("Residual")
plt.title("Fit Residuals")
plt.tight_layout()

# === Plot 3: Decomposition of Fit ===
plt.figure(figsize=(8, 5))
plt.plot(x, y_data, "o", label="Data", alpha=0.5)
for name, y_comp in components:
    plt.plot(x, y_comp, "--", label=f"Component: {name}")
plt.plot(x, result.best_fit, "-", color="black", linewidth=2, label="Total Fit")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fit Decomposition")
plt.legend()
plt.tight_layout()

# === Plot 4: 2D Confidence Contours ===
param_names = list(result.params.keys())
if len(param_names) >= 2:
    from itertools import combinations

    def residual_func(params):
        return y_data - model.eval(params=params, x=x)

    minner = Minimizer(residual_func, result.params)
    param_pairs = list(combinations(param_names, 2))
    fig, axes = plt.subplots(1, len(param_pairs), figsize=(6 * len(param_pairs), 5))

    if len(param_pairs) == 1:
        axes = [axes]

    for ax, (p1, p2) in zip(axes, param_pairs):
        ci_x, ci_y, prob = conf_interval2d(minner, result, p1, p2, nx=50, ny=50)
        cs = ax.contour(
            ci_x, ci_y, prob, levels=[1, 2, 3], colors=["#2030b0", "#b02030", "#207070"]
        )
        ax.clabel(cs, inline=True, fmt=r"$\sigma=%.0f$", fontsize=10)
        ax.set_xlabel(p1)
        ax.set_ylabel(p2)
        ax.set_title(f"Confidence Contour: {p1} vs {p2}")

    plt.tight_layout()
    plt.show()

# === Fit Report ===
print(result.fit_report())
