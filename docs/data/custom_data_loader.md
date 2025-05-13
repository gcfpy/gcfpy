# Adding a Custom Data Loader

This guide explains how to integrate a new data loading method into the application, in addition to the built-in CSV and HDF5 readers.

---

## 1. When to Customize

You may want to implement a custom loader when dealing with:

* JSON files
* Excel spreadsheets
* Proprietary binary formats
* Direct connections to databases or instruments

---

## 2. Where to Modify

The `DataLoader` class handles all file loading operations and is located in:

```
gcfpy/utils/data_loader.py
```

---

## 3. Implementing a New Loader

### Step 1 — Add a Method

Define a new method in the `DataLoader` class:

```python
def load_json_format(self, file_path):
    try:
        import json
        with open(file_path, "r") as f:
            data = json.load(f)
        df = pd.DataFrame({"X": data["X"], "Y": data["Y"]})
        return df
    except Exception as e:
        self.show_error_message(f"Failed to load JSON: {e}")
        return None
```

>  Make sure your method returns a `pandas.DataFrame` with columns `X` and `Y` (and optionally `Z`, `X_err`, `Y_err`).

---

### Step 2 — Register the Extension

Update the main `read_file()` method to detect and dispatch based on the file extension:

```python
if file_name.endswith(".json"):
    self.df = self.load_json_format(file_name)
```

You may also update the file dialog to list `.json` as a supported extension if needed.

---

## 4. No Further Changes Needed

Once your custom loader returns a valid DataFrame:

* The X/Y table will be populated
* The data will appear in the plot
* The fit panel and toolbar will be enabled

No need to modify any part of the fitting or visualization pipeline.
