import matplotlib.pyplot as plt
import pytest
from PyQt5.QtWidgets import QApplication, QWidget


@pytest.fixture(autouse=True)
def cleanup_after_test(qtbot):
    yield

    plt.close("all")

    app = QApplication.instance()
    if app:
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QWidget) and widget.isVisible():
                widget.close()
                widget.deleteLater()
        app.processEvents()
