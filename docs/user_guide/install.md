
# Installation

## Prerequisites

Graphical Curve Fit for Python requires **Python 3.8 or higher**. The following Python packages are needed for the core functionality:

| Package            | Version (min) | Purpose                            |
| ------------------ | ------------- | ---------------------------------- |
| `numpy`            | 1.20          | Array handling                     |
| `pandas`           | 1.3           | Dataframes and CSV management      |
| `matplotlib`       | 3.5           | Plotting                           |
| `PyQt5`            | 5.15          | Graphical interface                |
| `lmfit`            | 1.1           | Non-linear least-squares fitting   |
| `emcee`            | —             | Bayesian inference via MCMC        |
| `scipy`            | 1.8           | ODR fitting method                 |
| `sympy`            | —             | Symbolic formulas                  |
| `corner`           | —             | MCMC corner plots                  |
| `tqdm`             | —             | Progress bars                      |
| `sip`, `pyqt5-sip` | —             | Required for PyQt bindings         |
| `numdifftools`     | —             | (optional) Numerical derivatives   |

> These packages are all available on PyPI and will be installed automatically with `pip` if you use the instructions below.

---

## Installing the Application

To install the stable version from source:

```bash
git clone https://github.com/gcfpy/gcfpy
cd gcfpy
pip install -e .
```

This installs all required dependencies and enables you to run the application. To start it, run the following command in your terminal:

```bash
gcfpy
```

---

## Developer Installation

To install Graphical Curve Fit for Python in *editable mode* with development dependencies (formatting, tests, documentation):

```bash
pip install -e .[dev,test,doc]
```

This will include:

* `black`, `ruff`, `isort`, `flake8`: Code formatting and linting
* `pytest`, `pytest-qt`, `coverage`: Unit and GUI testing
* `mkdocs`, `mkdocs-material`, `mkdocstrings[python]`,`mkdocs-mermaid2-plugin`,`pymdown-extensions`: Documentation generation

You can also install subsets:

```bash
pip install -e .[dev]      # Dev tools only
pip install -e .[test]     # Testing tools only
pip install -e .[doc]      # Documentation tools only
```

---

## Additional Notes

* No Conda or pypi package is currently maintained.
* The application is **graphical** and needs a desktop environment.
* Example datasets can be found in the `examples/data/` folder of the repository.

