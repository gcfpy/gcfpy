# Data Loader

The `DataLoader` class handles the import and validation of user-provided data files before they are passed to the application’s visualization and fitting components.

---

## Responsibilities

* Open files using a dialog or programmatic input
* Read and validate `.csv` content
* Ensure required columns (`X`, `Y`) are present
* Reject malformed or incomplete data
* Return a clean `pandas.DataFrame` for downstream use

---

## Supported Formats

* `.csv` (standard)
* Custom loaders can be added (see [Custom Loader Guide](custom_data_loader.md))

---

## Main Methods

### `load_data(file_name=None)`

* Opens a file dialog (if `file_name` is not passed)
* Dispatches to the appropriate read method
* On success, returns a validated `DataFrame` and the file path

### `read_csv(file_path)`

* Uses `pandas.read_csv()` to load file
* Validates presence of `X` and `Y` columns
* Checks for NaNs or non-numeric values

### `show_error_message(message)`

* Uses `QMessageBox` to inform the user of errors (e.g., missing columns or invalid format)

---

## Typical Integration

```python
df, file_path = data_loader.load_data()
if df is not None:
    tab.load_data_into_tab(df, file_path)
```

Once the data is loaded:

* The table view (`X/Y Data`) is updated
* The main plot is refreshed
* Toolbar actions are enabled
* Fit controls become accessible
