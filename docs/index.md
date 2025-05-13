# Graphical Curve Fit for Python

**gcfpy** is a graphical application for building, executing, and analyzing curve fitting workflows. Designed for scientists and engineers, it provides an interactive environment for fitting experimental data using user-defined models.

You can define models using a formula interface based on `SymPy` syntax, fit data using least-squares (`lmfit`), Bayes  ian methods (`emcee`) or orthogonal distance regression (`scipy`), and compare multiple fits.


## Key Features

* Define custom models using symbolic formulas
* Fit using least-squares (lmfit), orthogonal distance regression (scipy.odr), or MCMC (emcee)
* Visualise residuals, confidence bands, and component contributions
* Run and compare multiple fits in parallel tabs
* Adjust parameters manually and explore model behavior
* Import/export data and fit results (CSV)
 

The gcfpy package is free software, using an Open Source license. The software and this document are works in progress. If you are interested in participating in this effort please use the [Git repository](https://github.com/gcfpy/gcfpy).

---
## User guide
* **[Getting started](user_guide/getting_started.md)**: How to begin using the application
* **[Installation](user_guide/install.md)**: Instructions for installing gcfpy and required dependencies
* **[Getting Help](user_guide/help.md)**: Where to look when you're stuck

## Tutorials

* **[Basic fit](tutorials/basic_fit.md)**: Start with a simple 1D fit using a basic formula on noisy data.
* **[Plots lmfit/odr](tutorials/plots.md)**: Explore confidence bands, residuals, decomposition, and 2D contour plots (for non-MCMC methods).
* **[Plots mcmc](tutorials/mcmc.md)**: Run a full MCMC fit and visualize results with corner, walkers, autocorrelation, and 99% bands.
* **[Multi 1D fit](tutorials/multi_1d.md)**: Perform 1D fits across slices of Y in a 2D dataset (Z = f(X), Y fixed), with a global formula including `y`.
* **[2D fit](tutorials/2d_fit.md)**: Fit a full surface model Z = f(X, Y), using 2D plotting, surface rendering, and projections.
* **[Manual fit](tutorials/manual_fit.md)**: Manually adjust parameters using sliders and observe the live response.
* **[Comparison](tutorials/comparison.md)**: Store, toggle, and compare multiple fits using the integrated comparison tool.


## Application Sections

* **[UI Overview](ui/overview.md)**: Introduction to the interface layout and navigation
* **[Menus](ui/menus.md)**: File, view, and advanced menu actions
* **[Toolbar](ui/toolbar.md)**: Quick-access actions for fitting, plotting, and toggles
* **[Docks](ui/docks.md)**: Modular panels for formulas, plots, results, and data inspection 

### Model Definition & Execution

* **[Formula Editor](fit/fit_formula.md)**: Writing and importing formulas using SymPy/NumPy syntax
* **[Fit Options](fit/fit_options.md)**: Customizing method, bounds, initial values, and strategy
* **[Manual Fit](fit/manual.md)**: Interactive sliders for manual parameter adjustment
* **[Comparison Mode](fit/fit_comparison.md)**: Save and compare multiple fits
* **[Fit result](fit/results.md)**: View numerical fit reports and graphical diagnostics (residuals, decomposition, etc.) 
* **[MCMC result](fit/mcmc.md)**: corner plots, autocorrelation diagnostics, uncertainty intervals  


## Working with Data

* **[Load Data](data/data_loader.md)**: Supported formats and loading mechanisms (CSV)
* **[Add Custom Loaders](data/custom_data_loader.md)**: Extend data input with custom logic

---

## Developpment 
* **[Overview](dev/overview.md)**: Supported formats and loading mechanisms (CSV)
* **[FitTab](dev/fit_tab.md)**: Main workspace for fitting operations and data handling
* **[Toolbar](dev/toolbar.md)**: Toolbar setup, menus, and action handling
* **[Fit Control](dev/fit_control.md)**: Fit parameter selection and orchestration
* **[Fit Processor](dev/fit_processor.md)**: Core fitting logic (lmfit, odr, emcee)
* **[Fit Comparison](dev/fit_comparison.md)**: Manage, display, and export multiple fits
* **[Plot System](dev/plot.md)**: 1D, 2D, an mcmc


## More Information

* **Dependencies**: `PyQt5`, `lmfit`, `emcee`, `scipy`, `pandas`, `numpy`, `matplotlib`
* **Source code**: [Git repository](https://github.com/gcfpy/gcfpy)
* **License**: MIT License



