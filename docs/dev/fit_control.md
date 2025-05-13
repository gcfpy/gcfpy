# `FitControl`

The `FitControl` class manages the orchestration of the fitting process for a given dataset. It instantiates and controls the **Fit Control dock**, handles the execution of the fit across all modes (1D, multi-1D, surface), and communicates with the `FitProcessor`, `MainWindow` toolbar, and `PlotWidget`.

---

## Role in the Application

* Resides inside each `FitTab` as a dock widget
* Provides main buttons: **Run Fit**, **Reset Fit**, and **Manual**
* Manages fit execution for all strategies and methods (`lmfit`, `odr`, `emcee`)
* Delegates core fitting to `FitProcessor`
* Updates fit reports, plot visuals, and toolbar state accordingly

---

## Interface Overview

The `FitControl` dock contains:

* **Run Fit** button
* **Reset Fit** button
* **Manual** toggle (for opening sliders)
* Optional **strategy combo box** when in 2D mode:

  * `Fit surface`
  * `Fit per Y`

The dock is built dynamically using a vertical layout (`QVBoxLayout`) and is hidden by default.

---

## Fit Modes Supported

| Mode          | Description                                        |
| ------------- | -------------------------------------------------- |
| `1D`          | Standard curve fit  y = f(x)                     |
| `Fit per Y`   | Multi-curve fit z = f(x) at fixed y slices |
| `Fit surface` | Full 2D model fit z = f(x, y)                |

The mode is automatically determined by the data shape (`X,Y` vs `X,Y,Z`). The strategy is only visible in 2D.

---

## Fit Execution Logic

Each time **Run Fit** is clicked, the following occurs:

```python
method = fit_options.get("method", "leastsq")
strategy = self.strategy_selector.currentText()

if mode == "2D":
    if strategy == "Fit per Y":
        self._run_fit_per_y(method)
    else:
        self._run_fit_surface(method)
else:
    self._run_fit_process(method)
```

Each sub-method handles:

* formula parsing
* data extraction
* call to `FitProcessor`
* storing results into `PlotWidget`
* updating toolbar and result dock

---

## Grouped Methods in `FitControl`

### 1. Initialization and UI

| Method                        | Description                           |
| ----------------------------- | ------------------------------------- |
| `__init__()`                  | Initializes dock and internal widgets |
| `_init_ui()`                  | Calls all UI setup sub-methods        |
| `_create_dock()`              | Builds and inserts the dock           |
| `_create_buttons()`           | Sets up Run, Reset, Manual buttons    |
| `_create_strategy_selector()` | Adds strategy combo box for 2D        |
| `_assemble_layout()`          | Finalizes layout with all components  |

---

### 2. Fit Dispatchers

| Method               | Description                        |
| -------------------- | ---------------------------------- |
| `run_fit()`          | Top-level dispatcher for all modes |
| `_run_fit_process()` | Runs 1D fit                        |
| `_run_fit_per_y()`   | Runs multi 1D (Fit per Y)          |
| `_run_fit_surface()` | Runs 2D surface fit                |

---

### 3. Result Handling and Reporting

| Method                   | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `_handle_fit_result()`   | Receives result and updates plot, dock, toolbar |
| `_generate_fit_report()` | Calls formatting function depending on method   |
| `_format_emcee_report()` | Formats result dict from MCMC                   |
| `_format_odr_report()`   | Formats ODR result into readable string         |

---

### 4. Utility and Sync

| Method                              | Description                               |
| ----------------------------------- | ----------------------------------------- |
| `reset_fit()`                       | Resets plot and toolbar to default state  |
| `display_fit_results()`             | Makes fit panel visible                   |
| `get_formula_or_warn()`             | Reads formula or shows error dialog       |
| `_get_selected_or_full_data()`      | Extracts X/Y/Z from selection or all data |
| `update_strategy_selector(visible)` | Shows/hides strategy selector             |
| `get_current_strategy()`            | Returns selected strategy for 2D fit      |
| `_on_strategy_change()`             | Updates plots when strategy is changed    |

---

## Related Modules

| Module             | Role                                           |
| ------------------ | ---------------------------------------------- |
| `fit_tab.py`       | Hosts the `FitControl` dock inside each tab    |
| `fit_processor.py` | Implements actual fit logic and dispatch       |
| `plot_widget.py`   | Receives and displays fits and confidence data |
| `toolbar.py`       | Updated by `FitControl` to reflect fit state   |
| `fit_formula.py`   | Provides the input formula as text             |

---

## Notes

* `FitControl` does **not** manage formula or data directly — it pulls them from its parent `FitTab`
* All fit result objects are stored in `PlotWidget` after processing, including residuals and confidence bands
* The dock remains hidden unless data is loaded
