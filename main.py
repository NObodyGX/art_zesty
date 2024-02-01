import sys
from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QLabel

from framework.button.b_button import (
    GTMinButton,
    GTMaxButton,
    GTOffButton,
    GOKButton,
    GNOButton,
)
from framework.theme.worker import GThemeWorker
from framework.window.b_window import GBaseWindow
from framework.label.number_label import GNumberLabel


class GMWindow(GBaseWindow):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.set_title("GXDToys")
        self.resize(540, 420)

    def center_layout(self):
        layout = QVBoxLayout()
        self.a1 = GTMinButton(self)
        self.a2 = GTMaxButton(self)
        self.a3 = GTOffButton(self)
        self.a4 = GOKButton(self)
        self.a5 = GNumberLabel()
        layout.addWidget(self.a1)
        layout.addWidget(self.a2)
        layout.addWidget(self.a3)
        layout.addWidget(self.a4)
        layout.addWidget(self.a5)
        return layout


if __name__ == "__main__":
    app = QApplication()
    win = GMWindow(None)
    GThemeWorker.apply(win, theme="default")
    win.show()
    sys.exit(app.exec())
