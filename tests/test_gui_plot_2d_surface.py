import os

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from gcfpy.app.main_window import MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


@pytest.fixture
def surface_csv_path():
    return os.path.join(
        os.path.dirname(__file__), "../examples/data", "example_2d_fit_data.csv"
    )


@pytest.mark.parametrize("method", ["lmfit", "odr", "emcee"])
def test_plot_2d_surface_workflow(qtbot, surface_csv_path, method):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()

    window.add_fit_tab()
    fit_tab = window.get_current_fit_tab()

    df = pd.read_csv(surface_csv_path)
    fit_tab.load_data_into_tab(df, file_path=surface_csv_path)

    fit_tab.formula_text.setPlainText("z = a*x + b*y + c")
    fit_tab.fit_options_dialog.method_combo.setCurrentText(method)
    fit_tab.fit_control.strategy_selector.setCurrentText("Fit surface")

    qtbot.mouseClick(fit_tab.fit_control.run_fit_button, Qt.LeftButton)
    qtbot.waitUntil(lambda: fit_tab.results_text.toPlainText() != "", timeout=8000)

    def get_button_for_action(toolbar, action):
        for child in toolbar.findChildren(QWidget):
            if hasattr(child, "defaultAction") and child.defaultAction() == action:
                return child
        return None

    button = get_button_for_action(
        window.toolbar, window.toolbar.toggle_confidence_2d_action
    )
    if button and button.isEnabled():
        qtbot.mouseClick(button, Qt.LeftButton)
        qtbot.wait(500)

    qtbot.wait(200)
    window.close()
    qtbot.wait(200)
    plt.close("all")
