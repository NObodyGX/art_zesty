import sys
from PySide6.QtWidgets import QApplication
from .framework.theme.worker import GThemeWorker


def run(winclass):
    app = QApplication()
    win = winclass()
    GThemeWorker.apply(win, theme=GThemeWorker.GThemeEnum.default)
    win.show()
    sys.exit(app.exec())
