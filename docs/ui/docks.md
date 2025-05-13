# Dock Widgets

Dock widgets are key components of the graphical interface. Each one provides a specific view or control for fitting, plotting, or data inspection. Docks can be  hidden, or restored via the **View** menu.

---

## Overview

By default, the following dock widgets are available in each fitting tab:

| Dock Name      | Purpose                                     |
| -------------- | ------------------------------------------- |
| Fit Formula    | Enter and edit the fitting equation         |
| Fit Results    | Display fit report and estimated parameters |
| Manual Control | Adjust parameters manually with sliders     |
| X/Y Data       | Inspect the loaded dataset in tabular form  |
| Plot Area      | Visualize raw data, fits, and diagnostics   |

---

## 1. Fit Formula

* Allows symbolic definition of the model using a Python-like syntax.
* Formula must start with `y =`, e.g., `y = a * x + b`.
* Parameters are automatically extracted and synchronized with the Fit Options.
* Functions like `exp`, `log`, `sin`, `abs`, and physical constants can be used.

Actions:

* Import or export formulas
* Open the Fit Options window
* Update formula dynamically with the fit mode (1D, 2D)

---

## 2. Fit Results

* Displays results after fitting:

  * Best-fit values
  * Confidence intervals
  * Goodness-of-fit metrics (e.g., χ², R²)
* Updated live after each fit
* Hidden until a fit is completed

---

## 3. Manual Control

* Provides sliders to control parameter values manually.
* Useful for visually exploring parameter space or preparing a good initial guess.
* Can be toggled from the toolbar.
* Automatically updates the plot in real time.

---

## 4. X/Y Data

* Displays the currently loaded dataset in table format.
* Adapts to data content (1D or 2D):

  * Shows `X`, `Y`, and optionally `Z`, `X_err`, `Y_err`, `Z_err`.
* Allows user to inspect data before fitting.
* Automatically appears after loading a valid file.

---

## 5. Plot Area

* Central area for displaying:

  * Raw data
  * Fitted curve
  * Residuals
  * Confidence bands
  * Decomposed components
* Interacts with toolbar toggles
* Automatically updated after data load or fit execution

---

## Managing Docks

* Docks can be moved, closed, or rearranged freely.
* Use `View > Restore Default Layout` to reset the layout.
* Visibility of individual docks can be toggled via the `View` menu.
