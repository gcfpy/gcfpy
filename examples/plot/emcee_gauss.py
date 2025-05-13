# MCMC example using emcee (no lmfit)

import corner
import emcee
import matplotlib.pyplot as plt
import numpy as np


# --- Likelihood and model ---
def log_likelihood(theta, x, y, yerr):
    amp, cen, sigma = theta
    model = amp * np.exp(-((x - cen) ** 2) / (2 * sigma**2))
    return -0.5 * np.sum(((y - model) / yerr) ** 2)


def log_prior(theta):
    amp, cen, sigma = theta
    if 0 < amp < 10 and 0 < cen < 10 and 0.1 < sigma < 5:
        return 0.0
    return -np.inf


def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, x, y, yerr)


# --- Simulated data ---
np.random.seed(42)
x = np.linspace(0, 10, 100)
true_params = (1.0, 5.0, 0.5)
yerr = 0.1
y = true_params[0] * np.exp(-((x - true_params[1]) ** 2) / (2 * true_params[2] ** 2))
y += yerr * np.random.randn(len(x))

# --- Initial guess for walkers ---
nwalkers = 500
ndim = 3
initial = np.array([2.0, 2.0, 2.0])
pos = initial + 1e-3 * np.random.randn(nwalkers, ndim)

# --- Run MCMC ---
sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(x, y, yerr))
sampler.run_mcmc(pos, 1000, progress=True)

# --- Extract chains ---
flat_samples = sampler.get_chain(discard=200, thin=15, flat=True)
labels = ["amp", "cen", "sigma"]

# --- Trace plots ---
fig, axes = plt.subplots(ndim, figsize=(10, 7), sharex=True)
samples = sampler.get_chain()
for i in range(ndim):
    ax = axes[i]
    for walker in samples[:, :, i].T:
        ax.plot(walker, alpha=0.2, color="black")
    ax.set_ylabel(labels[i])
axes[-1].set_xlabel("Step")
plt.tight_layout()

# --- Corner plot ---
corner.corner(flat_samples, labels=labels, truths=true_params)

# --- Posterior predictive plot ---
x_pred = np.linspace(0, 10, 200)
y_preds = []
for theta in flat_samples[np.random.choice(len(flat_samples), 100)]:
    amp, cen, sigma = theta
    y_preds.append(amp * np.exp(-((x_pred - cen) ** 2) / (2 * sigma**2)))

plt.figure()
for y_pred in y_preds:
    plt.plot(x_pred, y_pred, color="gray", alpha=0.1)
plt.errorbar(x, y, yerr=yerr, fmt="o", label="data")
plt.title("Posterior Predictive")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.show()

# --- Autocorrelation time (optional if long chains) ---
try:
    tau = sampler.get_autocorr_time()
finally:
    print("Autocorrelation time:", tau)
