# FitProcessor

The `FitProcessor` class encapsulates all curve fitting logic, independently of the UI. It handles multiple fitting strategies (`lmfit`, `ODR`, `emcee`) and supports 1D fitting, multi-1D (Fit per Y), and full 2D surface fitting.

---

## Responsibilities

* Convert a formula string to a Python function (`generate_fit_function`)
* Prepare fitting parameters and options (`prepare_parameters`)
* Dispatch the fitting logic depending on the selected method and strategy
* Return results in a unified format: `(result, minimizer, best_fit, confidence_band)`

---

## Entry Points

### 1. Standard 1D Fit

```python
result, model, best_fit, band = processor.process_fit(
    formula="y = A * exp(-B * x)",
    x_data=x,
    y_data=y,
    weights=w,
    weighting_method="None",
)
```

Dispatches to:

* `lmfit` → `_process_lmfit()`
* `odr`   → `_process_odr()`
* `emcee` → `_run_emcee()`

---

### 2. Multi 1D Fit (Z = f(X) with fixed Y)

```python
result, minimizer, best_fit, band = processor.process_fit_per_y(formula, x, y, z)
```

Performs a global fit with Y treated as a fixed value in each Z slice.
Supports `lmfit`, `odr`, `emcee`.

---

### 3. Full 2D Surface Fit

```python
func = processor.generate_fit_function(formula)
result, _, best_fit, band = processor.process_fit_surface(formula, func, x, y, z)
```

Z is modeled as a function of both X and Y. Each method is supported:

* `lmfit`: `process_fit_surface`
* `odr`: `process_fit_surface_odr`
* `emcee`: `process_fit_surface_emcee`

---

## MCMC Support (emcee)

All MCMC fits are handled via:

```python
_run_emcee(func, param_info, inputs, targets, sigma, fit_options, mode)
```

The `mode` argument changes the likelihood evaluation:

* `"1d"`
* `"per_y"` (multi 1D)
* `"surface"`

Returns:

```python
result: dict
sampler: emcee.EnsembleSampler
best_fit: np.ndarray
confidence_band: Tuple[np.ndarray, np.ndarray]
```

---

## Confidence Bands

The 99% confidence bands are:

* computed from `result.eval_uncertainty(sigma=3)` in `lmfit`
* extracted from the MCMC prediction percentiles
* approximated via the covariance matrix in `ODR`

---

## Method Summary

| Method                    | Role                                               |
| ------------------------- | -------------------------------------------------- |
| `generate_fit_function()` | Turns formula into executable Python function      |
| `prepare_parameters()`    | Extracts p0, bounds from FitOptions dialog         |
| `process_fit()`           | Entry for standard 1D fit                          |
| `process_fit_per_y()`     | Entry for multi-1D fit (Z = f(X), fixed Y)         |
| `process_fit_surface()`   | Entry for full surface fit                         |
| `_run_emcee()`            | Shared backend for MCMC fits                       |
| `_process_lmfit()`        | Core least-squares fitting with `lmfit.Model`      |
| `_process_odr()`          | Fitting using orthogonal distance regression (ODR) |
| `reset_fit()`             | Clears result, toolbar, and reinitializes plots    |

