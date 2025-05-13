# Toolbar

The toolbar provides quick access to key actions for running fits, adjusting plots, and managing the visual interface. It remains visible at the top of the application window and adapts dynamically based on the current data or fit state.

---

### Fit Management
* **Add to Comparison**: Save the current fit to the comparison buffer.
* **Toggle Comparison Mode**: Display multiple saved fits on the same plot.

These options are  visible when a fit is active. This option is available for 1D and multi 1D fits and is not available for 2D fits.

### Plot Controls

Enable or disable the following visual layers:

* **99% Confidence Band**: Visualize uncertainty of the fit.
* **Residuals**: Plot the difference between data and model.
* **Component Decomposition**: Show each term in the model separately.
* **2D Confidence Contours**: View parameter uncertainty in surface fits.

These options are  visible when a fit is active. Options are for for 1D fit. These options are not available for fits made with `emcee`. The 2D countour has not been integrated for the fit using `scipy.odr`. 
To see how these plots are made, examples can be found in the file examples/plot.

### Domain Selection

* **Set X Range**: Activate the **Xmin/Xmax** tool to restrict the domain used for fitting. For 1D fit.

### Preprocessing Options

* **Smoothing**: Apply a filter to the data before fitting.
* **Weighting**: Adjust the weight of each point during the fit.

---

## Toolbar Button Types

### Toggle Buttons

* Icon-based buttons that control visibility of features like confidence intervals or residuals.
* Buttons are highlighted when active and update the plot immediately.

### Dropdown Menus

Used for mutually exclusive options:

- **Smoothing**:
    - Gaussian (Savitzky-Golay)
    - Moving Average
    - None (default choice)

- **Weighting**:
    - `x error`: error on the x data need x_err column in the .csv (odr fit only)
    - `y error`: error on y data need y_err column in .csv file
    - `x and y error`: error on the x an y data need x_err an y_err columns in the .csv (odr fit only)
    - None

Only avaible  for 1D fit

---

## Dynamic Behavior

* Toolbar buttons are **disabled by default**.
* They are **enabled automatically** when:

  * A dataset is successfully loaded
  * A valid model is defined and a fit is performed
* Actions reflect their state in real-time (e.g., toggling residuals updates the plot immediately).
* Smoothing and weighting are mutually exclusive: only one method can be active per category at a time.

---
