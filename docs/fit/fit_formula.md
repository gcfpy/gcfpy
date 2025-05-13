
# Fit Formula

The **Fit Formula** defines the mathematical model used to fit experimental data. It is entered directly into the application using symbolic syntax inspired by `SymPy`, and parsed into executable Python code behind the scenes.

Graphical Curve Fit for Python allows formulas to be written interactively in the interface, and automatically extracts all parameters to configure the fitting backend.

---

## Syntax and Supported Functions

A formula must be a single line that starts with `y =`, for 1D data, or `z =`, for 2D surface fits.

### 1D Model Example
```
y = a * sin(x) + b
```

### 2D Surface Model Example
```
z = a * x + b * y + c
```

The formula should:

It must:

- Start with `y=` or `z=`
- Use one or two independent variables: `x`, or `x` and `y`
- Use standard Python-style operators (`*`, `+`, `-`, `/`, `**` for exponentiation)
- Use supported mathematical functions

### Supported functions
These expressions are automatically translated to NumPy-compatible code:

| Function | Description          | Translated to     |
|----------|----------------------|-------------------|
| sin(x)   | sine                 | `np.sin(x)`       |
| abs(x)   | absolute             | `np.abs(x)`       |
| cos(x)   | cosine               | `np.cos(x)`       |
| tan(x)   | tangent              | `np.tan(x)`       |
| exp(x)   | exponential          | `np.exp(x)`       |
| log(x)   | natural log (ln)     | `np.log(x)`       |
| log10(x) | base-10 logarithm    | `np.log10(x)`     |
| sqrt(x)  | square root          | `np.sqrt(x)`      |
| arcsin   | inverse sine         | `np.arcsin(x)`    |
| arccos   | inverse cosine       | `np.arccos(x)`    |
| arctan   | inverse tangent      | `np.arctan(x)`    |
| sinh     | hyperbolic sine      | `np.sinh(x)`      |
| cosh     | hyperbolic cosine    | `np.cosh(x)`      |



---

## Constants

You can use the following scientific constants directly in your formula:

| Name | Meaning                     | Value               |
|------|-----------------------------|---------------------|
| `pi`  | pi                         | 3.14159…            |
| `e0`   | Euler’s number             | 2.71828…            |
| `placnk`   | Planck constant            | 6.626e-34           |
| `c0`   | Speed of light (m/s)       | 299792458           |
| `kB`  | Boltzmann constant         | 1.380649e-23        |
| `eV`  | Elementary charge (Coul.)  | 1.602176634e-19     |

These different parameters are in the `\gcfpy\utils\math_config.json`

---

## Formula Parsing

Once entered, the formula is internally parsed using:

- [`sympy`](https://www.sympy.org/) to extract parameters and check validity
- [`ast`](https://docs.python.org/3/library/ast.html) for code transformation into valid NumPy-compatible Python

If the formula is invalid or non-numeric, the system will display an error message.

### Parameter Extraction

All symbolic parameters (like `a`, `b`, `c`) are automatically extracted. excluding `x`, `y`, or `z`. 
The extracted parameters are used to:

- Define the `fit_function`
- The **Fit Options** panel, which allows setting initial values, bounds, and constraints

> See [Fit Options](fit_options.md) for more details on parameter configuration.

---

## Importing a Formula 

You can import a previously saved fit function by clicking the **Import Formula** button. The file must contain a Python function of the form:

```python
import numpy as np

def fit_function(x, a, b):
    return a * np.sin(x) + b
```

The application parses the `return` line reconstructs the symbolic expression (e.g., `y = a*sin(x) + b`).

---

## Exporting the Formula

Click the **Export Formula** button to save the current expression as a `.py` file. The saved function will be compatible with Python and NumPy, and contain all constants used.

Generated file:

```python
import numpy as np

def fit_function(x, a, b):
    return a * np.sin(x) + b
```
This function can be reused in other scripts or re-imported in the interface.

---

## Writing Your Own Function

You can also write your own `fit_function` manually in a `.py` file. Just make sure:

- You name the function `fit_function`
- It accepts `x` or `x, y` as arguments, followed by all parameters
- Return a NumPy-compatible array

Example:

```python
import numpy as np

def fit_function(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))
```

For surface code:

```python
def fit_function(x, y, a, b, c):
    return a * x + b * y + c
```

## Notes

- Only one formula is used per fit tab
- The formula is reset if you load incompatible data
- Fit strategies (1D, Multi-Y, Surface) determine whether `y=` or `z=` is expected
- Formula and parameters can be adjusted live during the session